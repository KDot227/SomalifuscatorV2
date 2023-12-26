from dataclasses import dataclass

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.widgets import Footer, Header, Button, Static, Placeholder, Pretty, RichLog
from textual.events import Print
from textual.reactive import Reactive
from textual.binding import Binding
from rich.syntax import Syntax
from textual import work


@dataclass
class settings:
    debug: bool = False


class Code_Console1(Static):
    code: str = Reactive("test")

    def compose(self) -> ComposeResult:
        yield RichLog(highlight=True, markup=True)


class Code_Console2(Static):
    def compose(self) -> ComposeResult:
        with open("C:\\Users\\this1\\Desktop\\Software\\SomalifuscatorV2\\tests\\test_1.bat", "r") as f:
            code = f.read()
        yield Static(
            Syntax(code, "bat", theme="monokai", line_numbers=True, word_wrap=True),
        )


class Obfuscator(Static):
    def compose(self) -> ComposeResult:
        yield Button("Obfuscate", id="start", variant="success")


class SomalifuscatorV2(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [Binding("d", "toggle_debug", "Toggle Debug")]

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            print("Obfuscating")
        else:
            print("Unknown button pressed!")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with Container(id="MainContainer"):
            yield Horizontal(
                ScrollableContainer(Code_Console1()),
                ScrollableContainer(Code_Console2()),
            )
            yield Obfuscator()

    def action_toggle_debug(self) -> None:
        settings.debug = not settings.debug
        print(f"Debug is now {settings.debug}")

    def on_print(self, event: Print) -> None:
        self.query_one(RichLog).write(event.text)

    def on_mount(self) -> None:
        self.run_my_worker()

    @work(thread=True)
    def run_my_worker(self):
        self.begin_capture_print(self, True, True)


if __name__ == "__main__":
    app = SomalifuscatorV2()
    app.run()
