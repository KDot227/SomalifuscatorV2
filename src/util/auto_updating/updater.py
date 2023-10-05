import sys
import time
import requests
import webbrowser
import os
import zipfile
import tarfile
import platform
import shutil
from typing import Optional

class AutoUpdate:
    def __init__(self, current_version: str, update_url: str, github_url: str, zip_url: str, tar_url: str) -> None:
        self.current_version = current_version
        self.update_url = update_url
        self.github_url = github_url
        self.zip_url = zip_url
        self.tar_url = tar_url

    def fetch_latest_code(self) -> Optional[str]:
        try:
            response = requests.get(self.update_url)
            response.raise_for_status()
            if "__version__" not in response.text:
                print("Invalid update source: missing version information.")
                return None
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch the latest code: {e}")
            return None

    def extract_version(self, code: str) -> Optional[str]:
        version_string = "__version__ = "
        try:
            version = code.split(version_string)[1].split('"')[1]
            return version
        except IndexError:
            print("Failed to extract version from the fetched code.")
            return None

    def download_and_extract(self) -> None:
        archive_path = 'update_archive'
        if platform.system() == 'Windows':
            archive_path += '.zip'
            download_url = self.zip_url
        else:
            archive_path += '.tar.gz'
            download_url = self.tar_url

        try:
            response = requests.get(download_url)
            response.raise_for_status()
            with open(archive_path, 'wb') as f:
                f.write(response.content)

            if platform.system() == 'Windows':
                with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                    zip_ref.extractall('.')
            else:
                with tarfile.open(archive_path, 'r:gz') as tar_ref:
                    tar_ref.extractall('.')
            
            os.remove(archive_path)

            if not any(os.path.isfile(os.path.join(root, 'LICENSE')) for root, _, files in os.walk('.')):
                print("Update failed: Files not properly extracted.")
                return

        except (requests.RequestException, zipfile.BadZipFile, tarfile.ReadError) as e:
            print(f"Failed to download or extract the update archive: {e}")

    def prompt_for_update(self, new_version: str) -> None:
        print(f"New version available: {new_version}")
        print("Please go to the GitHub page to download the new version.")
        
        while True:
            choice = input("Would you like me to take you there or download it for you? (y/n/download): ").lower()
            if choice in ['y', 'n', 'download']:
                break
            print("Invalid option. Please enter y, n, or download.")

        if choice == 'y':
            webbrowser.open(self.github_url)
            sys.exit(0)
        elif choice == 'download':
            self.download_and_extract()
            print("Update complete. Please restart the application.")
            sys.exit(0)

    def check_for_updates(self) -> None:
        latest_code = self.fetch_latest_code()
        if latest_code is None:
            return
        
        new_version = self.extract_version(latest_code)
        if new_version is None:
            return

        if new_version != self.current_version:
            self.prompt_for_update(new_version)

if __name__ == "__main__":
    # change these variables so the main script provides them :>
    CURRENT_VERSION = "1.0.0"
    UPDATE_URL = "https://raw.githubusercontent.com/KDot227/SomalifuscatorV2/main/src/main.py"
    GITHUB_URL = "https://github.com/KDot227/SomalifuscatorV2"
    ZIP_URL = "https://github.com/KDot227/SomalifuscatorV2/archive/refs/tags/Bat2Exe_Method1.zip"
    TAR_URL = "https://github.com/KDot227/SomalifuscatorV2/archive/refs/tags/Bat2Exe_Method1.tar.gz"

    # this is just so uk how run it :>
    auto_updater = AutoUpdate(CURRENT_VERSION, UPDATE_URL, GITHUB_URL, ZIP_URL, TAR_URL)
    auto_updater.check_for_updates()
