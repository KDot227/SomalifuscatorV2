import os
import json
from dataclasses import dataclass

from util.auto_updating.updater import AutoUpdate

from util.obfuscation.obfuscate import Obfuscator as OBF

from util.supporting.settings import conf_file, Settings

try:
    from tkinter import Tk
    from tkinter import filedialog as fd
except:
    pass

from argparse import ArgumentParser

from textual.app import App, ComposeResult
from textual.containers import Horizontal, ScrollableContainer, Center
from textual.widgets import Footer, Header, Button, Static, RichLog
from textual.events import Print
from textual.binding import Binding
from textual import work
from rich.syntax import Syntax
from rich.text import Text

__version__ = "2.10.2"


@dataclass
class settings:
    file: str = ""


class Code_Display(ScrollableContainer):
    def compose(self) -> ComposeResult:
        settings.file = SomalifuscatorV2.get_user_file()
        with open(settings.file, "r") as f:
            code = f.read()
        yield Static(
            Syntax(
                code,
                "bat",
                theme="monokai",
                line_numbers=True,
                word_wrap=True,
            )
        )


class SomalifuscatorV2(App):
    CSS_PATH = "util\\ui\\style.tcss"
    BINDINGS = [
        Binding("d", "toggle_debug", "Toggle Debug"),
        Binding("q", "quit", "Quit"),
    ]

    def on_button_pressed(self, _: Button.Pressed) -> None:
        OBF(
            settings.file,
            double_click_check=Settings.double_click_check,
            utf_16_bom=Settings.utf_16_bom,
        )
        self.query_one(RichLog).write("Obfuscating...")

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield RichLog()
            yield Code_Display()
        with Center():
            yield Button("Obfuscate", variant="success")
        yield Footer()

    def action_toggle_debug(self) -> None:
        Settings.debug = not Settings.debug
        color = "red" if not Settings.debug else "green"
        debug_msg = Text.from_markup(
            f"Debug is now [{color} italic]{Settings.debug}[/]"
        )
        self.query_one(RichLog).write(debug_msg)

    def action_quit(self) -> None:
        self.exit()

    def on_print(self, event: Print) -> None:
        self.query_one(RichLog).write(Text.from_markup(event.text.strip()))
        # ill fix this soon
        # with open("test.txt", "a+") as f:
        #    f.write(str(Text.from_markup(event.text)))

    @work(thread=True)
    def run_my_worker(self):
        self.begin_capture_print(self, True, True)

    def on_mount(self) -> None:
        self.query_one(RichLog).border_title = "Log"
        self.query_one(Code_Display).border_title = "Code"

        self.query_one(RichLog).write(Text.from_markup(self.pretty_print_settings()))

        self.query_one(Button).focus()
        self.run_my_worker()

    @staticmethod
    def pretty_print_settings() -> str:
        with open(conf_file, "r") as f:
            settings = json.load(f)
        # print(Align.center(f"[cyan]Settings: {conf_file}[/cyan]"))
        # print(
        #    Align.center(
        #        f"[bold white]{'-' * (14 + len(conf_file.strip()))}[/bold white]"
        #    )
        # )
        # for key, value in settings.items():
        #    print(Align.center(f"[bold white]{key}: [/bold white]{value}"))
        to_print = ""
        to_print += f"[bold blue]Settings:[/] [bold white]{conf_file}[/]\n"
        for key, value in settings.items():
            color = "green" if value else "red"
            to_print += f"[bold blue]{key}:[/] [bold {color}]{value}[/]\n"
        return to_print

    @staticmethod
    def get_user_file() -> str:
        """
        Prompts the user to select a batch file.
        Returns the file path of the selected file.

        Returns:
        - str: The file path of the selected file.
        """
        file_path = ""
        # keep prompting user until they select a valid file
        root = Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)
        while not os.path.isfile(file_path):
            # make sure file is bat file
            file_path = fd.askopenfilename(
                title="Select a batch file",
                filetypes=[("Batch Files", ("*.bat", "*.cmd"))],
                initialdir=os.getcwd(),
                parent=root,
            )
        root.destroy()
        return file_path


if __name__ == "__main__":
    parse = ArgumentParser()
    parse.add_argument("-f", "--file", help="File to obfuscate", type=str)
    parse.add_argument(
        "-nu", "--no-utf-16-bom", help="No UTF-16 BOM", action="store_true"
    )
    args = parse.parse_args()
    if any([args.file]):
        Settings.utf_16_bom = False
        Settings.double_click_check = False
        OBF(
            args.file,
            double_click_check=Settings.double_click_check,
            utf_16_bom=Settings.utf_16_bom,
        )
        exit(0)
    AutoUpdate(__version__)
    SomalifuscatorV2().run()
    exit(0)
