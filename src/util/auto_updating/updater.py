import sys
import time
import requests

__version__ = "1.0.0"


class AutoUpdate:
    def __init__(self) -> None:
        self.check_for_updates()

    def check_for_updates(self) -> None:
        self.url = "https://raw.githubusercontent.com/KDot227/SomalifuscatorV2/main/src/main.py"
        main_code = requests.get(self.url).text
        if main_code.split("\n")[0].split(" ")[2].replace('"', "") != __version__:
            print("Update available!\nDownload it in the github!")
            time.sleep(3)
            sys.exit(1)
