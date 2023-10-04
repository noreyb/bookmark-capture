from repository.interface.bookmark import IBookmarkHandler


class PocketHandler(IBookmarkHandler):
    def __init__(self, token: str, consumer_key: str) -> None:
        super().__init__()

    def get_unread_items(self) -> list:
        return super().get_unread_items()

    def archive_item(self, url) -> None:
        return super().archive_item(url)