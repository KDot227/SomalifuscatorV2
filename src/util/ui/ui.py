import os
import sys
import time
import json

from util.methods.common.common import console

from util.supporting.settings import conf_file

try:
    from tkinter import Tk
    from tkinter import filedialog as fd
except:
    pass

from rich import print
from rich.align import Align

banner = """
███████╗ ██████╗ ███╗   ███╗ █████╗ ██╗     ██╗███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██║██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║   ██║██╔████╔██║███████║██║     ██║█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║   ██║██║╚██╔╝██║██╔══██║██║     ██║██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 Made by Godfather and K.Dot227\n\n
 
 
"""


class Ui:
    def __init__(self) -> None:
        """
        Initializes the Ui class.
        """
        pass

    @staticmethod
    def slow_print_input(text: str) -> str:
        """
        Prints the given text character by character with a delay of 0.1 seconds between each character.
        Returns the user's input.

        Args:
        - text (str): The text to be printed.

        Returns:
        - str: The user's input.
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        return input()

    @staticmethod
    def clear() -> None:
        """
        Clears the console screen.
        """
        os.system("cls")

    @staticmethod
    def pretty_print_settings() -> None:
        with open(conf_file, "r") as f:
            settings = json.load(f)
        print(Align.center(f"[cyan]Settings: {conf_file}[/cyan]"))
        print(Align.center(f"[bold white]{'-' * (14 + len(conf_file.strip()))}[/bold white]"))
        for key, value in settings.items():
            print(Align.center(f"[bold white]{key}: [/bold white]{value}"))

    def main_ui(self) -> None:
        """
        Displays the main user interface.
        """
        self.clear()
        for line in banner.split("\n"):
            console.print(Align.center(line), style=f"bold blue")

    def get_user_file(self) -> str:
        """
        Prompts the user to select a batch file.
        Returns the file path of the selected file.

        Returns:
        - str: The file path of the selected file.
        """
        self.file_path = ""
        # keep prompting user until they select a valid file
        root = Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)
        while not os.path.isfile(self.file_path):
            # make sure file is bat file
            self.file_path = fd.askopenfilename(
                title="Select a batch file",
                filetypes=[("Batch Files", ("*.bat", "*.cmd"))],
                initialdir=os.getcwd(),
                parent=root,
            )
        root.destroy()
        return self.file_path

    def show_file_insides(self, file_path: str) -> None:
        """
        Displays the contents of the given file.

        Args:
        - file_path (str): The file path of the file to be displayed.
        """
        with open(file_path, "r") as file:
            print(file.read())


class UiLinux:
    def __init__(self) -> None:
        pass

    @staticmethod
    def slow_print_input(text: str) -> str:
        """
        Prints the given text character by character with a delay of 0.1 seconds between each character.
        Returns the user's input.

        Args:
        - text (str): The text to be printed.

        Returns:
        - str: The user's input.
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        return input()

    @staticmethod
    def clear() -> None:
        """
        Clears the console screen.
        """
        os.system("clear")

    def main_ui(self) -> None:
        """
        Displays the main user interface.
        """
        self.clear()
        for line in banner.split("\n"):
            console.print(Align.center(line), style=f"bold blue")

    def get_user_file(self) -> str:
        """
        Prompts the user to select a batch file.
        Returns the file path of the selected file.

        Returns:
        - str: The file path of the selected file.
        """
        self.file_path = input("Enter the path to the batch file: ")

        return self.file_path

    def show_file_insides(self, file_path: str) -> None:
        """
        Displays the contents of the given file.

        Args:
        - file_path (str): The file path of the file to be displayed.
        """
        with open(file_path, "r") as file:
            print(file.read())
