import os
import requests
from zipfile import ZipFile


class level5:
    def __init__(self, file, *args, **kwargs) -> None:
        super().__init__()
        self.file = file
        self.main()

    def main(self):
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
