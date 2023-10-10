import time

import requests
from bs4 import BeautifulSoup
from PIL import Image, UnidentifiedImageError

from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from usecase.interface.image_downloader import IImageDownloader


class KMNImageDownloader(IImageDownloader):
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
                output_path = self.download_image(url)
            except Exception as e:
                print(e)
                continue
            for path in output_path:
                self.storage.upload_file(path)
            self.bookmark.archive_item(url)
        return None

    def download_image(self, url: str) -> str:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        time.sleep(1)

        output_path_list = []
        soup = soup.find_all(class_="post__thumbnail")
        for elem in soup:
            image_url = elem.find("a")["href"]
            file_name = image_url.split("?f=")[1]

            r = requests.get(image_url)
            time.sleep(1)
            output_path = f"{self.output_dir}/{file_name}"
            with open(output_path, "wb") as f:
                f.write(r.content)
            try:
                image = Image.open(output_path)
            except UnidentifiedImageError:
                raise Exception(f"UnidentifiedImageError: {file_name}, url: {url}")
            image.save(output_path, quality=85)
            output_path_list.append(output_path)

        return output_path_list
