import os
import json
import logging
from pathlib import Path

from dataclasses import dataclass

from util.supporting.logger import SomalifuscatorLogger

# Get the absolute path of the current file
current_file_path = Path(__file__).resolve()

# Set the path to the configuration file
working_dir = os.getcwd().replace("\\", "/")
conf_file = os.getcwd().replace("\\", "/") + "/settings.json"

# If the configuration file does not exist, create it with default settings
if not os.path.exists(conf_file):
    with open("settings.json", "+w", encoding="utf8", errors="ignore") as f:
        f.write(
            """{
    "bloat": true,
    "remove_blank_lines": true,
    "super_obf": false,
    "double_click_check": false,
    "utf_16_bom": true,
    "smartscreen_bypass": false,
    "hidden": false,
    "require_wifi": true,
    "FUD": true,
    "debug": false,
    "verbose": false
}"""
        )

json_set = json.load(open(conf_file, "r"))


@dataclass
class Settings:
    try:
        bloat: bool = json_set["bloat"]
        remove_blank_lines: bool = json_set["remove_blank_lines"]
        super_obf: bool = json_set["super_obf"]
        double_click_check: bool = json_set["double_click_check"]
        utf_16_bom: bool = json_set["utf_16_bom"]
        smartscreen_bypass: bool = json_set["smartscreen_bypass"]
        hidden: bool = json_set["hidden"]
        require_wifi: bool = json_set["require_wifi"]
        FUD: bool = json_set["FUD"]
        debug: bool = json_set["debug"]
        verbose: bool = json_set["verbose"]
    except KeyError:
        raise KeyError("The settings.json file is missing a required key.")


# Disable logging for requests and urllib3
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

# Configure logging using the Rich library
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    handlers=[SomalifuscatorLogger()],
)

# Get the logger for the Rich library
log = logging.getLogger("rich")

# If debug mode is not enabled, set the logging level to INFO
if not Settings.debug and not Settings.verbose:
    log.setLevel(logging.INFO)
    # log.info("logging level is INFO")
elif Settings.verbose and not Settings.debug:
    log.setLevel(logging.DEBUG)
    log.info("logging level is VERBOSE ONLY")
elif Settings.debug:
    try:
        os.remove("somalifuscatorv2.log")
    except FileNotFoundError:
        pass
    format2 = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler = logging.FileHandler("somalifuscatorv2.log")
    file_handler.setFormatter(format2)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)
    log.info("logging level is DEBUG")
else:
    print("logging level is NOTSET")
    log.setLevel(logging.NOTSET)
