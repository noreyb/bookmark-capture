# Dependency_injectorのContainerをusecase毎に作成する
from dependency_injector import containers, providers
from repository.pocket import PocketHandler
from repository.pcloud import PCloudHandler
from usecase.nitter_image_downloader import NitterImageDownloader
from usecase.interface.image_downloader import IImageDownloader
from repository.interface.bookmark import IBookmarkHandler
from repository.interface.storage import IStorageHandler

class NitterContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(PocketHandler, token=config.token, consumer_key=config.consumer_key)
    storage_handler = providers.Factory(PCloudHandler, username=config.pc_username, password=config.pc_password)
    image_downloader = providers.Factory(NitterImageDownloader, bookmark_handler=bookmark_handler, storage_handler=storage_handler, output_dir=config.output_dir)

# future work
"""
class BooruContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(PocketHandler, token=config.token, consumer_key=config.consumer_key)
    storage_handler = providers.Factory(PCloudHandler, username=config.pc_username, password=config.pc_password)
    image_downloader = providers.Factory(BooruImageDownloader, bookmark_handler=bookmark_handler, storage_handler=storage_handler, output_dir=config.output_dir)

class KemonoContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    bookmark_handler = providers.Factory(PocketHandler, token=config.token, consumer_key=config.consumer_key)
    storage_handler = providers.Factory(PCloudHandler, username=config.pc_username, password=config.pc_password)
    image_downloader = providers.Factory(KemonoImageDownloader, bookmark_handler=bookmark_handler, storage_handler=storage_handler, output_dir=config.output_dir)
"""