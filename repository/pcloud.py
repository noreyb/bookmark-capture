from repository.interface.storage import IStorageHandler


class PCloudHandler(IStorageHandler):
    def __init__(self, username: str, password: str, save_dir: str) -> None:
        self.username = username
        self.password = password
        self.save_dir = save_dir

    def upload_file(self, src_path: str) -> None:
        # save_dirを使う
        return super().upload_file(src_path)