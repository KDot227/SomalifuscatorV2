import random
import logging


class SomalifuscatorLogger(logging.StreamHandler):
    """Custom Logger because rich logger does too much smh"""

    def emit(self, record):
        try:
            msg = self.format(record)
            print(f"[bold {self.get_random_color()}]{msg}[/]\n")
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def get_random_color(self) -> str:
        return random.choice(["blue", "white"])
