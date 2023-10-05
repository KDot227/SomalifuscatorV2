import os
import sys
import time
from argparse import ArgumentParser

from util.supporting.settings import all_
from util.ui.ui import Ui, UiLinux
from util.obfuscation.obfuscate import Obfuscator
from util.auto_updating.updater import AutoUpdate

from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.syntax import Syntax
from rich.traceback import install

install()

__version__ = "2.2.0"


class Main:
    def __init__(self):
        if os.name == "nt":
            self.ui = Ui()
        else:
            self.ui = UiLinux()

    def measure_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print(f"It only took {end_time - start_time} to finish!")
        return wrapper

    def show_file_content(self, file_path):
        with open(file_path, encoding="utf8", errors="ignore") as f:
            syntax = Syntax(f.read(), "bat", line_numbers=True)
        print(Align.center(Panel.fit(syntax, title="Batch Content", border_style="bold blue", padding=(1, 2), subtitle=f"SomalifuscatorV{__version__}")))

    @measure_time
    def obfuscate_file(self, file_path):
        Obfuscator(file_path, double_click_check=all_.double_click_check, utf_16_bom=all_.utf_16_bom)

    def main(self, file_path=None):
        if file_path:
            if os.path.exists(file_path):
                self.obfuscate_file(file_path)
            else:
                print("File does not exist.")
            return

        AutoUpdate(__version__)
        self.ui.main_ui()
        Ui.pretty_print_settings()

        file_location = self.ui.get_user_file()
        if not os.path.exists(file_location):
            print("File does not exist.")
            return

        self.show_file_content(file_location)

        if all_.super_obf:
            print("This is only available in the paid version of Somalifuscator.")
            input("Press any key to exit...")
        else:
            self.obfuscate_file(file_location)
            input("Press any key to exit...")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="File to obfuscate", type=str)
    args = parser.parse_args()

    if args.file and not os.path.exists(args.file):
        print("File does not exist.")
        sys.exit(1)

    Main().main(file_path=args.file)
    sys.exit(0)
