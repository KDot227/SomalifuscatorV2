import os
import sys
import time
import cProfile

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

from argparse import ArgumentParser


__version__ = "2.6.0"


class Main:
    def main(self):
        super_obf = all_.super_obf
        if any([args.file]):
            current_time = time.time()
            Obfuscator(args.file, double_click_check=False, utf_16_bom=False)
            finish_time = time.time()
            print(f"It only took {finish_time - current_time} to finish!")
            return

        AutoUpdate(__version__)

        # initialize UI
        if os.name == "nt":
            self.ui = Ui()
        else:
            self.ui = UiLinux()

        # show main ui
        self.ui.main_ui()

        # hot asf settings
        Ui.pretty_print_settings()

        # get file location
        file_location = self.ui.get_user_file()

        current_time = time.time()

        # show inside of file (aesthetic trust)
        with open(file_location, encoding="utf8", errors="ignore") as f:
            syntax = Syntax(f.read(), "bat", line_numbers=True)
        print(Align.center(Panel.fit(syntax, title="Batch Content", border_style="bold blue", padding=(1, 2), subtitle=f"SomalifuscatorV{__version__}")))
        if super_obf:
            print("This is only available in the paid version of Somalifuscator.")
            input("Press any key to exit...")
        else:
            Obfuscator(file_location, double_click_check=all_.double_click_check, utf_16_bom=all_.utf_16_bom)
            finish_time = time.time()
            print(f"It only took {finish_time - current_time} to finish!")
            input("Press any key to exit...")


TIME_CHECK = False

if TIME_CHECK:
    parse = ArgumentParser()
    parse.add_argument("-f", "--file", help="File to obfuscate", type=str)
    parse.add_argument("-nu", "--no-utf-16-bom", help="No UTF-16 BOM", action="store_true")
    args = parse.parse_args()
    # profile the Main().main() function and show what functions took the longest to execute and write the info to a file
    with cProfile.Profile() as pr:
        Main().main()
    pr.print_stats(sort="cumtime")
    with open("profile.txt", "w") as f:
        sys.stdout = f
        pr.print_stats(sort="time")
    sys.exit(0)

if __name__ == "__main__":
    parse = ArgumentParser()
    parse.add_argument("-f", "--file", help="File to obfuscate", type=str)
    parse.add_argument("-nu", "--no-utf-16-bom", help="No UTF-16 BOM", action="store_true")
    args = parse.parse_args()
    Main().main()

# import os
# import sys
# import time
# import json
# from dataclasses import dataclass
#
# from util.methods.common.common import console
#
# from util.supporting.settings import conf_file
#
# try:
#    from tkinter import Tk
#    from tkinter import filedialog as fd
# except:
#    pass
#
# from rich.align import Align
#
# from textual.app import App, ComposeResult
# from textual.containers import Container, Horizontal, ScrollableContainer
# from textual.widgets import Footer, Header, Button, Static, Placeholder, Pretty, RichLog
# from textual.events import Print
# from textual.reactive import Reactive
# from textual.binding import Binding
# from rich.syntax import Syntax
# from textual import work, events
#
#
# @dataclass
# class settings:
#    file: str = ""
#    debug: bool = False
#
#
# class Code_Console1(Static):
#    code: str = Reactive("test")
#
#    def compose(self) -> ComposeResult:
#        yield RichLog(highlight=True, markup=True)
#
#
# class Code_Console2(Static):
#    def compose(self) -> ComposeResult:
#        settings.file = SomalifuscatorV2.get_user_file()
#        with open(settings.file, "r") as f:
#            code = f.read()
#        yield Static(
#            Syntax(code, "bat", theme="monokai", line_numbers=True, word_wrap=True),
#        )
#
#
# class Obfuscator(Static):
#    def compose(self) -> ComposeResult:
#        yield Button("Obfuscate", id="start", variant="success")
#
#
# class SomalifuscatorV2(App):
#    CSS_PATH = "util\\ui\\style.tcss"
#    BINDINGS = [Binding("d", "toggle_debug", "Toggle Debug")]
#
#    def on_button_pressed(self, event: Button.Pressed) -> None:
#        if event.button.id == "start":
#            OBF(settings.file, double_click_check=all_.double_click_check, utf_16_bom=all_.utf_16_bom)
#        else:
#            print("Unknown button pressed!")
#
#    def compose(self) -> ComposeResult:
#        yield Header()
#        yield Footer()
#        with Container(id="MainContainer"):
#            yield Horizontal(
#                ScrollableContainer(Code_Console1()),
#                ScrollableContainer(Code_Console2()),
#            )
#            yield Obfuscator()
#
#    def action_toggle_debug(self) -> None:
#        settings.debug = not settings.debug
#        print(f"Debug is now {settings.debug}")
#
#    def on_print(self, event: Print) -> None:
#        # check if any text in events.text is not in string.printable
#        # if so, then it's probably a key event
#        self.query_one(RichLog).write(event.text)
#
#    def on_mount(self) -> None:
#        self.run_my_worker()
#
#    @work(thread=True)
#    def run_my_worker(self):
#        self.begin_capture_print(self, True, True)
#
#    @staticmethod
#    def pretty_print_settings() -> None:
#        with open(conf_file, "r") as f:
#            settings = json.load(f)
#        print(Align.center(f"[cyan]Settings: {conf_file}[/cyan]"))
#        print(Align.center(f"[bold white]{'-' * (14 + len(conf_file.strip()))}[/bold white]"))
#        for key, value in settings.items():
#            print(Align.center(f"[bold white]{key}: [/bold white]{value}"))
#
#    @staticmethod
#    def get_user_file() -> str:
#        """
#        Prompts the user to select a batch file.
#        Returns the file path of the selected file.
#
#        Returns:
#        - str: The file path of the selected file.
#        """
#        file_path = ""
#        # keep prompting user until they select a valid file
#        root = Tk()
#        root.withdraw()
#        root.wm_attributes("-topmost", 1)
#        while not os.path.isfile(file_path):
#            # make sure file is bat file
#            file_path = fd.askopenfilename(
#                title="Select a batch file",
#                filetypes=[("Batch Files", ("*.bat", "*.cmd"))],
#                initialdir=os.getcwd(),
#                parent=root,
#            )
#        root.destroy()
#        return file_path
