import sys
import time
import requests
import webbrowser


class AutoUpdate:
    # There is no actual auto updating :skull:
    def __init__(self, __version__) -> None:
        self.check_for_updates(__version__)

    def check_for_updates(self, __version__) -> None:
        self.url = "https://raw.githubusercontent.com/KDot227/SomalifuscatorV2/main/src/main.py"
        try:
            main_code = requests.get(self.url)
        except:
            return
        main_code = main_code.text
        version_string = "__version__ = "
        version = main_code.split(version_string)[1].split('"')[1]
        if version != __version__:
            print(f"New version available: {version}")
            print("Please go to the github page to download the new version.")
            to_take = input("Would you like me to take you there? (y/n): ")
            if to_take.lower() == "y":
                print("Taking you there...")
                time.sleep(1)
                webbrowser.open("https://github.com/KDot227/SomalifuscatorV2")
                sys.exit(0)
