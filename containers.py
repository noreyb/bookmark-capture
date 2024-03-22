from injector import Module

from repository.booru_pocket import BooruPocketHandler
from repository.fdv_pocket import FDVPocketHandler
from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from repository.kmn_pocket import KMNPocketHandler
from repository.ngk_pocket import NGKPocketHandler
from repository.pcloud import PCloudHandler
from repository.twitter_pocket import TwitterPocketHandler
from usecase.booru_image_downloader import BooruImageDownloader
from usecase.fdv_image_downloader import FDVImageDownloader
from usecase.interface.image_downloader import IImageDownloader
from usecase.kmn_image_downloader import KMNImageDownloader
from usecase.ngk_image_downloader import NGKImageDownloader
from usecase.twitter_image_downloader import TwitterImageDownloader


class TwitterFactory(Module):
    def __init__(
        self,
        token: str,
        consumer_key: str,
        pc_username: str,
        pc_password: str,
        save_dir: str,
        output_dir: str,
    ):
        self.token = token
        self.consumer_key = consumer_key
        self.pc_username = pc_username
        self.pc_password = pc_password
        self.save_dir = save_dir
        self.output_dir = output_dir

    def configure(self, binder):
        binder.bind(
            IImageDownloader,
            to=TwitterImageDownloader(
                TwitterPocketHandler(
                    token=self.token,
                    consumer_key=self.consumer_key,
                ),
                PCloudHandler(
                    username=self.pc_username,
                    password=self.pc_password,
                    save_dir=self.save_dir,
                ),
                self.output_dir,
            ),
        )


class NGKFactory(Module):
    def __init__(
        self,
        token: str,
        consumer_key: str,
        pc_username: str,
        pc_password: str,
        save_dir: str,
        output_dir: str,
    ):
        self.token = token
        self.consumer_key = consumer_key
        self.pc_username = pc_username
        self.pc_password = pc_password
        self.save_dir = save_dir
        self.output_dir = output_dir

    def configure(self, binder):
        binder.bind(
            IImageDownloader,
            to=NGKImageDownloader(
                NGKPocketHandler(
                    token=self.token,
                    consumer_key=self.consumer_key,
                ),
                PCloudHandler(
                    username=self.pc_username,
                    password=self.pc_password,
                    save_dir=self.save_dir,
                ),
                self.output_dir,
            ),
        )


class FDVFactory(Module):
    def __init__(
        self,
        token: str,
        consumer_key: str,
        pc_username: str,
        pc_password: str,
        save_dir: str,
        output_dir: str,
    ):
        self.token = token
        self.consumer_key = consumer_key
        self.pc_username = pc_username
        self.pc_password = pc_password
        self.save_dir = save_dir
        self.output_dir = output_dir

    def configure(self, binder):
        binder.bind(
            IImageDownloader,
            to=FDVImageDownloader(
                FDVPocketHandler(
                    token=self.token,
                    consumer_key=self.consumer_key,
                ),
                PCloudHandler(
                    username=self.pc_username,
                    password=self.pc_password,
                    save_dir=self.save_dir,
                ),
                self.output_dir,
            ),
        )


class BooruFactory(Module):
    def __init__(
        self,
        token: str,
        consumer_key: str,
        pc_username: str,
        pc_password: str,
        save_dir: str,
        output_dir: str,
    ):
        self.token = token
        self.consumer_key = consumer_key
        self.pc_username = pc_username
        self.pc_password = pc_password
        self.save_dir = save_dir
        self.output_dir = output_dir

    def configure(self, binder):
        binder.bind(
            IImageDownloader,
            to=BooruImageDownloader(
                BooruPocketHandler(
                    token=self.token,
                    consumer_key=self.consumer_key,
                ),
                PCloudHandler(
                    username=self.pc_username,
                    password=self.pc_password,
                    save_dir=self.save_dir,
                ),
                self.output_dir,
            ),
        )


class KMNFactory(Module):
    def __init__(
        self,
        token: str,
        consumer_key: str,
        pc_username: str,
        pc_password: str,
        save_dir: str,
        output_dir: str,
    ):
        self.token = token
        self.consumer_key = consumer_key
        self.pc_username = pc_username
        self.pc_password = pc_password
        self.save_dir = save_dir
        self.output_dir = output_dir

    def configure(self, binder):
        binder.bind(
            IImageDownloader,
            to=KMNImageDownloader(
                KMNPocketHandler(
                    token=self.token,
                    consumer_key=self.consumer_key,
                ),
                PCloudHandler(
                    username=self.pc_username,
                    password=self.pc_password,
                    save_dir=self.save_dir,
                ),
                self.output_dir,
            ),
        )
