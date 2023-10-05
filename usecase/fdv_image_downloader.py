import time
import json

import requests
from PIL import Image, UnidentifiedImageError
from urllib.parse import unquote, urlparse

from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from usecase.interface.image_downloader import IImageDownloader


class FDVImageDownloader(IImageDownloader):
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
            self.storage.upload_file(output_path)
            self.bookmark.archive_item(url)
        return None

    def download_image(self, url: str) -> str:
        if len(urlparse(url).path.split("/")) < 3:  # Only note get
            raise Exception(f"Invalid url: {url}")
        note_id = urlparse(url).path.split("/")[2]

        # Get image url
        # Get misskey post by notes/show endpoint
        host = "https://misskey.io/api"
        endpoint = "notes/show"
        data = {"noteId": note_id}
        r = requests.post(
            f"{host}/{endpoint}",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )

        if "error" in r.json().keys():
            raise Exception(f"status_code: {r.status_code}, url: {url}")

        files = r.json()["files"]
        for f in files:
            image_url = unquote(f["url"])
            file_name = image_url.split("/")[-1]
            r = requests.get(image_url)

            output_path = f"{self.output_dir}/{file_name}"
            with open(output_path, "wb") as f:
                f.write(r.content)
            try:
                image = Image.open(output_path)
            except UnidentifiedImageError:
                raise Exception(f"UnidentifiedImageError: {file_name}, url: {url}")
            image.save(output_path, quality=85)
        return output_path