from repository.interface.storage import IStorageHandler
from pcloud import PyCloud
import time


class PCloudHandler(IStorageHandler):
    def __init__(self, username: str, password: str, save_dir: str) -> None:
        self.username = username
        self.password = password
        self.save_dir = save_dir

    def upload_file(self, src_path: str) -> None:
        pc = PyCloud(self.username, self.password)
        pc.uploadfile(files=[src_path], path=self.save_dir)
        time.sleep(1)
        return None