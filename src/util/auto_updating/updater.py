import time
import requests
import webbrowser

__version__ = "1.0.0"


class AutoUpdate:
    # There is no actual auto updating :skull:
    def __init__(self) -> None:
        self.check_for_updates()

    def check_for_updates(self) -> None:
        self.url = "https://raw.githubusercontent.com/KDot227/SomalifuscatorV2/main/src/main.py"
        main_code = requests.get(self.url).text
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
            else:
                print("you are on the newest verison!")
