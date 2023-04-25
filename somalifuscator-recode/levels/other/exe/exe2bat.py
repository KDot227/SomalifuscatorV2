import os, time, subprocess

from levels.ultimate import ultimate

from pystyle import *


class exe2bat:
    def __init__(self, file, *args, **kwargs) -> None:
        self.file = file
        self.main()

    def main(self):
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
            os._exit(1)
        to_subprocess = f"powershell.exe -C \"$base64 = [System.Convert]::ToBase64String([System.IO.File]::ReadAllBytes('{self.exe_path}')); $base64 | Out-File -Encoding ASCII -FilePath 'test.txt' -NoNewline\""
        subprocess.run(to_subprocess)
        with open("test.txt", "rb") as f:
            data = f.read()
        with open("mixer.bat", "w") as f:
            f.write(code)
        self.file = "mixer.bat"
        ultimate.Ultimate(utf_16=False, check_bypass=True)
        with open("mixer.bat.ultimate.bat", "rb") as f:
            insides = f.read()
        os.remove("mixer.bat.ultimate.bat")
        with open("mixer.bat.ultimate.bat", "wb") as f:
            f.write(insides + b"\n" + data)
        os.remove("test.txt")
        os.remove("mixer.bat")
        os.rename("mixer.bat.ultimate.bat", "bat2exe.bat")
