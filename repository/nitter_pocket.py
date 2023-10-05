import time

import requests

from repository.base_pocket import BasePocketHandler


class NitterPocketHandler(BasePocketHandler):
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
