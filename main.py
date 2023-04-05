# Documentation = in hell
# Also don't ask me how the regex works cause idk either

import os
import time
import json
import threading
from tkinter import Tk
from tkinter import filedialog as kdot2

# hide the tkinter window
# I love stack overflow
root = Tk()
root.withdraw()

root.overrideredirect(True)
root.geometry("0x0+0+0")

root.deiconify()
root.lift()
root.focus_force()

current_dir = os.path.dirname(os.path.realpath(__file__))
settings_path = current_dir + "/settings.json"

with open(settings_path, "r") as f:
    settings = json.load(f)

try:
    chinese = settings["chinese"]
    pogdog_fun = settings["pogdog"]
    hell = settings["hell"]
    eicar = settings["eicar"]
    unicode = settings["unicode"]
    utf_16_bom = settings["utf_16_bom"]
    music = settings["music"]
    ads = settings["ads"]
    random_spacing = settings["random_spacing"]
    auto_update = settings["auto_update"]
    echo_weird = settings["echo_weird"]
    anti_vm = settings["anti_vm"]
    for_loop = settings["for_loop"]
    scramble_labels = settings["scramble_labels"]
except:
    print(
        "Your settings.json file has been update! Please redownload somalifuscator and try again"
    )
    time.sleep(30)
    os._exit(1)

global debug
debug = False

if debug:
    print("For best debugging experiences, turn off all settings")
    time.sleep(3)

try:
    from rich.progress import Progress, track
    from zipfile import ZipFile
    from random import randint
    from ctypes import windll
    from pygame import mixer
    from pystyle import *
    import subprocess
    import colorama
    import requests
    import random
    import string
    import re
except Exception as e:
    print(
        e
        + "\nYou don't have the required modules installed. Please run the setup.bat file to fix this. If that doesn't work that means the requirements were updated. If this is the case please redownload the setup.bat from the github"
    )
    time.sleep(5)
    os._exit(1)

# fix colorama
colorama.deinit()

# fix dpi awareness or else the file picker looks terrible
windll.shcore.SetProcessDpiAwareness(1)

# proud author
__author__ = "K.Dot#4044 and Godfather"

cesar_val = randint(1, 13)


def Music():
    """Plays music in the background."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    song_dir = current_dir + "/assets/music/"
    random_song = random.choice(os.listdir(song_dir))

    song = song_dir + random_song

    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    while mixer.music.get_busy():
        pass


def caesar_cipher_rotations(rotation):
    """Generates the Caesar cipher for a given rotation value."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


def caesar_cipher_rotations_upper(rotation):
    """Generates the Caesar cipher for a given rotation value. (CAPITAL LETTERS ONLY)"""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}1={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(cesar_val)
together = together[:-4]


# average W batch thing where u get a error every line

if chinese:
    chinese_characters = "苑范腕勝滕贖值債價償責直真賭哀衰衷袁忠棄業停亨享亭亮閏闊閒闌聞門閂閃閉開閑間閘閡閣閥閨閩閱閹閻闃闔闕闖關闡募幕慕壞壤讓鑲"
else:
    chinese_characters = string.ascii_letters + string.digits

code = f"""@echo off
{together}
chcp 65001 > nul
"""
if (
    __author__
    != "\x4b\x2e\x44\x6f\x74\x23\x34\x30\x34\x34\x20\x61\x6e\x64\x20\x47\x6f\x64\x66\x61\x74\x68\x65\x72"
):
    os._exit(0)
banner = Center.XCenter(
    """
███████╗ ██████╗ ███╗   ███╗ █████╗ ██╗     ██╗███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██║██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║   ██║██╔████╔██║███████║██║     ██║█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║   ██║██║╚██╔╝██║██╔══██║██║     ██║██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 Made by Godfather and K.Dot#4044\n\n
"""
)

options = (
    r"""[1] Level 1 (Recommended to use AFTER 2) (Rot-x method)
[2] Level 2 (More Variable replacement)
[3] Level 3 (Encoding trick by changing first 2 bytes)
[4] Level 4 (NOTE: Don't end your files with exit when its done with this command or it might break. (same with pause))
[5] Level 5 (NOTE: THIS WAS NOT MADE BY ME IT WAS MADE BY https://www.dostips.com/forum/memberlist.php?mode=viewprofile&u=2258 W mans btw) (If u really wanna be mean use Ultimate first lmao)
[clean] cleans the code to try and fix any common errors (FIXES BUILT IN VARIABLES)
[all] does 1, 2, 3 and clean
[fud] makes it undetectable by everything on virustotal

[ultimate] The Ultimate batch obfuscation (The Ultimate batch obfuscation) (Also fud from virus total and all AV)

[embed] Embeds powershell code in a batch file. (they run bat file but it reruns as ps1/powershell)
[exe] Simple Bat2Exe with self extracting zip (usually low detections too)
[exe2] Second method for Bat2Exe (usually low detections but may increase over time)
[COMING SOON] [exe3] Third method for Bat2Exe (100% fud)
[ONELINE] I did it
[exe2bat] Converts exe to bat (EXPERIMENTAL)
[py2bat] Converts python file to bat (Note you cant use things like getting the execution path cause that might break but idk ur choice)

[?] (If you want to use built in variables such as %~dp0 etc wrap them in percent signes then run the clean mode afterwards. You DONT have to do this if your using ultimate)
"""
    + "\n\n"
)

settings = [
    f"Chinese = {chinese}",
    f"Pogdog = {pogdog_fun}",
    f"Hell = {hell}",
    f"Eicar = {eicar}",
    f"Unicode = {unicode}",
    f"UTF-16-BOM = {utf_16_bom}",
    f"ADS = {ads} (Experimental)",
    f"Random Spacing = {random_spacing}",
    f"Echo Weird = {echo_weird} (Experimental)",
    f"Auto Update = {auto_update}",
    f"Anti VM = {anti_vm}",
    f"For Loop Obfuscation = {for_loop} (Experimental)",
    f"Scramble Labels = {scramble_labels} (Experimental)",
    f"Music = {music}",
]


class AutoUpdate:
    def __init__(self):
        self.code = (
            "https://raw.githubusercontent.com/KDot227/Somalifuscator/main/main.py"
        )
        self.bypass = False

        try:
            username = os.getlogin()
            if username == "this1":
                self.bypass = True
            self.update()
        except OSError:
            self.bypass = True

    def update(self):
        if not self.bypass:
            print("Checking for updates...")
            code = requests.get(self.code, timeout=10).text
            with open(__file__, "r", encoding="utf-8", errors="ignore") as f:
                main_code = f.read()
            if code != main_code:
                print("Updating...")
                with open(__file__, "w", encoding="utf-8", errors="ignore") as f:
                    f.write(code)
                os.startfile(__file__)
                os._exit(0)
            else:
                print("No updates found!")


class Main:
    def __init__(self):
        # if u on linux kys
        # nvm I'm on linux now I gotta fix this
        os.system("cls" if os.name == "nt" else "clear")
        print(Colorate.Vertical(Colors.purple_to_blue, banner, 2))
        self.carrot = False
        self.label = False
        # This is so the fud mode doesn't show the first time it's ran
        self.down = False
        self.rep_num = 0
        for setting in settings:
            setting_name, setting_value = setting.split("=")
            setting_name = setting_name.strip()
            setting_value = setting_value.strip()
            if setting_value == "True" or setting_value == "True (Experimental)":
                value_color = colorama.Fore.GREEN
            else:
                value_color = colorama.Fore.RED
            print(
                colorama.Fore.BLUE
                + setting_name
                + " = "
                + value_color
                + setting_value
                + colorama.Style.RESET_ALL
            )
        print(
            Colorate.Vertical(Colors.purple_to_blue, "\nPick your file to obfuscate", 2)
        )

        # asthetic stuff
        time.sleep(1)

        self.file = ""

        while not os.path.exists(self.file):
            self.file = kdot2.askopenfilename(
                title="Select a file to obfuscate",
                filetypes=(("Batch files", "*.bat"), ("All files", "*.*")),
            )

        root.destroy()

        if os.path.exists(self.file):
            os.system("cls" if os.name == "nt" else "clear")
            print(Colorate.Vertical(Colors.purple_to_blue, options, 2))
            self.level = Write.Input(
                "What level of Obfuscation do you want? -> ",
                Colors.green,
                interval=0.05,
            )
            self.level = self.level.lower()
            self.level_dict = {
                "1": self.level1,
                "2": self.level2,
                "3": self.level3,
                "4": self.level4,
                "5": self.level5,
                "clean": self.clean,
                "all": self.all,
                "fud": self.fud,
                "ultimate": self.ultimate,
                "embed": self.embed,
                "exe": self.bat2exe,
                "exe2": self.bat2exe2,
                "oneline": self.oneline,
                "exe2bat": self.exe2bat,
                "py2bat": self.py2bat,
            }

            pick = self.level_dict.get(self.level)
            if pick is not None:
                self.mixer()
                os.system("cls" if os.name == "nt" else "clear")
                pick()
            else:
                print("Invalid option")
                time.sleep(3)
                Main()
        else:
            print(Colors.red + "That file does not exist!" + Colors.reset)
            time.sleep(3)
            Main()

    @staticmethod
    def make_random_string(length_nums=(5, 7)):
        length = random.randint(*length_nums)
        stringed = "".join(
            random.choice(
                # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
                # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            for _ in range(length)
        )
        # yes this has happened to me before and echo check terms it
        while "echo" in stringed.lower():
            stringed = "".join(
                random.choice(
                    # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
                    # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                )
                for _ in range(length)
            )
        return stringed

    @staticmethod
    def random_capitalization(string):
        return "".join(random.choice([char.upper(), char.lower()]) for char in string)

    @staticmethod
    def make_random_label_no_working():
        # 911 lol
        length = random.choice([9, 11])
        return "".join(random.choice(chinese_characters) for _ in range(length))

    @staticmethod
    def fake_ceaser_cipher():
        together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(
            cesar_val
        )
        together = together[:-4]
        return together

    @staticmethod
    def more_dead_comments(main_list) -> list:
        code_examples = [
            "::Made with somalifuscator",
            "::discord.gg/batch",
            "::https://sped.lol",
            "::KDot > Batch",
        ]
        for _ in range(len(main_list)):
            random_chance = random.choice([True, False])
            if random_chance:
                main_list.insert(
                    random.randint(0, len(main_list)),
                    random.choice(code_examples),
                )
        return main_list

    def obf_oneline(self, line):
        final_string = ""
        for word in line.split(" "):
            if word.startswith("%"):
                final_string += word + " "
                continue
            if word.find("%~") != -1:
                final_string += word + " "
                continue
            if word.startswith("^"):
                final_string += word + " "
                continue
            if word.startswith("::"):
                final_string += word + " "
                continue
            else:
                for char in word:
                    # fasho could have used dict for this but idc its already done
                    public = r"C:\Users\Public"
                    weird = r"C:\Program Files (x86)\Common Files"
                    program_1 = r"C:\Program Files"
                    program_2 = r"C:\Program Files (x86)"
                    psmodule_path = r"C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
                    driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
                    comspec = r"C:\WINDOWS\system32\cmd.exe"
                    pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

                    list_of_all = [
                        public,
                        weird,
                        program_1,
                        program_2,
                        psmodule_path,
                        driver_stuff,
                        comspec,
                        pathext,
                    ]

                    corosponding = [
                        "PUBLIC",
                        "COMMONPROGRAMFILES(X86)",
                        "PROGRAMFILES",
                        "PROGRAMFILES(X86)",
                        "PSMODULEPATH",
                        "DRIVERDATA",
                        "COMSPEC",
                        "PATHEXT",
                    ]

                    new_lists = []

                    for i in list_of_all:
                        if char in i:
                            new_lists.append(i)

                    if len(new_lists) > 0:
                        if char == " ":
                            final_string += char
                        new = random.choice(new_lists)
                        if char in new:
                            if new == psmodule_path:
                                index = new.index(char)
                                new = corosponding[list_of_all.index(new)]
                                final_string += (
                                    f"%{self.random_capitalization(new)}:~{index},1%"
                                )
                            else:
                                index = new.index(char)
                                new = corosponding[list_of_all.index(new)]
                                final_string += (
                                    f"%{self.random_capitalization(new)}:~{index},1%"
                                )
                    else:
                        if unicode:
                            final_string += f"%‮%{char}%‮%"
                        else:
                            random_string = "".join(
                                random.choice(string.ascii_letters)
                                for _ in range(randint(5, 7))
                            )
                            final_string += f"%{random_string}%{char}%{random_string}%"
                final_string += " "

        return final_string

    @staticmethod
    def random_oct_hex(ans: int):
        choices = [hex(ans), oct(ans)]
        decided = random.choice(choices)
        if decided == oct(ans):
            return "0" + str(decided[2:])
        else:
            return decided

    @staticmethod
    def random_semi_and_comma(string):
        symbols = [";", ",", " ", "     "]
        random_symbols = "".join(random.choice(symbols) for _ in range(randint(3, 7)))
        new_string = random_symbols + string + random_symbols
        return new_string

    @staticmethod
    def pogdog(entire_array):
        if not unicode:
            return entire_array
        uni = r"็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็"
        for array in entire_array:
            if randint(0, 3) == 3:
                scated = uni * 2
                new_string = [scated]
                entire_array.insert(entire_array.index(array), new_string)

        return entire_array

    def caesar_cipher_rotation(self, letter):
        """Returns the Caesar cipher rotation for a given letter and rotation value."""
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        letter_index = alphabet.index(letter.lower())
        rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
        rotated_letter = rotated_alphabet[letter_index]

        return rotated_letter

    def caesar_cipher_rotation_UPPER(self, letter):
        """Returns the Caesar cipher rotation for a given letter and rotation value."""
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        letter_index = alphabet.index(letter.upper())
        rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
        rotated_letter = rotated_alphabet[letter_index]

        return rotated_letter

    def mixer(self):
        original_file = self.file
        with open("mixer.bat", "w") as f:
            f.write(code)
        self.file = "mixer.bat"
        self.fud()
        with open("mixer.bat.fud.bat", "r", encoding="utf-8", errors="ignore") as f:
            self.code_new = f.read()
        os.remove("mixer.bat")
        os.remove("mixer.bat.fud.bat")
        self.file = original_file

    def level1(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level1.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
            data = f.readlines()
        with open(
            f"{self.file}.level1.bat", "a+", encoding="utf-8", errors="ignore"
        ) as f:
            f.write(self.code_new)
            for line in track(
                data, description="[bold green]Obfuscating", total=len(data)
            ):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)

                        elif var == True:
                            f.write(char)

                        elif "\n" in char:
                            f.write(char)

                        else:
                            random = self.make_random_string()
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = self.caesar_cipher_rotation(char)
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random}%")
                                else:
                                    coded0 = self.caesar_cipher_rotation_UPPER(char)
                                    coded = coded0.replace(coded0, f"%{coded0}1%")
                                    f.write(f"{coded}%{random}%")
                            else:
                                f.write(f"{char}%{random}%")

    def level2(self):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level2.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
            data = f.readlines()
        with open(
            f"{self.file}.level2.bat", "a+", encoding="utf-8", errors="ignore"
        ) as f:
            f.write(f"set KDOT={random_order}\nchcp 65001 > nul\n")
            for line in track(
                data, description="[bold green]Obfuscating", total=len(data)
            ):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)

                        elif var == True:
                            f.write(char)

                        elif "\n" in char:
                            f.write(char)

                        else:
                            if char in string.ascii_letters:
                                vard = f"%KDOT:~{random_order.index(char)},1%"
                                f.write(vard)
                            else:
                                f.write(char)

    def level3(self):
        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(["FF", "FE", "0A", "0D"])
        with open(f"{self.file}", "rb") as f:
            penis = f.read()

        out_hex.extend(["{:02X}".format(b) for b in penis])

        with open(f"{self.file}.level3.bat", "wb") as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))

    def clean(self):
        with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
            contents = f.read()
        with open(
            f"{self.file}.cleaned.bat", "a+", encoding="utf-8", errors="ignore"
        ) as f:
            # if there are any others that people use please make a pr and add them.
            batch_vars = [
                "%~dp0",
                "%~f0",
                "%~n0",
                "%~x0",
                "%~dpnx0",
            ]
            batch_vars_to_replace = [
                r"%~dp0%",
                r"%~f0%",
                r"%~n0%",
                r"%~x0%",
                r"%~dpnx0%",
            ]
            for i in range(len(batch_vars)):
                contents = contents.replace(batch_vars_to_replace[i], batch_vars[i])
            f.write(contents)

    def all(self):
        names = []
        self.level2()
        self.file = f"{self.file}.level2.bat"
        names.append(self.file)
        self.level1()
        self.file = f"{self.file}.level1.bat"
        names.append(self.file)
        self.clean()
        self.file = f"{self.file}.cleaned.bat"
        names.append(self.file)
        self.level3()
        os.rename(f"{self.file}.level3.bat", "FINAL.bat")
        for name in names:
            os.remove(name)
        print("FINAL.bat is the finished product!")
        time.sleep(5)
        os._exit(0)

    def fud(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.fud.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
            data = f.readlines()
        with open(f"{self.file}.fud.bat", "a+", encoding="utf-8", errors="ignore") as f:
            f.write("::Made by K.Dot and Godfather\n")
            # this is so I don't have to see the status bar when using mixer
            if self.down == False:
                for line in data:
                    if line.startswith(":") and not line.startswith("::"):
                        f.write(line)
                        continue
                    for char in line:
                        if char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)
                            elif var == True:
                                f.write(char)
                            elif "\n" in char:
                                f.write(char)
                            else:
                                random = self.make_random_string()
                                f.write(f"{char}%{random}%")
            else:
                for line in track(
                    data, description="[bold green]Obfuscating", total=len(data)
                ):
                    if line.startswith(":") and not line.startswith("::"):
                        f.write(line)
                        continue
                    for char in line:
                        if char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)
                            elif var == True:
                                f.write(char)
                            elif "\n" in char:
                                f.write(char)
                            else:
                                random = self.make_random_string()
                                f.write(f"{char}%{random}%")
        self.down = not self.down

    def ultimate(self, utf_16=True, check_bypass=False) -> None:
        self.check_bypass = check_bypass
        if debug:
            self.check_bypass = True
            utf_16 = False
        # progress bar things
        with Progress() as progress:
            task1 = progress.add_task("[bold green]Searching through file", total=100)
            task1andhalf = progress.add_task("[bold green]Obfuscating", total=100)
            task2 = progress.add_task("[bold green]Adding Anti Echo", total=100)
            task3 = progress.add_task("[bold green]Cleaning Obfuscated Code", total=100)
            task4 = progress.add_task(
                "[bold green]Cleaning up Echo Commands", total=100
            )
            task5 = progress.add_task(
                "[bold green]Writing Out-Bytes to File", total=100
            )
            try:
                os.remove(f"{self.file}.ultimate.bat")
            except:
                pass
            # cool thing
            # mshta vbscript:execute("CreateObject(""Scripting.FileSystemObject"").GetStandardStream(1).Write(Chr(89) & Chr(111)& Chr(117) & Chr(114) & Chr(32) & Chr(109) & Chr(97) & Chr(109) & Chr(97) & Chr(32) ):Close")|more
            # ultimate mode
            with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
                data = f.readlines()

            # This took way longer than it should have
            # Basically the entire point of it is to turn multiline commands that could be oneline into just oneline commands. I'm guessing this will break for anything larger than like 30 lines. If that's the cause then do if not stuff

            # basic parsing of the file and changing things that need to be changed

            new_lines = []
            i = 0
            while i < len(data):
                line = data[i].strip()

                if line.endswith("("):
                    while not line.endswith(")"):
                        i += 1
                        next_line = data[i].strip()
                        # Add '&' between lines cause it can't just do stuff like allat
                        line += " & " + next_line

                    line = line.replace("\n", " ").replace("\r", "")
                    line = " ".join(line.split())

                    # regex cause im a RE tard
                    # that was funny asf ngl
                    matches = re.findall(r"\((.*?)\)", line)
                    for match in matches:
                        if match.startswith(" &"):
                            modified_match = match[2:-2]
                            line = line.replace(match, modified_match)
                        else:
                            modified_match = match

                if line:
                    new_lines.append(line + "\n")
                i += 1

            data = new_lines.copy()

            checked_labels = {}

            if scramble_labels:
                for index, line in enumerate(data):
                    if line.startswith(":") and not line.startswith("::"):
                        label_name = line.split(":")[1]
                        random_string = self.make_random_string((8, 9))
                        checked_labels[label_name] = random_string

                for label_name, new_label_name in checked_labels.items():
                    for index, line in enumerate(data):
                        if line.startswith(":") and not line.startswith("::"):
                            if line.split(":")[1] == label_name:
                                data[index] = f":{new_label_name}\n"
                        else:
                            data[index] = line.replace(
                                label_name, new_label_name + "\n"
                            )

            data = data.copy()

            if debug:
                with open("debug1.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(data)

            env_vars = [
                r"%ALLUSERSPROFILE%",
                r"%APPDATA%",
                r"%CD%",
                r"%CMDCMDLINE%",
                r"%CMDEXTVERSION%",
                r"%COMPUTERNAME%",
                r"%COMSPEC%",
                r"%DATE%",
                r"%ERRORLEVEL%",
                r"%HOMEDRIVE%",
                r"%HOMEPATH%",
                r"%NUMBER_OF_PROCESSORS%",
                r"%OS%",
                r"%PATH%",
                r"%PATHEXT%",
                r"%PROCESSOR_ARCHITECTURE%",
                r"%PROCESSOR_LEVEL%",
                r"%PROCESSOR_REVISION%",
                r"%PROMPT%",
                r"%RANDOM%",
                r"%SYSTEMDRIVE%",
                r"%SYSTEMROOT%",
                r"%TMP%",
                r"%TEMP%",
                r"%TIME%",
                r"%USERDOMAIN%",
                r"%USERNAME%",
                r"%USERPROFILE%",
                r"%WINDIR%",
                r"%0",
                r"%1",
                r"%2",
                r"%3",
                r"%4",
                r"%5",
                r"%6",
                r"%7",
                r"%8",
                r"%9",
                r"%*",
                r"%~dp0",
                r"%~dp1",
                r"%~dp2",
                r"%~dp3",
                r"%~dp4",
                r"%~dp5",
                r"%~dp6",
                r"%~dp7",
                r"%~dp8",
                r"%~dp9",
                r"%~f0",
                r"%~f1",
                r"%~f2",
                r"%~f3",
                r"%~f4",
                r"%~f5",
                r"%~f6",
                r"%~f7",
                r"%~f8",
                r"%~f9",
                r"%~nx0",
                r"%~nx1",
                r"%~nx2",
                r"%~nx3",
                r"%~nx4",
                r"%~nx5",
                r"%~nx6",
                r"%~nx7",
                r"%~nx8",
                r"%~nx9",
                r"%~s0",
                r"%~s1",
                r"%~s2",
                r"%~s3",
                r"%~s4",
                r"%~s5",
                r"%~s6",
                r"%~s7",
                r"%~s8",
                r"%~s9",
                r"%~t0",
                r"%~t1",
                r"%~t2",
                r"%~t3",
                r"%~t4",
                r"%~t5",
                r"%~t6",
                r"%~t7",
                r"%~t8",
                r"%~t9",
                r"%~x0",
                r"%~x1",
                r"%~x2",
                r"%~x3",
                r"%~x4",
                r"%~x5",
                r"%~x6",
                r"%~x7",
                r"%~x8",
                r"%~x9",
                r"%~a0",
                r"%~dpn0",
                r"%~dpnx0",
            ]

            self.used_env_vars = []

            for env_var in env_vars:
                if env_var in data:
                    self.used_env_vars.append(env_var)

            if ads:
                lines = data.copy()
                new_lines = []
                maybe = False

                for line in lines:
                    line = line.lower()
                    # basic checks
                    if (
                        line.startswith("echo")
                        and not line.startswith("echo @")
                        and ("&" not in line or "^&" in line)
                    ):
                        maybe = True
                        new_lines.append(
                            line.strip()
                            + " > somali.txt:kdot & more < somali.txt:kdot\n"
                        )
                    else:
                        new_lines.append(line)

                new_lines.reverse()
                for index, line in enumerate(new_lines):
                    if (
                        line.startswith("echo")
                        and not line.startswith("echo @")
                        and maybe
                    ):
                        new_lines[index] = line.strip() + " & del somali.txt\n"
                        break
                new_lines.reverse()

                data = new_lines.copy()

            if debug:
                with open("debug1_2.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(data)

            progress.update(task1, advance=100)
            with open(
                f"{self.file}.ultimate.bat", "a+", encoding="utf-8", errors="ignore"
            ) as f:
                f.write("::Made by K.Dot and Godfather\n")
                f.write(self.code_new)
                characters = (
                    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                )
                random_order = "".join(random.sample(characters, len(characters)))
                f.write(self.obf_oneline(f"set KDOT={random_order}\n"))
                # for line in track(
                #    data, description="[bold green]Obfuscating", total=len(data)
                # ):
                # This regex is basically tryna get variables that are set to a value. For example if someone has set "starttime=%time%"
                regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")
                for line in data:
                    progress.update(task1andhalf, advance=100 / len(data))
                    random_bool = random.choice([True, False])
                    if for_loop:
                        random_bool_2 = random.choice([True, False])
                        if random_bool_2 and not line.startswith(":"):
                            line = self.ran3(line=line)
                    if line.startswith("::"):
                        f.write(line)
                        continue
                    elif line.startswith(":"):
                        f.write(line)
                        continue
                    else:
                        if random_bool == True:
                            symbols = [";", ",", " ", "     "]
                            random_symbols = "".join(
                                random.choice(symbols) for _ in range(randint(3, 7))
                            )
                            f.write(random_symbols)
                        for word in line.split():
                            if any(env_var in word for env_var in env_vars):
                                f.write(word + " ")
                                continue
                            elif word.startswith("%") or word.startswith("!"):
                                f.write(self.random_capitalization(word) + " ")
                                continue
                            elif re.match(regex_bat, word):
                                # regex be my bae
                                f.write(word + " ")
                                continue
                            else:
                                for char in word:
                                    if char == "\n":
                                        f.write("\n")
                                        continue
                                    elif char == " ":
                                        f.write(" ")
                                        continue
                                    else:
                                        random_obf = [
                                            self.ran1(char),
                                            self.ran2(char, random_order),
                                        ]
                                        f.write(f"{random.choice(random_obf)}")
                                f.write(" ")
                        f.write("\n")
            # ignore everything below this until the function ends I could have made this 100x better but I'm lazy
            with open(
                f"{self.file}.ultimate.bat", "r", encoding="utf-8", errors="ignore"
            ) as f:
                news = f.readlines()
            if debug:
                with open("debug2.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(news)
            news.insert(2, self.obf_oneline(self.first_line_echo_check()))
            messed_up = self.scrambler(news)
            progress.update(task2, advance=100)
            with open(
                f"{self.file}.ultimate.bat", "w", encoding="utf-8", errors="ignore"
            ) as f:
                for array in messed_up:
                    for thing in array:
                        f.write(thing.strip() + "\n")
            if debug:
                with open("debug3.bat", "w", encoding="utf-8", errors="ignore") as f:
                    for array in messed_up:
                        for thing in array:
                            f.write(thing.strip() + "\n")
            progress.update(task3, advance=100)
            with open(
                f"{self.file}.ultimate.bat", "r", encoding="utf-8", errors="ignore"
            ) as f:
                data = f.readlines()
                # add echo off to the first line
                data.insert(0, "@echo off\n")
                for i in range(len(data)):
                    if "echo" in data[i]:
                        data[i] = data[i].replace(
                            "echo", r"%GODFATHER%e%GODFATHER%c%GODFATHER%h%GODFATHER%o"
                        )
                    if not data[i].startswith(";") or not data[i].startswith("; "):
                        new = self.random_semi_and_comma(data[i])
                        data[i] = new
            if debug:
                with open("debug4.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(data)
            progress.update(task4, advance=100)
            if utf_16_bom and utf_16:
                out_hex = self.anti_check_error(code=data)
                with open(f"{self.file}.ultimate.bat", "wb") as f:
                    for i in out_hex:
                        f.write(bytes.fromhex(i))
            else:
                with open(
                    f"{self.file}.ultimate.bat", "w", encoding="utf-8", errors="ignore"
                ) as f:
                    for line in data:
                        f.write(line)
            progress.update(task5, advance=100)

    def ran1(self, char):
        # caesar cipher rotation shi
        choices = [self.make_random_string(), self.make_random_string()]
        randomed = random.choice(choices)
        if char in string.ascii_letters:
            if char.islower():
                coded0 = self.caesar_cipher_rotation(char)
                coded = coded0.replace(coded0, f"%{coded0}%")
                return f"{coded}%{randomed}%"
            else:
                coded0 = self.caesar_cipher_rotation_UPPER(char)
                coded = coded0.replace(coded0, f"%{coded0}1%")
                return f"{coded}%{randomed}%"
        else:
            return f"{char}%{randomed}%"

    def ran2(self, char, random_order):
        # fasho could have used dict for this but idc its already done
        public = r"C:\Users\Public"
        weird = r"C:\Program Files (x86)\Common Files"
        program_1 = r"C:\Program Files"
        program_2 = r"C:\Program Files (x86)"
        psmodule_path = r"C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
        driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
        comspec = r"C:\WINDOWS\system32\cmd.exe"
        pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

        list_of_all = [
            public,
            weird,
            program_1,
            program_2,
            psmodule_path,
            driver_stuff,
            comspec,
            pathext,
        ]

        corosponding = [
            "PUBLIC",
            "COMMONPROGRAMFILES(X86)",
            "PROGRAMFILES",
            "PROGRAMFILES(X86)",
            "PSMODULEPATH",
            "DRIVERDATA",
            "COMSPEC",
            "PATHEXT",
        ]

        new_lists = []

        for i in list_of_all:
            if char in i:
                new_lists.append(i)

        if len(new_lists) > 0:
            if char == " ":
                return char
            new = random.choice(new_lists)
            if char in new:
                if new == psmodule_path:
                    index = new.index(char)
                    new = corosponding[list_of_all.index(new)]
                    return f"%{self.random_capitalization(new)}:~{index},1%"
                else:
                    index = new.index(char)
                    new = corosponding[list_of_all.index(new)]
                    return f"%{self.random_capitalization(new)}:~{index},1%"
        else:
            if char in string.ascii_letters:
                var = f"%{self.random_capitalization('KDOT')}:~{random_order.index(char)},1%"
                return var
            else:
                return char

    # def ran3(self, char):
    #    if char in string.ascii_letters:
    #        escape = "^"
    #        return f"{escape}{char}"
    #    else:
    #        return char'

    def ran3(self, line):
        random_letter = random.choice(string.ascii_letters)
        random_number = random.randint(1, 99)
        return f"for /l %%{random_letter} in ( {random_number}, {random_number}, {random_number} ) do ( {line} )\n"

    def ran4(self, char):
        return char

    def random_dead_code(self, entire_array):
        """Dead code that just won't be executed so it can be whatever. If u wanna add more its all u"""
        dead_code = [
            "echo Best Batch Obfuscated By KDot and Godfather\n",
            "if 0 == 0 (echo Best Batch Obfuscated By KDot and Godfather)\n",
            f"set KDOT={self.fake_KDOT()}\n",
            f"{self.fake_ceaser_cipher()}\n",
            f"{self.fake_ceaser_cipher_obfuscated()}\n",
            f"set somalifuscator=op_asf\n",
        ]
        if eicar:
            dead_code.append(
                "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n"
            )
        for array in entire_array:
            if randint(0, 3) == 3:
                option = random.choice(dead_code)
                if (
                    option
                    # it's funny cause it's still fud even unobfuscated
                    == "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n"
                ):
                    scated = option
                else:
                    scated = self.obf_oneline(option)
                new_string = "".join(scated)
                new_string = [new_string]
                entire_array.insert(entire_array.index(array), new_string)

        return entire_array

    def vm_test(self):
        codes = [
            # r"""for /f "tokens=2 delims==" %%a in ('wmic computersystem get manufacturer /value') do set manufacturer=%%a\nfor /f "tokens=2 delims==" %%a in ('wmic computersystem get model /value') do set model=%%a\nif "%manufacturer%"=="Microsoft Corporation" if "%model%"=="Virtual Machine" exit\nif "%manufacturer%"=="VMware, Inc." exit\nif "%model%"=="VirtualBox" exit""",
            # r"""for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "Total Physical Memory"') do ( set available_memory=%%a ) & set available_memory=%available_memory: =% & set available_memory=%available_memory:M=% & set available_memory=%available_memory:B=% & set /a available_memory=%available_memory% / 1024 / 1024 & if not %available_memory% gtr 4 ( exit /b 1 )""",
            # I love batch so much I gave up and used powershell
            """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$VM=Get-WmiObject -Class Win32_ComputerSystem ; if ($VM.Model -match 'Virtual') { Write-Host 'Virtual Machine Detected. Exiting script.' ; taskkill /F /IM cmd.exe }\""""
            # """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "$tr=(Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory / 1KB ; $trgb=[math]::Round($tr / 1024, 2) ; if ($trgb -lt 8) { Write-Host 'Less than 8gb ram exiting' ; pause }\""""
        ]
        # ill add more one day
        return self.obf_oneline(random.choice(codes))

    def byte_check(self):
        choices = [
            """powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$bytes = [System.IO.File]::ReadAllBytes('%~f0') ; if (($bytes[0] -ne 0xFF) -or ($bytes[1] -ne 0xFE) -or ($bytes[2] -ne 0x26)) { Write-Host 'The first 3 bytes of the file are not FF FE 0A.' ; taskkill /F /IM cmd.exe }\"""",
        ]

        choice = random.choice(choices)
        obfus = self.obf_oneline(choice)
        return obfus

    def tests(self):
        # I just made this cause editing it the other way would be annoying
        choices = [self.first_line_echo_check()]
        if anti_vm:
            choices.append(self.vm_test())

        if utf_16_bom:
            choices.append(self.byte_check())

        if debug:
            choices = [self.first_line_echo_check()]
        return choices

    def fake_ceaser_cipher_obfuscated(self):
        """simple function to obfuscate the cipher"""
        cipher = self.fake_ceaser_cipher()
        obfuscated = self.obf_oneline(cipher)
        return obfuscated

    def fake_KDOT(self):
        """makes fake KDOT var"""
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        return random_order

    def generate_math_problem(self, answer: int):
        """Entire point of this is to make a math problem for the set /a. We do this cause kids need a calculator but once they see that there are octals and hexadecimals they'll prolly give up lmao"""
        # no division since we don't want floats BUT we can use division in the answer since its how you undo multiplication
        # but im not gonna do this cause it still makes floats and im slow
        operators = ["+", "-"]
        opp1 = random.choice(operators)
        opp2 = random.choice(operators)
        num1 = random.randint(10000, 10000000)
        num2 = random.randint(10000, 10000000)

        # maybe add division and multiplication to the problem using even dividers and getting remainder to check if zero.

        problem = f"{answer} {opp1} {num1} {opp2} {num2}"
        ans = eval(problem)

        # make new problem from original answer

        if opp1 == "+":
            opp1 = "-"
        else:
            opp1 = "+"

        if opp2 == "+":
            opp2 = "-"
        else:
            opp2 = "+"

        # randomly do hex or oct to ans instead of all just hex
        problem2 = f"{self.random_oct_hex(ans)} {opp1} {self.random_oct_hex(num1)} {opp2} {self.random_oct_hex(num2)}"
        problem23 = f"{ans} {opp1} {num1} {opp2} {num2}"

        ans2 = eval(problem23)

        while ans < 0:

            operators = ["+", "-"]
            opp1 = random.choice(operators)
            opp2 = random.choice(operators)
            num1 = random.randint(10000, 10000000)
            num2 = random.randint(10000, 10000000)

            problem = f"{answer} {opp1} {num1} {opp2} {num2}"
            ans = eval(problem)

            # make new problem from original answer

            if opp1 == "+":
                opp1 = "-"
            else:
                opp1 = "+"

            if opp2 == "+":
                opp2 = "-"
            else:
                opp2 = "+"

            # for some reason if number is negative only hex will work idk why and im not tryna figure it out
            # mental health > octals
            problem2 = f"{hex(ans)} {opp1} {self.random_oct_hex(num1)} {opp2} {self.random_oct_hex(num2)}"
            problem23 = f"{ans} {opp1} {num1} {opp2} {num2}"

            ans2 = eval(problem23)

        return problem2, ans2

    def scrambler(self, codeed):
        """This absolutely beautiful function takes the code, puts it into a nested array of goto values that all point to each other then obfuscates tf outta it."""
        original_lines = codeed

        for index, line in enumerate(original_lines):
            random_number = random.randint(1, 4)
            if random_number == 1:
                # add a label that doesn't do anything
                label = f":{self.make_random_label_no_working()}\n"
                original_lines.insert(index, label)

        original_lines = [
            item for item in original_lines if item not in [";", "\n", ";\n"]
        ]

        self.dict_thing = {}

        main_list = []

        for index, item in enumerate(original_lines):
            t = self.generate_math_problem(answer=random.randint(100000, 10000000))
            self.dict_thing[item] = [
                t[0],
                t[1],
                index,
            ]

        # I use ; infront of everything cause it gets rid of syntax highlight on vscode and notepad++ lmao
        for index, (key, value) in enumerate(self.dict_thing.items()):
            if index == 0:
                remem = [
                    f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(value[0])}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                ]
            part_1 = f";:{value[1]}\n"
            part_2 = f";{key}\n"
            if hell and unicode:
                badded = (
                    r" ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็"
                    * random.randint(10, 20)
                )
                try:
                    random_t_f = random.choice([True, False])
                    if random_t_f:
                        dead = list(self.dict_thing.values())[index + 1][1]
                        random_working_value = random.choice(
                            list(self.dict_thing.values())
                        )
                        while random_working_value[1] == dead:
                            random_working_value = random.choice(
                                list(self.dict_thing.values())
                            )
                        run = self.deadcodes(
                            good_label=str(dead), bad_label=random_working_value[1]
                        )
                        part_3 = f"{run}\n::{badded}\n"
                    else:
                        maybe_echo_check = random.randint(1, 3)
                        if maybe_echo_check == 1:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n::{badded}\n::{badded}\n::{badded}\n{self.obf_oneline(random.choice(self.tests()))}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                        else:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n::{badded}\n::{badded}\n::{badded}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                except Exception:
                    part_3 = f";{self.random_semi_and_comma(self.obf_oneline('goto'))} :EOF\n::{badded}\n::{badded}\n::{badded}\n"
            else:
                try:
                    random_t_f = random.choice([True, False])
                    if random_t_f:
                        dead = list(self.dict_thing.values())[index + 1][1]
                        random_working_value = random.choice(
                            list(self.dict_thing.values())
                        )
                        while random_working_value[1] == dead:
                            random_working_value = random.choice(
                                list(self.dict_thing.values())
                            )
                        run = self.deadcodes(
                            good_label=str(dead), bad_label=random_working_value[1]
                        )
                        part_3 = f"{run}\n"
                    else:
                        maybe_echo_check = random.randint(1, 3)
                        if maybe_echo_check == 1:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n{self.obf_oneline(random.choice(self.tests()))}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                        else:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                except Exception:
                    part_3 = f";{self.random_semi_and_comma(self.obf_oneline('goto'))} :EOF\n"

            main_list.append([part_1, part_2, part_3])

        random.shuffle(main_list)

        main_list = self.bad_labels_and_dead_code(main_list)

        main_list = self.random_inserts(main_list)

        main_list = self.random_dead_code(main_list)

        if random_spacing:
            main_list = self.more_dead_comments(main_list)

        if pogdog_fun:
            main_list = self.pogdog(main_list)

        # pointer that points to first line of the actual code.
        main_list.insert(0, remem)

        return main_list

    def deadcodes(self, good_label, bad_label):
        """not really deadcode but it just makes it hard for kids to understand"""
        # gotta love %random%
        # hehehehe
        RANNUM = randint(32769, 99999)
        # This is absolute hell for anyone trying to deobfuscate this
        label123 = bad_label
        if self.rep_num < 5:
            examples = [
                f"if %random% equ {RANNUM} ( goto :{label123} ) else ( goto :{good_label} )",
                f"if not 0 neq 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System32 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if not %cd% == %cd% ( goto :{label123} ) else ( goto :{good_label} )",
                f"if 0 equ 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System3 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %cd% == %cd% ( goto :{good_label} ) else ( goto :{label123} )",
                f"if chcp leq 1 ( goto :{label123} ) else ( goto :{good_label} )",
            ]
        else:
            examples = [
                f"if %random% equ {RANNUM} ( goto :{label123} ) else ( goto :{good_label} )",
                f"if not 0 neq 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System32 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if not %cd% == %cd% ( goto :{label123} ) else ( goto :{good_label} )",
                f"if 0 equ 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System3 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %cd% == %cd% ( goto :{good_label} ) else ( goto :{label123} )",
                f"if chcp leq 1 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if not defined KDOT ( goto :EOF ) else ( goto :{good_label} )",
                f"if not defined f ( goto :EOF ) else ( goto :{good_label} )",
            ]
        if echo_weird:
            random_maybe = random.choice([True, False])
            code_examples = [
                "::Made with somalifuscator",
                "::discord.gg/batch",
                "::https://sped.lol",
                "::KDot > Batch",
            ]
            if random_maybe:
                coded = f"{random.choice(code_examples)} ^\n {random.choice(examples)} ^\n exit /b 0\n{random.choice(examples)}"
                for _ in range(3):
                    examples.append(coded)
            else:
                coded = f"{random.choice(code_examples)} ^\n exit /b 0\n {random.choice(examples)}"
                for _ in range(3):
                    examples.append(coded)

        randomed = random.choice(examples)
        obfuscated = self.obf_oneline(randomed)
        self.rep_num += 1
        return obfuscated

    def random_inserts(self, main_list):
        listes = [
            ";::Made by K.Dot and Godfather\n",
            ";::Good luck deobfuscating\n",
            ";::Made with Somalifuscator\n",
            ";::discord.gg/batch\n",
            ";::... --- -- .- .-.. .. ..-. ..- ... -.-. .- - --- .-. / --- -. / - --- .--.",
        ]
        for i in range(len(main_list)):
            if i == 0:
                continue
            else:
                random_int = randint(1, 10)
                if random_int == 10:
                    list_choice = random.choice(listes)
                    main_list.insert(i, [list_choice])

        return main_list

    def bad_labels_and_dead_code(self, main_list):
        """inserts labels that are valid but won't do anything since they have a zero width space infront. This mainly messes up looking at it from a text editor. You can still goto it if you use the weird translated bytes."""
        main_dict = self.dict_thing.copy()
        new_list = []
        types = [True, False]
        doskey_options = [
            "dir",
            "echo",
            "for",
            "if",
            "set",
            "goto",
            "cd",
            "",
        ]
        random_choci = random.choice(types)
        bad_insert = "GODFATHER"
        for item in main_dict.values():
            strung = str(item[1])
            strung = ";:" + bad_insert + strung
            new_list.append(strung)
        for array in main_list:
            if random_choci:
                random_chance = randint(1, 3)
                if random_chance == 5:
                    random_label = random.choice(new_list)
                    random_place = randint(0, len(array))
                    array.insert(random_place, random_label)
            else:
                doskey = f"doskey {random.choice(doskey_options)}={random.choice(doskey_options)}"
                # we gotta place at zero or else we get bad output for errorlevel checking
                array.insert(0, self.obf_oneline(doskey))
        return main_list

    def first_line_echo_check(self):
        """basically just checks the entire file for the word echo. If it finds it then it will kill the process. Also the no debug checks to see if the user is double clicking the file instead of running it through a different application"""
        # I hate people who echo :angryface:
        self.checked123 = True
        # This is for when I run through vscode but I can't since it just finna close itself
        self.debug = False
        if self.check_bypass:
            return ""
        if self.debug:
            if self.checked123 == True:
                command = (
                    r'echo @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( ( goto ) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                    + "\n"
                )
                self.checked123 = False
                return command
            else:
                command = (
                    r'echo @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( ( goto ) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                    + "\n"
                )
                return command
        else:
            if self.checked123 == True:
                command = (
                    """net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q close.bat >nul 2>&1 & exit )\necho @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                    + "\n"
                )
                self.checked123 = False
                return command
            else:
                command = (
                    """net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q close.bat >nul 2>&1 & exit )\necho @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                    + "\n"
                )
                return command

    def anti_check_error(self, code):
        """This just checks to see if the first byte of the file is the utf-16 BOM. If it is then it clears screen otherwise it exits."""
        strung = ">nul 2>&1 && exit >nul 2>&1 || cls \n@%nobruh%e%nobruh%c%nobruh%h%nobruh%o o%nobruh%f%nobruh%f%nobruh%\n"
        code.insert(0, strung)

        # There is a 99% chance I could have just used .encode() but im just lazy like that if u gotta problem wit it make a pr

        with open("placeholder.bat", "w", encoding="utf-8", errors="ignore") as f:
            f.writelines(code)
        with open("placeholder.bat", "rb") as f:
            code = f.read()

        os.remove("placeholder.bat")

        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE"])

        out_hex.extend(["{:02X}".format(b) for b in code])

        return out_hex

    def embed(self):
        starting_code_normal = """<# :validbatch
@echo off
setlocal
cd /d "%~dp0"

echo K.Dot up

powershell.exe -ep Bypass -Command "IEX $([System.IO.File]::ReadAllText('%~f0'))"
goto :eof
#>"""
        starting_code_to_obf = """@echo off
setlocal
cd /d "%~dp0"

echo K.Dot up

powershell.exe -ep Bypass -Command "IEX $([System.IO.File]::ReadAllText('%~f0'))"
goto :eof
"""
        ps1_file_location = Write.Input(
            "Enter the location of the ps1 file: ", Colors.green, interval=0.05
        )
        try:
            with open(ps1_file_location, "r", encoding="utf-8", errors="ignore") as f:
                data = f.readlines()
        except FileNotFoundError:
            print("File not found!")
            time.sleep(3)
            Main()
        obfuscate = Write.Input(
            "Would you like to obfuscate the batch code? (y/n): ",
            Colors.green,
            interval=0.05,
        )
        if obfuscate.lower() == "y":
            with open("place_holder.bat", "w", encoding="utf-8", errors="ignore") as f:
                f.write(starting_code_to_obf)
                self.file = "place_holder.bat"
            self.ultimate(utf_16=False, check_bypass=True)
            os.remove("place_holder.bat")
            os.rename("place_holder.bat.ultimate.bat", "embed.bat")
            with open("embed.bat", "r+", encoding="utf-8", errors="ignore") as f:
                data2 = f.readlines()
                data2_size = len(data2)
                data2.insert(0, "<# :validkdot\n")
                data2.insert(data2_size + 1, "#>\n")
                data2 += data
            with open("embed.bat", "w+", encoding="utf-8", errors="ignore") as f:
                f.writelines(data2)
        else:
            # I can FASHO make this a lot cleaner and better but im too lazy rn (split string into list instead of reading it from file :skull:)
            with open("embed.bat", "w", encoding="utf-8", errors="ignore") as f:
                f.write(starting_code_normal)
            with open("embed.bat", "r+", encoding="utf-8", errors="ignore") as f:
                data2 = f.readlines()
            with open("embed.bat", "w", encoding="utf-8", errors="ignore") as f:
                data2_size = len(data2)
                data2.insert(data2_size, "\n")
                data2 += data
                f.writelines(data2)

    def level4(self):
        # Level 4 as promised. (I lowkey skidded it from someone else but i cant remember who :skull:) W mans tho ong
        # Also I can remake this instead of using JScript, etc
        batch_code = """@if (@CodeSection == @Batch) @then


@echo off
setlocal DisableDelayedExpansion

if "%~1" equ "" echo Usage: Obfuscate filename.bat & goto :EOF
if not exist "%~1" echo File not found: "%~1" & goto :EOF

set "at=@"
set "pass=%random%"
(
    echo %at%if (@Pass == @X%pass%^) @begin
    echo    @echo off
    echo    CScript //nologo //E:JScript.Encode "%%~F0" ^> %pass%.bat
    echo    call %pass%
    echo    del /f /q %pass%.bat
    echo    exit /B
    echo %at%end 
    echo //**Start Encode**
    echo var a = new Array(^);

    set "i=0"
    for /F "usebackq delims=" %%a in ("%~1") do (
        set /A i+=1
        set "line=%%a"
        setlocal EnableDelayedExpansion
        echo a[!i!] = '!line:'=\x27!';
        endlocal
    )

    setlocal EnableDelayedExpansion
    echo for ( var i=1; i^<=!i!; ++i ^) WScript.Stdout.WriteLine(a[i]^);
) > "%~N1.tmp"

CScript //nologo //E:JScript "%~F0" "%~N1.tmp"
::rename "%~N1.tmp" "%~N1.bat"
::del "%~N1.tmp"
rename "%~N1.tmp" "%~N1.encoded.bat"
goto :EOF


@end

//Made by some guy on stack overflow (I can't find the post anymore + I delete the old comments I had :sob:)
//I had to edit it a lil bit to make it work again. (It didn't work at all for me before)

var fileToEncode = WScript.Arguments(0);

var oFSO = WScript.CreateObject("Scripting.FileSystemObject");
var oFile = oFSO.GetFile(fileToEncode);
var oStream = oFile.OpenAsTextStream(1);
var sSourceFile = oStream.ReadAll();
oStream.Close();

var oEncoder = WScript.CreateObject("Scripting.Encoder");
var sDest = oEncoder.EncodeScriptFile(".js", sSourceFile, 0, "")

var edited_name = fileToEncode.replace(".bat", ".encoded.bat");

var oStream = oFSO.OpenTextFile(fileToEncode, 2, true);
oStream.Write(sDest);
oStream.Close();"""
        with open("level4.bat", "w") as f:
            f.writelines(batch_code)
        os.system("level4.bat " + self.file)
        file_name = self.file.replace(".bat", ".encoded.bat")
        os.rename(f"{file_name}", f"{self.file}.level4.bat")
        os.remove("level4.bat")

    def level5(self):
        batch_code = r"""@echo off
setlocal disableDelayedExpansion
if /i "%~1" equ "/m" set "/m=/m" & shift /1
set "in=%~1"
if not defined in echo Error: Missing inputFile>&2&exit /b
set "out=%~2"
if not defined out set "out=%~dpn1_obfuscated%~x1"
set "find={[:<][^}]*}|^[^:\r\n]?[ \t=,;\xFF]*:[^ \t:\r\n+]*[ \t:\r\n+]?|%%%%|%%\*|%%(?:~[fdpnxsatz]*(?:\$[^:\r\n]+:)?)?[0-9]|%%[^%%\r\n]+%%|%%@[\x20-\x24\x26-\x7E]"
set "repl=$txt=$0@$txt='%%'+String.fromCharCode($0.charCodeAt(0)+129)+'%%'"

setlocal enableDelayedExpansion
set "str1="
set "x=x"
for %%A in (2 3 4 5 6 7) do @for %%B in (0 1 2 3 4 5 6 7 8 9 A B C D E F) do set "str1=!str1!\x%%A%%B"
set "str1=%str1:~0,-4%"
set "str1=%str1:\x22=%\x22"
set "str1=%str1:\x24\x25=DDDD%"
call jrepl x str1 /m /x /v /s x /rtn lo
set "lo=!lo:DDDD=$!"

set "str2="
for %%A in (A B C D E F) do @for %%B in (0 1 2 3 4 5 6 7 8 9 A B C D E F) do set "str2=!str2!\x%%A%%B"
set "str2=%str2:~4%"
set "str2=%str2:\xA3=%\xA3"
set "str2=%str2:\xA6=%"
call jrepl x str2 /m /x /v /s x /rtn hi
call jrepl "" "%%%%=%%%%" /m /x /s hi /rtn hi2

call :write <"!in!" >"!out!"
exit /b

:write
echo @echo off^&(if defined @lo@ goto !hi:~0,1!)^&setlocal disableDelayedExpansion^&for /f "delims=:. tokens=2" %%%%A in ('chcp') do set "@chcp@=chcp %%%%A>nul"^&chcp 708^>nul^&set ^^^^"@args@=%%*"
echo set "@lo@=!lo!"
echo set "@hi@=!hi2!"
echo (setlocal enableDelayedExpansion^&for /l %%%%N in (0 1 93) do set "^!@hi@:~%%%%N,1^!=^!@lo@:~%%%%N,1^!")^&cmd /c ^^^^^""%%~f0" ^^!@args@^^!"
echo %%@chcp@%%^&exit /b
echo :!hi:~0,1!
jrepl "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"^
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"^
        %/m% /t "" /p "{[^:}][^}]*}" | jrepl find repl %/m% /t @ /v /x /jq
exit /b """
        with open("level5.bat", "w") as f:
            f.write(batch_code)
        r = requests.get(
            "https://www.dostips.com/forum/download/file.php?id=605", timeout=10
        )
        with open("jrepl.zip", "wb") as f:
            f.write(r.content)
        with ZipFile("jrepl.zip", "r") as zipObj:
            zipObj.extractall()
        os.remove("jrepl.zip")
        os.system("level5.bat " + self.file)
        os.remove("level5.bat")
        os.remove("JREPL.bat")
        file = self.file.replace(".bat", "_obfuscated.bat")
        os.rename(f"{file}", f"{self.file}.level5.bat")

    def bat2exe(self):
        code = r"""[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
"""
        current_dir = os.getcwd()
        bat_file_name = os.path.basename(self.file)
        exe_name = bat_file_name[:-4] + ".exe"

        app_launched = "AppLaunched=cmd /c " + '"' + bat_file_name + '"'
        target = f"TargetName={exe_name}"
        file_0 = f"FILE0={bat_file_name}"
        source_files = f"[SourceFiles]\nSourceFiles0={current_dir}"
        extra = f"[SourceFiles0]\n%FILE0%="

        to_write = [app_launched, target, file_0, source_files, extra]
        with open("setup.sed", "a+") as f:
            f.write(code)
            for item in to_write:
                f.write(item + "\n")
        os.system("iexpress /n /q /m setup.sed")
        os.remove("setup.sed")
        print(f"Exe file saved as {exe_name}")

    def bat2exe2(self):
        warning = Write.Input(
            "WARNING: This method requires you to download a exe file from the github repo and run it. Are you ok with this? (y/n): ",
            Colors.green,
            interval=0.05,
        )
        if warning.lower() == "n":
            time.sleep(3)
            Main()
        else:
            r = requests.get(
                "https://github.com/KDot227/Somalifuscator/releases/download/Bat2Exe_Method1/Bat2Exe.exe"
            )
            with open("Bat2Exe.exe", "wb") as f:
                f.write(r.content)
            os.system("start Bat2Exe.exe")
            time.sleep(3)

    def oneline(self):
        batch_code = """
@if (@CodeSection == @Batch) @then


@echo off
setlocal DisableDelayedExpansion

if "%~1" equ "" echo Usage: Obfuscate filename.bat & goto :EOF
if not exist "%~1" echo File not found: "%~1" & goto :EOF

set "pass=%random%"
(
    echo /* @echo off ^& CScript //nologo //E:JScript.Encode "%%~F0" ^> %pass%.bat ^& call %pass% ^& del /f /q %pass%.bat ^& exit /B */ //**Start Encode**
    echo var a = new Array(^);

    set "i=0"
    for /F "usebackq delims=" %%a in ("%~1") do (
        set /A i+=1
        set "line=%%a"
        setlocal EnableDelayedExpansion
        echo a[!i!] = '!line:'=\x27!';
        endlocal
    )

    setlocal EnableDelayedExpansion
    echo for ( var i=1; i^<=!i!; ++i ^) WScript.Stdout.WriteLine(a[i]^);
) > "%~N1.tmp"

CScript //nologo //E:JScript "%~F0" "%~N1.tmp"
::rename "%~N1.tmp" "%~N1.bat"
::del "%~N1.tmp"
rename "%~N1.tmp" "%~N1.encoded.bat"
goto :EOF


@end

//Made by some guy on stack overflow (I can't find the post anymore + I delete the old comments I had :sob:)
//I had to edit it a lil bit to make it work again. (It didn't work at all for me before)

var fileToEncode = WScript.Arguments(0);

var oFSO = WScript.CreateObject("Scripting.FileSystemObject");
var oFile = oFSO.GetFile(fileToEncode);
var oStream = oFile.OpenAsTextStream(1);
var sSourceFile = oStream.ReadAll();
oStream.Close();

var oEncoder = WScript.CreateObject("Scripting.Encoder");
var sDest = oEncoder.EncodeScriptFile(".js", sSourceFile, 0, "")

var edited_name = fileToEncode.replace(".bat", ".encoded.bat");

var oStream = oFSO.OpenTextFile(fileToEncode, 2, true);
oStream.Write(sDest);
oStream.Close();
        """
        with open("oneline.bat", "w") as f:
            f.writelines(batch_code)
        os.system("oneline.bat " + self.file)
        file_name = self.file.replace(".bat", ".encoded.bat")
        os.rename(f"{file_name}", f"{self.file}.oneline.bat")
        os.remove("oneline.bat")

    def exe2bat(self):
        code = r"""@echo off
powershell "$base64_last_line = Get-Content %~f0 | Select-Object -Last 1 ; $bytes = [System.Convert]::FromBase64String($base64_last_line) ; [System.IO.File]::WriteAllBytes('%~dp0\kdot.exe', $bytes)"
start /b /WAIT %~dp0\kdot.exe
del /f /q %~dp0\kdot.exe
exit
"""

        self.exe_path = Write.Input("Enter the path to the exe file: ", Colors.green)
        if not os.path.isfile(self.exe_path):
            print("File does not exist!")
            time.sleep(3)
            Main()
        to_subprocess = f"powershell.exe -C \"$base64 = [System.Convert]::ToBase64String([System.IO.File]::ReadAllBytes('{self.exe_path}')); $base64 | Out-File -Encoding ASCII -FilePath 'test.txt' -NoNewline\""
        subprocess.run(to_subprocess)
        with open("test.txt", "rb") as f:
            data = f.read()
        with open("mixer.bat", "w") as f:
            f.write(code)
        self.file = "mixer.bat"
        self.ultimate(utf_16=False, check_bypass=True)
        with open("mixer.bat.ultimate.bat", "rb") as f:
            insides = f.read()
        os.remove("mixer.bat.ultimate.bat")
        with open("mixer.bat.ultimate.bat", "wb") as f:
            f.write(insides + b"\n" + data)
        os.remove("test.txt")
        os.remove("mixer.bat")
        os.rename("mixer.bat.ultimate.bat", "bat2exe.bat")

    def py2bat(self):
        # https://stackoverflow.com/questions/4571244/creating-a-bat-file-for-python-script
        # I had another way of doing this but it was absolute dog compared to this method
        start_code = """
0<0# : ^
'''
@echo off
echo batch
python "%~f0" %*
exit /b 0
'''
"""
        python_code = Write.Input("Enter the path to the python file: ", Colors.green)
        if not os.path.isfile(python_code):
            print("File does not exist!")
            time.sleep(3)
            Main()
        with open(python_code, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
        with open("py2bat.bat", "w", encoding="utf-8", errors="ignore") as f:
            f.write(start_code + data)


if __name__ == "__main__":
    threads = []
    if music:
        threads.append(Music)
    if auto_update:
        threads.append(AutoUpdate)
    if not threads == []:
        for thread in threads:
            threading.Thread(target=thread).start()
    Main()
    print("Done!")
    input()
    os._exit(0)
