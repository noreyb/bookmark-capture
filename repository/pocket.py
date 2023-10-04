from repository.interface.bookmark import IBookmarkHandler
import requests


class PocketHandler(IBookmarkHandler):
    def __init__(self, token: str, consumer_key: str) -> None:
        self.token = token
        self.consumer_key = consumer_key

    def get_unread_items(self) -> list:
        url = "http://getpocket.com/v3/get"
        data = {
            "consumer_key": self.consumer_key,
            "access_token": self.token,
            "state": "unread",
            "domain": "nitter.net",
        }
        resp = requests.post(url, data=data)
        resp = resp.json()

        if len(resp["list"]) == 0:
            print("No item in pocket")
            exit()

        return [item["given_url"] for item in resp["list"].values()]

    def archive_item(self, url) -> None:
        return super().archive_item(url)