import abc


class IStorageHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_image(self, src_path, dst_dir) -> None:
        raise NotImplementedError