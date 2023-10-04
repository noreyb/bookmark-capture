from usecase.interface.image_downloader import IImageDownloader
from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
import requests
import time

class NitterImageDownloader(IImageDownloader):
    def __init__(self, bookmark_handler: IBookmarkHandler, storage_handler: IStorageHandler, output_dir: str) -> None:
        self.bookmark = bookmark_handler
        self.storage = storage_handler
        self.output_dir = output_dir

    def run(self) -> None:
        # pocketのurlを取得
        urls = self.bookmark.get_unread_items()
        print(urls)
        # 画像ダウンロード       
        # pcloudへ保存
        return None

    def get_image(self, url: str) -> None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }
        r = requests.get(url, headers=headers)
        time.sleep(2)
        if r.status_code != requests.codes.ok:
            return None
        file_name = url.split("/")[-1]
        return (r.content, file_name)