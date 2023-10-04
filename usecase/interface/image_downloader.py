import abc
from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler


class IImageDownloader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, bookmark_handler: IBookmarkHandler, storage_handler: IStorageHandler, output_dir: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def download_image(self, url: str) -> None:
        raise NotImplementedError