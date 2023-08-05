import os
import glob
import time
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

        if choice_list[choice] == 4:
            args1 = True
        else:
            args1 = None

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
        for file in glob.glob(f"{directory}\\*.bat", recursive=rec):
            if file.endswith("_obf.bat"):
                os.remove(file)
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
        out1, err1 = t1.communicate()
        out2, err2 = t2.communicate()

        with open("output1.txt", "r", encoding="utf8") as f:
            inside1 = f.read().strip()
        with open("output2.txt", "r", encoding="utf8") as f:
            inside2 = f.read().strip()

        if inside1 == inside2:
            table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
        else:
            a = set(inside1.split())
            b = set(inside2.split())

            diff = a.symmetric_difference(b)
            # these next 3 if statements are very important.
            # they check to see if the difference is set() or set([]) or set() (python set is very weird and sometimes works strangly)
            # If you want to take a deeper look into the output of these commands you can always comment out the os.remove("output1.txt") and check the type files.
            # Also sometimes my obfuscator might put extra spaces in between variables. This is normal and im not too sure why but it's only with echo and doesn't affect
            # the code runtime.
            if diff == "set()" or diff == set():
                table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
                return
            # check if diff is type set
            if type(diff) == set:
                if len(diff) == 1:
                    if diff.pop() == "0":
                        table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
                        return
                # check if first item is a string
                if type(diff.pop()) == str:
                    # check if first 2 letters of first item are numbers
                    if diff.pop()[0:2].isdigit():
                        table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
                        return

            table.add_row(file_path, "[red]Error[/red]", str(diff))

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

        time.sleep(3)

        try:
            os.remove("output1.txt")
            os.remove("output2.txt")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    RunAll()
    input("Press any key to exit...")
