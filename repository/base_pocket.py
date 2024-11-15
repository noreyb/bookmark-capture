import time

import requests

from repository.interface.bookmark import IBookmarkHandler


class BasePocketHandler(IBookmarkHandler):
    def __init__(self, token: str, consumer_key: str) -> None:
        self.token = token
        self.consumer_key = consumer_key

    def archive_item(self, url) -> None:
        # get item_id from url
        endpoint = "https://getpocket.com/v3/get"
        resp = requests.post(
            endpoint,
            data={
                "consumer_key": self.consumer_key,
                "access_token": self.token,
                "search": url,
            },
        )
        # Error handling
        if resp.status_code != requests.codes.ok:
            raise Exception(f"status_code: {resp.status_code}, url: {url}")

        resp = resp.json()
        time.sleep(1)
        if resp["status"] == 2:
            # This item has been deleted
            return None
        item_id = resp["list"][list(resp["list"].keys())[0]]["item_id"]

        # archive item
        endpoint = "http://getpocket.com/v3/send"
        data = {
            "consumer_key": self.consumer_key,
            "access_token": self.token,
            "actions": [
                {
                    "action": "archive",
                    "item_id": item_id,
                }
            ],
        }
        headers = {"Content-type": "application/json", "X-accept": "application/json"}
        resp = requests.post(endpoint, json=data, headers=headers)
        if resp.status_code != requests.codes.ok:
            raise Exception(f"status_code: {resp.status_code}, url: {url}")
        time.sleep(1)

    
    def delete_item(self, url) -> None:
        # get item_id from url
        endpoint = "https://getpocket.com/v3/get"
        resp = requests.post(
            endpoint,
            data={
                "consumer_key": self.consumer_key,
                "access_token": self.token,
                "search": url,
            },
        )
        # Error handling
        if resp.status_code != requests.codes.ok:
            raise Exception(f"status_code: {resp.status_code}, url: {url}")

        resp = resp.json()
        time.sleep(1)
        if resp["status"] == 2:
            # This item has been deleted
            return None
        item_id = resp["list"][list(resp["list"].keys())[0]]["item_id"]

        # archive item
        endpoint = "http://getpocket.com/v3/send"
        data = {
            "consumer_key": self.consumer_key,
            "access_token": self.token,
            "actions": [
                {
                    "action": "delete",
                    "item_id": item_id,
                }
            ],
        }
        headers = {"Content-type": "application/json", "X-accept": "application/json"}
        resp = requests.post(endpoint, json=data, headers=headers)
        if resp.status_code != requests.codes.ok:
            raise Exception(f"status_code: {resp.status_code}, url: {url}")
        time.sleep(1)
