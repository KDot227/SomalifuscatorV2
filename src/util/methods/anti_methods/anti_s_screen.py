# anti smart screen module

import os
import subprocess

from util.methods.common.common import make_random_string


class AntiSScreen:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.winrar_path = "C:/Program Files/WinRAR"

    def check_winrar(self) -> bool:
        if os.path.exists(f"{self.winrar_path}/WinRAR.exe"):
            return True
        else:
            return False

    def pack_file(self, rar_out) -> None:
        if not self.check_winrar():
            print("WinRAR is not installed.")
            input("Press any key to exit...")
            return
        self.password = make_random_string(special_chars=False)
        subprocess.Popen(f"{self.winrar_path}/WinRAR.exe a -ep -p{self.password} -m5 {rar_out} {self.file_path}", stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
        print(f"\nIMPORTANT\nPassword (SAVE): {self.password}\nIMPORTANT\n")
        return
