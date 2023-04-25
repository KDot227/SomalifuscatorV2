from pystyle import *
import colorama
import time
import os

def menu(settings):
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

    options1 = r"""[1] Level 1 (Recommended to use AFTER 2) (Rot-x method)
[2] Level 2 (More Variable replacement)
[3] Level 3 (Encoding trick by changing first 2 bytes)
[4] Level 4 (NOTE: Don't end your files with exit when its done with this command or it might break. (same with pause))
[5] Level 5 (NOTE: THIS WAS NOT MADE BY ME IT WAS MADE BY https://www.dostips.com/forum/memberlist.php?mode=viewprofile&u=2258 W mans btw) (If u really wanna be mean use Ultimate first lmao)
[clean] cleans the code to try and fix any common errors (FIXES BUILT IN VARIABLES)
[all] does 1, 2, 3 and clean
[fud] makes it undetectable by everything on virustotal
"""
    options2 = r"""
[ultimate] The Ultimate batch obfuscation (The Ultimate batch obfuscation) (Also fud from virus total and all AV)
"""
    options3 = (
    r"""
[embed] Embeds powershell code in a batch file. (they run bat file but it reruns as ps1/powershell)
[exe] Simple Bat2Exe with self extracting zip (usually low detections too)
[exe2] Second method for Bat2Exe (usually low detections but may increase over time)
[COMING SOON] [exe3] Third method for Bat2Exe (100% fud)
[ONELINE] I did it
[exe2bat] Converts exe to bat (EXPERIMENTAL) (NOTE THIS IS NOT A DECOMPILER. IT EMBEDS THE EXE IN THE BAT FILE)
[py2bat] Converts python file to bat (Note you cant use things like getting the execution path cause that might break but idk ur choice)

[?] (If you want to use built in variables such as %~dp0 etc wrap them in percent signes then run the clean mode afterwards. You DONT have to do this if your using ultimate)
"""
    + "\n\n"
)
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Vertical(Colors.purple_to_blue, banner, 2))
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
    #GET FILE
    print(Colorate.Vertical(Colors.purple_to_blue, options1, 2))
    print(Colorate.Vertical(Colors.green_to_blue, options2, 2))
    print(Colorate.Vertical(Colors.purple_to_blue, options3, 2))