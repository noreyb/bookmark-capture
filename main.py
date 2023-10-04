from dependency_injector import providers, containers
import sys
from containers import NitterContainer

def main():
    image_downloader = container.image_downloader()
    image_downloader.run()


if __name__ == "__main__":
    container = NitterContainer()
    container.config.token.from_env('POCKET_TOKEN')
    container.config.consumer_key.from_env('POCKET_CONSUMER_KEY')
    container.config.pc_username.from_env('PCLOUD_USERNAME')
    container.config.pc_password.from_env('PCLOUD_PASSWORD')
    
    # from_dict を使うと、configの値をdictで渡せる
    container.config.from_dict(
        {"output_dir": './output'}
    )
    container.wire(modules=[sys.modules[__name__]])
    main()