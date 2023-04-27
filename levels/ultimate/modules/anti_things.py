import os, random, inspect

from util.settings import *
from levels.ultimate.modules.gen_obf import obf_oneline


def anti_check_error(code):
    """This just checks to see if the first byte of the file is the utf-16 BOM. If it is then it clears screen otherwise it exits."""
    strung = ">nul 2>&1 && exit >nul 2>&1 || cls \n@echo off\n"
    strung = obf_oneline(strung)
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


def tests(level):
    # I just made this cause editing it the other way would be annoying
    choices = [first_line_echo_check()]
    if anti_vm:
        choices.append(vm_test())

    if utf_16_bom and not level == "exe2bat":
        choices.append(byte_check())

    if debug:
        choices = [first_line_echo_check()]
    return choices


def vm_test():
    codes = [
        # r"""for /f "tokens=2 delims==" %%a in ('wmic computersystem get manufacturer /value') do set manufacturer=%%a\nfor /f "tokens=2 delims==" %%a in ('wmic computersystem get model /value') do set model=%%a\nif "%manufacturer%"=="Microsoft Corporation" if "%model%"=="Virtual Machine" exit\nif "%manufacturer%"=="VMware, Inc." exit\nif "%model%"=="VirtualBox" exit""",
        # r"""for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "Total Physical Memory"') do ( set available_memory=%%a ) & set available_memory=%available_memory: =% & set available_memory=%available_memory:M=% & set available_memory=%available_memory:B=% & set /a available_memory=%available_memory% / 1024 / 1024 & if not %available_memory% gtr 4 ( exit /b 1 )""",
        # I love batch so much I gave up and used powershell
        """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$VM=Get-WmiObject -Class Win32_ComputerSystem ; if ($VM.Model -match 'Virtual') { Write-Host 'Virtual Machine Detected. Exiting script.' ; taskkill /F /IM cmd.exe }\""""
        # """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "$tr=(Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory / 1KB ; $trgb=[math]::Round($tr / 1024, 2) ; if ($trgb -lt 8) { Write-Host 'Less than 8gb ram exiting' ; pause }\""""
    ]
    # ill add more one day
    return obf_oneline(random.choice(codes))


def byte_check():
    # choices = [
    #    """powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$bytes = [System.IO.File]::ReadAllBytes('%~f0') ; if (($bytes[0] -ne 0xFF) -or ($bytes[1] -ne 0xFE) -or ($bytes[2] -ne 0x26)) { Write-Host 'The first 3 bytes of the file are not FF FE 0A.' ; taskkill /F /IM cmd.exe }\"""",
    # ]
    # return obf_oneline(random.choice(choices))
    return ""


def first_line_echo_check():
    if not echo_check:
        return "\n"
    """basically just checks the entire file for the word echo. If it finds it then it will kill the process. Also the no debug checks to see if the user is double clicking the file instead of running it through a different application"""
    # I hate people who echo
    checked123 = True
    # This is for when I run through vscode but I can't since it just finna close itself
    debug = False
    if not double_click_check:
        debug = True
    if debug:
        if checked123 == True:
            command = (
                r'echo @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( ( goto ) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                + "\n"
            )
            checked123 = False
            return command
        else:
            command = (
                r'echo @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( ( goto ) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                + "\n"
            )
            return command
    else:
        if checked123 == True:
            command = (
                """net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q close.bat >nul 2>&1 & exit )\necho @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                + "\n"
            )
            checked123 = False
            return command
        else:
            command = (
                """net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q close.bat >nul 2>&1 & exit )\necho @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                + "\n"
            )
            return command
