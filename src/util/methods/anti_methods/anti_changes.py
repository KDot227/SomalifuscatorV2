import random


from util.methods.common.common import make_random_string
from util.obfuscation.obf_oneline import Obfuscate_Single
from util.supporting.settings import all_

checked = False


class AntiChanges:
    @staticmethod
    def first_line_echo_check(c_check: bool = True, *args, **kwargs) -> str:
        """
        This function checks to see 2 things.
        1.) Is the user running with double click
        2.) Do echo commands exist in the file.

        If either of these are true it will exit the file.
        """
        random_bat_name = make_random_string((5, 6), False)
        if all_.debug or not c_check:
            return "\n"
        if all_.super_obf:
            command = f"""echo @echo off >> kdot{random_bat_name}.bat && echo findstr /i "echo" "%~f0" >> kdot{random_bat_name}.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> kdot{random_bat_name}.bat && call kdot{random_bat_name}.bat\n""" + "\n"
        else:
            command = f"""net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q kdot{random_bat_name}.bat >nul 2>&1 & exit )\necho @echo off >> kdot{random_bat_name}.bat && echo findstr /i "echo" "%~f0" >> kdot{random_bat_name}.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> kdot{random_bat_name}.bat && call kdot{random_bat_name}.bat\n""" + "\n"

        other_command = 'echo %cmdcmdline% | find /i "%~f0">nul || exit /b 1\n'

        return other_command + command

    @staticmethod
    def byte_check(*args, **kwargs) -> str:
        choices = [
            """powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$bytes = [System.IO.File]::ReadAllBytes('%~f0') ; if (($bytes[0] -ne 0xFF) -or ($bytes[1] -ne 0xFE) -or ($bytes[2] -ne 0x26)) { Write-Host 'The first 3 bytes of the file are not FF FE 0A.' ; taskkill /F /IM cmd.exe }\"""",
        ]

        choice = random.choice(choices)
        return choice

    @staticmethod
    def vm_test(*args, **kwargs):
        codes = [
            # r"""for /f "tokens=2 delims==" %%a in ('wmic computersystem get manufacturer /value') do set manufacturer=%%a\nfor /f "tokens=2 delims==" %%a in ('wmic computersystem get model /value') do set model=%%a\nif "%manufacturer%"=="Microsoft Corporation" if "%model%"=="Virtual Machine" exit\nif "%manufacturer%"=="VMware, Inc." exit\nif "%model%"=="VirtualBox" exit""",
            # r"""for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "Total Physical Memory"') do ( set available_memory=%%a ) & set available_memory=%available_memory: =% & set available_memory=%available_memory:M=% & set available_memory=%available_memory:B=% & set /a available_memory=%available_memory% / 1024 / 1024 & if not %available_memory% gtr 4 ( exit /b 1 )""",
            # I love batch so much I gave up and used powershell
            """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$VM=Get-WmiObject -Class Win32_ComputerSystem ; if ($VM.Model -match 'Virtual') { Write-Host 'Virtual Machine Detected. Exiting script.' ; taskkill /F /IM cmd.exe }\""""
            # """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "$tr=(Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory / 1KB ; $trgb=[math]::Round($tr / 1024, 2) ; if ($trgb -lt 8) { Write-Host 'Less than 8gb ram exiting' ; pause }\""""
        ]
        # ill add more one day
        return random.choice(codes)

    @staticmethod
    def anti_wifi(*args, **kwargs) -> str:
        if all_.require_wifi:
            return 'ping -n 2 -w 700 www.google.com | find "bytes=" > nul || exit'
        return ""

    @staticmethod
    def tests(*args, **kwargs):
        choices = [
            AntiChanges.vm_test,
            AntiChanges.first_line_echo_check,
        ]

        if all_.require_wifi:
            choices.append(AntiChanges.anti_wifi)
        # if all_.utf_16_bom:
        #    choices.append(AntiChanges.byte_check)

        return random.choice(choices)(False)

    @staticmethod
    def ads_spammer(code: list, *args, **kwargs) -> list:
        ads_points = {}
        for index, line in enumerate(code):
            random_chance = random.randint(1, 10)
            if random_chance == 1:
                # replace the line with a ads method that points towards its own scramble
                line.replace("|", "^|").replace(">", "^>").replace("<", "^<").replace("&", "^&").replace("%", "%%")
                random_point = make_random_string((5, 6), False)
                while random_point in ads_points:
                    random_point = make_random_string((5, 6), False)
                command = f"%TO_SCRAMBLE_PLZ%{Obfuscate_Single('echo').out()} {line} > %~f0:{random_point}\n"
                random_letter = make_random_string((1, 1), False)
                out_command = f'%TO_SCRAMBLE_PLZ%for /f "usebackq delims=φ" %%{random_letter} in (%~f0:{random_point}) do %%{random_letter}\n'

                # command = Obfuscate_Single(command, simple=False).out()
                # out_command = Obfuscate_Single(out_command, simple=False).out()

                together = command + out_command

                print(together)

                # replace the current line of code with this and rewrite it
                code[index] = together
        return code

    @staticmethod
    def anti_edit(*args, **kwargs):
        pass
