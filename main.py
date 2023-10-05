import sys

import click
from dependency_injector import containers, providers
from dotenv import load_dotenv

from containers import NGKContainer, NitterContainer, FDVContainer, BooruContainer, KMNContainer


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
    container = NitterContainer()
    image_downloader = _get_wired_app(container, "/nittr")
    image_downloader.run()
    print("nitter")


@cli.command()
def ngk():
    container = NGKContainer()
    image_downloader = _get_wired_app(container, "/ngk")
    image_downloader.run()
    print("ngk")


@cli.command()
def fdv():
    container = FDVContainer()
    image_downloader = _get_wired_app(container, "/fdv")
    image_downloader.run()
    print("fdv")


@cli.command()
def booru():
    container = BooruContainer()
    image_downloader = _get_wired_app(container, "/booru")
    image_downloader.run()
    print("booru")


@cli.command()
def kmn():
    container = KMNContainer()
    image_downloader = _get_wired_app(container, "/kmn")
    image_downloader.run()
    print("kmn")


def main():
    cli()


if __name__ == "__main__":
    load_dotenv()
    main()
