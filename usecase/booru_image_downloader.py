import time

import requests
from bs4 import BeautifulSoup
from PIL import Image, UnidentifiedImageError

from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from usecase.interface.image_downloader import IImageDownloader


class BooruImageDownloader(IImageDownloader):
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
            self.bookmark.delete_item(url)
        return None

    def download_image(self, url: str) -> str:
        url = url.replace("&amp;", "&")

        # gelbooruのURLの先の画像URLを取得する
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        time.sleep(1)

        for elem in soup.find_all("picture"):
            url = elem.find("img")["src"]
        r = requests.get(url)
        time.sleep(5)
        if r.status_code != requests.codes.ok:
            raise Exception(f"status_code: {r.status_code}, url: {url}")

        file_name = url.split("/")[-1]
        output_path = f"{self.output_dir}/{file_name}"
        with open(output_path, "wb") as f:
            f.write(r.content)
        try:
            image = Image.open(output_path)
        except UnidentifiedImageError:
            raise Exception(f"UnidentifiedImageError: {url}")
        image.save(output_path, quality=85)
        return output_path
