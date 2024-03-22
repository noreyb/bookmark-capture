import os
import time
from urllib.parse import unquote, urlparse

import requests
from PIL import Image, UnidentifiedImageError

from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from usecase.interface.image_downloader import IImageDownloader


class TwitterImageDownloader(IImageDownloader):
    def __init__(
        self,
        bookmark_handler: IBookmarkHandler,
        storage_handler: IStorageHandler,
        output_dir: str,
    ) -> None:
        self.bookmark = bookmark_handler
        self.storage = storage_handler
        self.output_dir = output_dir

    def run(self) -> None:
        # pocketのurlを取得
        urls = self.bookmark.get_unread_items()
        # 画像ダウンロード
        for url in urls:
            try:
                # url = urldefrag(url)[0]
                output_path = self.download_image(url)
            except Exception as e:
                print(e)
                continue
            self.storage.upload_file(output_path)
            self.bookmark.archive_item(url)
        return None

    def download_image(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "ja,en-US;q=0.7,en;q=0.3",
            # 'Accept-Encoding': 'gzip, deflate, br',
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
        }
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            time.sleep(5)

            parsed_url = urlparse(url)
            query_params = dict(qc.split("=") for qc in parsed_url.query.split("&"))
            extension = query_params.get("format", "jpg")

            path_parts = parsed_url.path.split("/")
            file_name = f"{path_parts[-1]}.{extension}"
            file_name = unquote(file_name)

            output_path = os.path.join(self.output_dir, file_name)
            with open(output_path, "wb") as f:
                f.write(r.content)

            image = Image.open(output_path)
            image.save(output_path, quality=85)

            return output_path

        except requests.exceptions.RequestException as e:
            raise Exception(f"status_code: {r.status_code}, url: {url}")

        except UnidentifiedImageError as e:
            raise Exception(f"UnidentifiedImageError: {url}")
