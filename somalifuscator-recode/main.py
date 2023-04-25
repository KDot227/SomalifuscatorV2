import time, os, tkinter, random, string

import kdot
import colorama


#from ctypes import windll
from levels import level1, level2, level3, level4, level5
from levels.other import fud
from util.settings import *
from util.update import AutoUpdate
from util.menu import menu
from util.cesar import together

# fix colorama
colorama.deinit()

# fix dpi awareness or else the file picker looks terrible
#windll.shcore.SetProcessDpiAwareness(1)

# proud author
__author__ = "K.Dot#4044 and Godfather"

kdot.check()

code = f"""@echo off
{together}
chcp 65001 > nul
"""

class main:
    def __init__(self, mode=None, file=None) -> None:
        #AutoUpdate()
        self.Main(mode, file)

    def Main(self, mode, file) -> None:
        menu(settings=settings2)

        self.level = mode
        self.file = file
        self.down = False
        self.rep_num = 0
        self.level = self.level.lower()
        #self.level_dict = {
        #    "1": self.Level1,
        #    "2": self.level2,
        #    "3": self.level3,
        #    "4": self.level4,
        #    "5": self.level5,
        #    "clean": self.clean,
        #    "all": self.all,
        #    "fud": self.fud,
        #    "ultimate": self.ultimate,
        #    "embed": self.embed,
        #    "exe": self.bat2exe,
        #    "exe2": self.bat2exe2,
        #    "oneline": self.oneline,
        #    "exe2bat": self.exe2bat,
        #    "py2bat": self.py2bat,
        #}
        self.level_dict = {
            "1": level1.level1,
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

if __name__ == "__main__":
    main("1", "test.bat")