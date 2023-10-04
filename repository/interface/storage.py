import abc


class IStorageHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def upload_file(self, src_path: str) -> None:
        raise NotImplementedError