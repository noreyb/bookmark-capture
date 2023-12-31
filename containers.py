# Dependency_injectorのContainerをusecase毎に作成する
from dependency_injector import containers, providers

from repository.booru_pocket import BooruPocketHandler
from repository.fdv_pocket import FDVPocketHandler
from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler
from repository.kmn_pocket import KMNPocketHandler
from repository.ngk_pocket import NGKPocketHandler
from repository.nitter_pocket import NitterPocketHandler
from repository.pcloud import PCloudHandler
from usecase.booru_image_downloader import BooruImageDownloader
from usecase.fdv_image_downloader import FDVImageDownloader
from usecase.interface.image_downloader import IImageDownloader
from usecase.kmn_image_downloader import KMNImageDownloader
from usecase.ngk_image_downloader import NGKImageDownloader
from usecase.nitter_image_downloader import NitterImageDownloader


class NitterContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(
        NitterPocketHandler, token=config.token, consumer_key=config.consumer_key
    )
    storage_handler = providers.Factory(
        PCloudHandler,
        username=config.pc_username,
        password=config.pc_password,
        save_dir=config.save_dir,
    )
    image_downloader = providers.Factory(
        NitterImageDownloader,
        bookmark_handler=bookmark_handler,
        storage_handler=storage_handler,
        output_dir=config.output_dir,
    )


class NGKContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(
        NGKPocketHandler, token=config.token, consumer_key=config.consumer_key
    )
    storage_handler = providers.Factory(
        PCloudHandler,
        username=config.pc_username,
        password=config.pc_password,
        save_dir=config.save_dir,
    )
    image_downloader = providers.Factory(
        NGKImageDownloader,
        bookmark_handler=bookmark_handler,
        storage_handler=storage_handler,
        output_dir=config.output_dir,
    )


class FDVContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(
        FDVPocketHandler, token=config.token, consumer_key=config.consumer_key
    )
    storage_handler = providers.Factory(
        PCloudHandler,
        username=config.pc_username,
        password=config.pc_password,
        save_dir=config.save_dir,
    )
    image_downloader = providers.Factory(
        FDVImageDownloader,
        bookmark_handler=bookmark_handler,
        storage_handler=storage_handler,
        output_dir=config.output_dir,
    )


class BooruContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(
        BooruPocketHandler, token=config.token, consumer_key=config.consumer_key
    )
    storage_handler = providers.Factory(
        PCloudHandler,
        username=config.pc_username,
        password=config.pc_password,
        save_dir=config.save_dir,
    )
    image_downloader = providers.Factory(
        BooruImageDownloader,
        bookmark_handler=bookmark_handler,
        storage_handler=storage_handler,
        output_dir=config.output_dir,
    )


class KMNContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(
        KMNPocketHandler, token=config.token, consumer_key=config.consumer_key
    )
    storage_handler = providers.Factory(
        PCloudHandler,
        username=config.pc_username,
        password=config.pc_password,
        save_dir=config.save_dir,
    )
    image_downloader = providers.Factory(
        KMNImageDownloader,
        bookmark_handler=bookmark_handler,
        storage_handler=storage_handler,
        output_dir=config.output_dir,
    )
