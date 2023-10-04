from repository.interface.storage import IStorageHandler


class PCloudHandler(IStorageHandler):
    def __init__(self, username: str, password: str) -> None:
        super().__init__()

    def save_image(self, src_path, dst_dir) -> None:
        return super().save_image(src_path, dst_dir)