import os, time
import requests
from pystyle import *


class bat2exe2:
    def __init__(self) -> None:
        self.main()

    def main(self) -> None:
        warning = Write.Input(
            "WARNING: This method requires you to download a exe file from the github repo and run it. Are you ok with this? (y/n): ",
            Colors.green,
            interval=0.05,
        )
        if warning.lower() == "n":
            time.sleep(3)
            os._exit(1)
        else:
            r = requests.get(
                "https://github.com/KDot227/Somalifuscator/releases/download/Bat2Exe_Method1/Bat2Exe.exe"
            )
            with open("Bat2Exe.exe", "wb") as f:
                f.write(r.content)
            os.system("start Bat2Exe.exe")
            time.sleep(3)
