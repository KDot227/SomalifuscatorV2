import random


class CommandWrappers:
    """
    A class that contains methods for wrapping commands in various ways.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def main(command: str):
        """
        A method that randomly chooses one of the available command wrappers and applies it to the given command.

        Args:
            command (str): The command to wrap.

        Returns:
            str: The wrapped command.
        """
        chocies = [
            CommandWrappers.for_loop,
            CommandWrappers.outside_command,
            # CommandWrappers.var_command,
        ]

        return random.choice(chocies)(command)

    @staticmethod
    def for_loop(command: str):
        """
        A method that wraps the given command in a for loop.

        Args:
            command (str): The command to wrap.

        Returns:
            str: The wrapped command.
        """
        ran_num = random.randint(1, 100)
        loops = [
            f"for /l %%X in ( {ran_num} , {ran_num} , {ran_num} ) do ( {command} )",
        ]
        return random.choice(loops)

    @staticmethod
    def outside_command(command: str):
        """
        A method that wraps the given command in a block of code that runs before the command.

        Args:
            command (str): The command to wrap.

        Returns:
            str: The wrapped command.
        """
        commands = [
            # f"echo KDOT WAS HERE ^\nexit > nul\n{command}",
            f"if exist %temp% {command}",
            f"if exist %appdata% {command}",
        ]

        return random.choice(commands)

    @staticmethod
    def var_command(command: str):
        """
        A method that wraps the given command in an environment variable.

        Args:
            command (str): The command to wrap.

        Returns:
            str: The wrapped command.
        """
        public = r"C:\Users\Public"
        weird = r"C:\Program Files (x86)\Common Files"
        program_1 = r"C:\Program Files"
        program_2 = r"C:\Program Files (x86)"
        driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
        pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
        CommonProgramFiles = r"C:\Program Files\Common Files"
        CommonProgramFiles_x86 = r"C:\Program Files (x86)\Common Files"
        CommonProgramW6432 = r"C:\Program Files\Common Files"
        list_of_all = [
            public,
            weird,
            program_1,
            program_2,
            driver_stuff,
            pathext,
            CommonProgramFiles,
            CommonProgramFiles_x86,
            CommonProgramW6432,
        ]
        corosponding = [
            "PUBLIC",
            "COMMONPROGRAMFILES(X86)",
            "PROGRAMFILES",
            "PROGRAMFILES(X86)",
            "DRIVERDATA",
            "PATHEXT",
            "COMMONPROGRAMFILES",
            "COMMONPROGRAMFILES(X86)",
            "COMMONPROGRAMW6432",
        ]

        random_path = random.choice(corosponding)
        corosponding_index = corosponding.index(random_path)
        out = list_of_all[corosponding_index]
        valid_text = f"%{random_path}:{out}=%{command}"

        return valid_text
