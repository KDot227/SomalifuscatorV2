import os
import json
import logging
from pathlib import Path

from rich.logging import RichHandler

# Get the absolute path of the current file
current_file_path = Path(__file__).resolve()

# Set the path to the configuration file
working_dir = os.getcwd().replace("\\", "/")
conf_file = os.getcwd() + "/settings.json"

# If the configuration file does not exist, create it with default settings
if not os.path.exists(conf_file):
    with open("settings.json", "+w", encoding="utf8", errors="ignore") as f:
        f.write(
            """{
    "chinese": false,
    "hidden": false,
    "bloat": true,
    "remove_blank_lines": true,
    "super_obf": false,
    "FUD": false,
    "debug": false,
    "key": "NONE"
}"""
        )


class Settings:
    """
    A class for loading and accessing settings from a JSON configuration file.
    """

    def __init__(self, config_file=conf_file) -> None:
        """
        Initializes a new instance of the Settings class.

        :param config_file: The path to the configuration file.
        """
        self.json = json.load(open(config_file, "r"))

    def __getattr__(self, attr):
        """
        Gets the value of a setting by its name.

        :param attr: The name of the setting.
        :return: The value of the setting.
        """
        return self.get_key(attr)

    def get_key(self, key_name):
        """
        Gets the value of a setting by its name.

        :param key_name: The name of the setting.
        :return: The value of the setting.
        """
        return self.json[key_name]

    def load_all(self):
        """
        Loads all settings from the configuration file and sets them as attributes of the Settings object.
        """
        for key, value in self.json.items():
            setattr(self, key, value)


# Create a global instance of the Settings class and load all settings
all_ = Settings()
all_.load_all()

# Disable logging for requests and urllib3
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

# Configure logging using the Rich library
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    handlers=[
        RichHandler(show_time=False),
    ],
)

# Get the logger for the Rich library
log = logging.getLogger("rich")

# If debug mode is not enabled, set the logging level to INFO
if not all_.get_key("debug"):
    log.setLevel(logging.INFO)
    # log.info("logging level is INFO")
else:
    # If debug mode is enabled, create a log file and set the logging level to DEBUG
    try:
        os.remove("somalifuscatorv2.log")
    except FileNotFoundError:
        pass

    file_handler = logging.FileHandler("somalifuscatorv2.log")
    format2 = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(format2)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)
    # log.info("logging level is DEBUG")
