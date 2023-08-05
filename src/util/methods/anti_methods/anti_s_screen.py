# anti smart screen module

import os
import subprocess

from util.methods.common.common import make_random_string


class AntiSScreen:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.winrar_path = "C:/Program Files/WinRAR"

    def check_winrar(self) -> bool:
        """Checks if WinRAR is installed.

        Returns:
            bool: True if WinRAR is installed, False otherwise.
        """
        if os.path.exists(f"{self.winrar_path}/WinRAR.exe"):
            return True
        else:
            return False

    def pack_file(self, rar_out: str) -> None:
        """If winrar is installed it will pack the file with a random password.
        This is important because in windows if a rar file is compressed with best and is password locked (encrypted) it will not be detected by smart screen.

        Args:
            rar_out str: Path to the rar file to be created.
        """
        if not self.check_winrar():
            print("WinRAR is not installed.")
            input("Press any key to exit...")
            return
        self.password = make_random_string(special_chars=False)
        subprocess.Popen(f"{self.winrar_path}/WinRAR.exe a -ep -p{self.password} -m5 {rar_out} {self.file_path}", stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
        print(f"\nIMPORTANT\nPassword (SAVE): {self.password}\nIMPORTANT\n")
        return
