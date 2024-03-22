import time

import requests
from PIL import Image, UnidentifiedImageError

from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from usecase.interface.image_downloader import IImageDownloader


class NGKImageDownloader(IImageDownloader):
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
                self.bookmark.archive_item(url)
                continue
            self.storage.upload_file(output_path)
            self.bookmark.archive_item(url)
        return None

    def download_image(self, url: str) -> str:
        r = requests.get(url)
        time.sleep(1)

        file_name = url.split("/")[-1]
        # ファイル名の揺れを吸収するための処理
        if "?" in file_name:
            file_name = file_name.split("?")[0]
        if len(file_name) >= 200:
            file_name = file_name[-200:]
        if "." not in file_name:
            raise Exception(f"file_name: {file_name}, url: {url}")

        output_path = f"{self.output_dir}/{file_name}"
        with open(output_path, "wb") as f:
            f.write(r.content)
        try:
            image = Image.open(output_path)
        except UnidentifiedImageError:
            raise Exception(f"UnidentifiedImageError: {file_name}, url: {url}")
        image.save(output_path, quality=85)

        return output_path
