from dependency_injector import providers, containers
import sys
from containers import NitterContainer
from dotenv import load_dotenv

def main():
    image_downloader = container.image_downloader()
    image_downloader.run()


if __name__ == "__main__":
    load_dotenv()
    container = NitterContainer()
    container.config.token.from_env('POCKET_TOKEN')
    container.config.consumer_key.from_env('POCKET_CONSUMER_KEY')
    container.config.pc_username.from_env('PCLOUD_USERNAME')
    container.config.pc_password.from_env('PCLOUD_PASSWORD')
    container.config.from_dict(
        {"output_dir": './output'}
    )
    container.wire(modules=[sys.modules[__name__]])
    main()