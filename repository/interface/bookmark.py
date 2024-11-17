import abc


class IBookmarkHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_unread_items(self) -> list:
        # return URL lists
        raise NotImplementedError

    @abc.abstractmethod
    def archive_item(self, url) -> None:
        raise NotImplementedError
        
    @abc.abstractmethod
    def delete_item(self, url) -> None:
        raise NotImplementedError
