import os

import click
from injector import Injector

from containers import BooruFactory, FDVFactory, KMNFactory, NGKFactory, TwitterFactory
from usecase.interface.image_downloader import IImageDownloader

# from dependency_injector import containers, providers
# from dotenv import load_dotenv


def _get_wired_app(container, save_dir: str):
    container.config.token.from_env("POCKET_TOKEN")
    container.config.consumer_key.from_env("POCKET_CONSUMER_KEY")
    container.config.pc_username.from_env("PCLOUD_USERNAME")
    container.config.pc_password.from_env("PCLOUD_PASSWORD")
    container.config.from_dict(
        {
            "output_dir": "./output",
            "save_dir": save_dir,
        }
    )
    container.wire(modules=[sys.modules[__name__]])
    image_downloader = container.image_downloader()
    return container.image_downloader()


@click.group()
def cli():
    print("cli")


@cli.command()
def nitter():
    factory = TwitterFactory(
        token=os.getenv("POCKET_TOKEN"),
        consumer_key=os.getenv("POCKET_CONSUMER_KEY"),
        pc_username=os.getenv("PCLOUD_USERNAME"),
        pc_password=os.getenv("PCLOUD_PASSWOTRD"),
        save_dir="/nittr",
        output_dir="./output",
    )
    injector = Injector(factory.configure)
    image_downloader = injector.get(IImageDownloader)
    image_downloader.run()


@cli.command()
def ngk():
    factory = NGKFactory(
        token=os.getenv("POCKET_TOKEN"),
        consumer_key=os.getenv("POCKET_CONSUMER_KEY"),
        pc_username=os.getenv("PCLOUD_USERNAME"),
        pc_password=os.getenv("PCLOUD_PASSWOTRD"),
        save_dir="/ngk",
        output_dir="./output",
    )
    injector = Injector(factory.configure)
    image_downloader = injector.get(IImageDownloader)
    image_downloader.run()


@cli.command()
def fdv():
    factory = FDVFactory(
        token=os.getenv("POCKET_TOKEN"),
        consumer_key=os.getenv("POCKET_CONSUMER_KEY"),
        pc_username=os.getenv("PCLOUD_USERNAME"),
        pc_password=os.getenv("PCLOUD_PASSWOTRD"),
        save_dir="/fdv",
        output_dir="./output",
    )
    injector = Injector(factory.configure)
    image_downloader = injector.get(IImageDownloader)
    image_downloader.run()


@cli.command()
def booru():
    factory = BooruFactory(
        token=os.getenv("POCKET_TOKEN"),
        consumer_key=os.getenv("POCKET_CONSUMER_KEY"),
        pc_username=os.getenv("PCLOUD_USERNAME"),
        pc_password=os.getenv("PCLOUD_PASSWOTRD"),
        save_dir="/booru",
        output_dir="./output",
    )
    injector = Injector(factory.configure)
    image_downloader = injector.get(IImageDownloader)
    image_downloader.run()


@cli.command()
def kmn():
    factory = KMNFactory(
        token=os.getenv("POCKET_TOKEN"),
        consumer_key=os.getenv("POCKET_CONSUMER_KEY"),
        pc_username=os.getenv("PCLOUD_USERNAME"),
        pc_password=os.getenv("PCLOUD_PASSWOTRD"),
        save_dir="/kmn",
        output_dir="./output",
    )
    injector = Injector(factory.configure)
    image_downloader = injector.get(IImageDownloader)
    image_downloader.run()


def main():
    cli()


if __name__ == "__main__":
    # load_dotenv()
    main()
