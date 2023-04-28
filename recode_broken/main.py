import time, os, argparse, string

import kdot
import colorama

from tkinter import Tk
from tkinter import filedialog as kdot2

# hide the tkinter window
# I love stack overflow
root = Tk()
root.withdraw()


from ctypes import windll
from pystyle import *
from levels import level1, level2, level3, level4, level5
from levels.other.embed import embed
from levels.other.exe import exe2bat, bat2exe, bat2exe2
from levels.other.oneline import oneline
from levels.ultimate import ultimate
from levels.other import fud
from util.settings import *
from util.update import AutoUpdate
from util.menu import menu
from util.cesar import together

# fix colorama
colorama.deinit()

# fix dpi awareness or else the file picker looks terrible
windll.shcore.SetProcessDpiAwareness(1)

# proud author
__author__ = "K.Dot#4044 and Godfather"

kdot.check()

code = f"""@echo off
{together}
chcp 65001 > nul
"""


class main:
    def __init__(self, mode=None, file=None) -> None:
        if auto_update:
            AutoUpdate()
        self.Main(mode=mode, file=file)

    def Main(self, mode, file) -> None:
        menu(settings=settings2)

        try:
            if not os.path.exists(file):
                file = self.get_file()
                mode = self.get_mode()
        except:
            file = self.get_file()
            mode = self.get_mode()

        self.level = mode
        self.file = file
        self.down = False
        self.rep_num = 0
        self.level = self.level.lower()
        self.level_dict = {
            "1": level1.level1,
            "2": level2.level2,
            "3": level3.level3,
            "4": level4.level4,
            "5": level5.level5,
            "fud": fud.Fud,
            "ultimate": ultimate.Ultimate,
            "embed": embed,
            "exe": bat2exe.bat2exe,
            "exe2": bat2exe2.bat2exe2,
            # "oneline": oneline.o,
            "exe2bat": exe2bat.exe2bat,
        }
        pick = self.level_dict.get(self.level)
        if pick is not None:
            self.mixer()
            os.system("cls" if os.name == "nt" else "clear")
            pick(self.file, self.code_new)
            os._exit(0)
        else:
            print("Invalid mode!")
            time.sleep(3)
            os._exit(1)

    def mixer(self):
        original_file = self.file
        with open("mixer.bat", "w") as f:
            f.write(code)
        self.file = "mixer.bat"
        self.down = fud.Fud(file=self.file, down=self.down)
        with open("mixer.bat.fud.bat", "r", encoding="utf-8", errors="ignore") as f:
            self.code_new = f.read()
        os.remove("mixer.bat")
        os.remove("mixer.bat.fud.bat")
        self.file = original_file

    @staticmethod
    def get_file():
        file = ""

        while not os.path.exists(file):
            file = kdot2.askopenfilename(
                title="Select a file to obfuscate",
                filetypes=(("Batch files", "*.bat"), ("All files", "*.*")),
            )

        root.destroy()
        return file

    @staticmethod
    def get_mode():
        mode = ""
        modes = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "fud",
            "ultimate",
            "embed",
            "exe",
            "exe2",
            "oneline",
            "exe2bat",
        ]

        while not mode in modes:
            mode = Write.Input(
                "What level of Obfuscation do you want? -> ",
                Colors.green,
                interval=0.05,
            )
        return mode


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("-f", "--file", help="Auto update")
    argparse.add_argument("-m", "--mode", help="Mode")
    args = argparse.parse_args()
    if auto_update:
        AutoUpdate()
    main(args.mode, args.file)
    print("Done!")
    time.sleep(3)
    os._exit(0)
