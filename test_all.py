import os
import glob
import time
import difflib
import subprocess

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("File Name")
table.add_column("Level")
table.add_column("Difference")

directory = f"{os.getcwd()}\\tests"
python_file = f"{os.getcwd()}\\src\\main.py"

# the default cmd.exe has different env vars than a normal bat file so we need to account to that.
env_vars = {
    "PATHEXT": ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC",
    "PUBLIC": r"C:\Users\Public",
    "COMMONPROGRAMFILES(X86)": r"C:\Program Files (x86)\Common Files",
    "PROGRAMFILES": r"C:\Program Files",
    "PROGRAMFILES(X86)": r"C:\Program Files (x86)",
    "DRIVERDATA": r"C:\Windows\System32\Drivers\DriverData",
    "COMMONPROGRAMFILES": r"C:\Program Files\Common Files",
    "COMMONPROGRAMW6432": r"C:\Program Files\Common Files",
    "COMMONPROGRAMFILES(X86)": r"C:\Program Files (x86)\Common Files",
}

# using this we take the current env vars and update them with the ones we need. (so we also get the good ones that normally work for the user too)
custom_env = os.environ.copy()
custom_env.update(env_vars)

menu = """
1.) Delete all obfuscated files
2.) Obfuscate all files
3.) Run all tests
4.) Delete all obfuscated files in ALL test directories
"""


class RunAll:
    """
    A class that provides methods to delete all files, test all files, check output and run full test sequence.
    This is important because it allows us more control over using somalifuscator over multiple files and cleanup.
    If obfuscated bat files that aren't test files aren't working for you please check to see if these are also all obfuscated correctly.
    If they are please contact K.Dot or Godfather and let them know. Otherwise try changing your code around to make it more simple.
    """

    def __init__(self, *args, **kwargs) -> None:
        choice = input("What would you like to do?\n" + menu + "\n> ")
        choice_list = {
            "1": self.delete_all,
            "2": self.test_all,
            "3": self.full_test_sequence,
            "4": self.delete_all,
        }

        args1 = True if choice == "4" else False

        choice_list[choice](args1)

        return

    def delete_all(self, rec: bool = False, *args, **kwargs) -> None:
        """
        A method that deletes all files with .bat extension in the directory.

        Args:
        - rec (bool): A boolean value that indicates whether to delete files recursively or not. Default is False.

        Returns:
        - None
        """
        remove_endings = ["_obf.bat", ".rar"]
        for root, dirs, files in os.walk(directory, topdown=rec):
            for file in files:
                if any([file.endswith(x) for x in remove_endings]):
                    os.remove(os.path.join(root, file))
        return

    def test_all(self, *args, **kwargs) -> None:
        """
        A method that tests all files with .bat extension in the directory.

        Args:
        - None

        Returns:
        - None
        """
        for file in glob.glob(f"{directory}\\*.bat"):
            os.system(f"python {python_file} -f {file}")
        return

    def check_output(self, file_path, new_file_path, *args, **kwargs):
        """
        A method that checks the output of the file.

        Args:
        - file_path (str): A string that represents the path of the file.
        - new_file_path (str): A string that represents the path of the new file.

        Returns:
        - None
        """
        command1 = f"{file_path} > output1.txt"
        command2 = f"{new_file_path} > output2.txt"

        t1 = subprocess.Popen(command1, shell=True, env=custom_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        t2 = subprocess.Popen(command2, shell=True, env=custom_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # wait for process to finish
        _, _ = t1.communicate()
        _, _ = t2.communicate()

        with open("output1.txt", "r", encoding="utf8") as f:
            a = [line.rstrip("\n") for line in f]
        with open("output2.txt", "r", encoding="utf8") as f:
            b = [line.rstrip("\n") for line in f]  # Remove leading space from each line

        # remove trailing spaces from a and b
        a = [line.strip() for line in a]
        b = [line.strip() for line in b]

        differ = difflib.unified_diff(a, b, lineterm="", n=3)
        differences = list(differ)

        if not differences:
            table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
        else:
            differences = "\n".join(differences)
            table.add_row(file_path, "[red]Obfuscated Incorrectly[/red]", differences)
            input()

        os.remove("output1.txt")
        os.remove("output2.txt")

        return

    def full_test_sequence(self, *args, **kwargs) -> None:
        """
        A method that runs the full test sequence.

        Args:
        - None

        Returns:
        - None
        """
        os.system("cls")
        with Live(table, refresh_per_second=4) as live:
            location = f"{os.getcwd()}\\tests\\tests_full\\*.bat"
            files = glob.glob(location, recursive=True)
            for file in files:
                file_path = os.path.join(os.getcwd(), file)
                if file.endswith("_obf.bat"):
                    try:
                        os.remove(file_path)
                    except FileNotFoundError:
                        pass
                    continue
                # we need to put .communicate() at the end or it will continue with the code instead of waiting until it finishes.
                subprocess.Popen(f"python {python_file} -f {file_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

                new_file_path = file_path.replace(".bat", "_obf.bat")

                self.check_output(file_path, new_file_path)

                try:
                    os.remove(new_file_path)
                except FileNotFoundError:
                    pass

        try:
            os.remove("output1.txt")
            os.remove("output2.txt")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    while True:
        RunAll()
        input("Press any key to continue...")
        os.system("cls")
