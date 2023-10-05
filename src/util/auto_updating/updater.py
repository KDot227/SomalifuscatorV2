import sys
import time
import requests
import webbrowser

class AutoUpdate:
    def __init__(self, current_version: str, update_url: str, github_url: str) -> None:
        self.current_version = current_version
        self.update_url = update_url
        self.github_url = github_url

    def fetch_latest_code(self) -> str:
        try:
            response = requests.get(self.update_url)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            print("Failed to fetch the latest code. Please check your internet connection.")
            return None

    def extract_version(self, code: str) -> str:
        version_string = "__version__ = "
        try:
            version = code.split(version_string)[1].split('"')[1]
            return version
        except IndexError:
            print("Failed to extract version from the fetched code.")
            return None

    def prompt_for_update(self, new_version: str) -> None:
        print(f"New version available: {new_version}")
        print("Please go to the GitHub page to download the new version.")
        to_take = input("Would you like me to take you there? (y/n): ")
        if to_take.lower() == "y":
            print("Taking you there...")
            time.sleep(1)
            webbrowser.open(self.github_url)
            sys.exit(0)

    def check_for_updates(self) -> None:
        latest_code = self.fetch_latest_code()
        if not latest_code:
            return
        
        new_version = self.extract_version(latest_code)
        if not new_version:
            return

        if new_version != self.current_version:
            self.prompt_for_update(new_version)

if __name__ == "__main__":
#   CURRENT_VERSION = "2.4.0"
#   UPDATE_URL = "https://raw.githubusercontent.com/KDot227/SomalifuscatorV2/main/src/main.py"
#   GITHUB_URL = "https://github.com/KDot227/SomalifuscatorV2"

#   auto_updater = AutoUpdate(CURRENT_VERSION, UPDATE_URL, GITHUB_URL)
#   auto_updater.check_for_updates()
