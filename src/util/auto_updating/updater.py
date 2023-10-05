import sys
import time
import requests
import webbrowser
import os
import zipfile
import tarfile
import platform
import shutil

class AutoUpdate:
    def __init__(self, current_version: str, update_url: str, github_url: str, zip_url: str, tar_url: str) -> None:
        self.current_version = current_version
        self.update_url = update_url
        self.github_url = github_url
        self.zip_url = zip_url
        self.tar_url = tar_url
        self.license = os.path.join(os.getcwd(), 'LICENSE')

    def fetch_latest_code(self) -> str:
        try:
            response = requests.get(self.update_url)
            response.raise_for_status()
            if "__version__" not in response.text:  # Edge Case 1
                print("Invalid update source: missing version information.")
                return None
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

    def download_and_extract(self):
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
            with open(archive_path, 'wb') as f:  # Logic Error Fix
                f.write(response.content)

            if platform.system() == 'Windows':
                try:
                    with zipfile.ZipFile(archive_path, 'r') as zip_ref:  # Edge Case 2
                        zip_ref.extractall('.')
                except zipfile.BadZipFile:
                    print("Corrupted ZIP archive. Update failed.")
                    return
            else:
                try:
                    with tarfile.open(archive_path, 'r:gz') as tar_ref:  # Edge Case 2
                        tar_ref.extractall('.')
                except tarfile.ReadError:
                    print("Corrupted TAR.GZ archive. Update failed.")
                    return

            os.remove(archive_path)

            # Edge Case 3
            if not os.path.exists(self.license):
                print("Update failed: Files not properly extracted.")
                return

        except requests.RequestException:
            print("Failed to download the update archive.")
            return

    def prompt_for_update(self, new_version: str) -> None:
        print(f"New version available: {new_version}")
        print("Please go to the GitHub page to download the new version.")
        
        # Edge Case 4
        while True:
            choice = input("Would you like me to take you there or download it for you? (y/n/download): ").lower()
            if choice in ['y', 'n', 'download']:
                break
            print("Invalid option. Please enter y, n, or download.")

        if choice == 'y':
            print("Taking you there...")
            time.sleep(1)
            webbrowser.open(self.github_url)
            sys.exit(0)
        elif choice == 'download':
            print("Downloading and extracting the new version...")
            self.download_and_extract()
            print("Update complete. Please restart the application.")
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
    # change these variables so the main script provides them :>
    CURRENT_VERSION = "1.0.0"
    UPDATE_URL = "https://raw.githubusercontent.com/KDot227/SomalifuscatorV2/main/src/main.py"
    GITHUB_URL = "https://github.com/KDot227/SomalifuscatorV2"
    ZIP_URL = "https://github.com/KDot227/SomalifuscatorV2/archive/refs/tags/Bat2Exe_Method1.zip"
    TAR_URL = "https://github.com/KDot227/SomalifuscatorV2/archive/refs/tags/Bat2Exe_Method1.tar.gz"

    # this is just so uk how run it :>
    auto_updater = AutoUpdate(CURRENT_VERSION, UPDATE_URL, GITHUB_URL, ZIP_URL, TAR_URL)
    auto_updater.check_for_updates()
