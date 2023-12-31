import os
import sys
import glob
import difflib
import subprocess

from rich.live import Live
from rich.table import Table
from concurrent.futures import ThreadPoolExecutor, as_completed

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


class RunAll:
    def __init__(self) -> None:
        self.failed = False

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
        subprocess.Popen(f"python {python_file} -f {file_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

        command1 = f"{file_path} > {file_path}.txt"
        command2 = f"{new_file_path} > {new_file_path}.txt"

        t1 = subprocess.Popen(command1, shell=True, env=custom_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        t2 = None

        try:
            t2 = subprocess.Popen(command2, shell=True, env=custom_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # wait for process to finish
            _, _ = t1.communicate()
            _, _ = t2.communicate()

            with open(f"{file_path}.txt", "r", encoding="utf8") as f:
                a = [line.rstrip("\n") for line in f]
            with open(f"{new_file_path}.txt", "r", encoding="utf8") as f:
                b = [line.rstrip("\n") for line in f]  # Remove leading space from each line

            # remove trailing spaces from a and b
            a = [line.strip() for line in a]
            b = [line.strip() for line in b]

            differ = difflib.unified_diff(a, b, lineterm="", n=3)
            differences = list(differ)

            if not differences:
                table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
            else:
                self.failed = True
                differences = "\n".join(differences)
                table.add_row(file_path, "[red]Obfuscated Incorrectly[/red]", differences)
                # table.add_row(file_path, "[red]Obfuscated Incorrectly[/red]", "N/A")

        except Exception as e:
            self.failed = True
            table.add_row(file_path, "[red]Obfuscated Incorrectly[/red]", "Error occurred during execution")

        finally:
            if t2 is not None and t2.poll() is None:
                t2.kill()

            os.remove(f"{file_path}.txt")
            os.remove(f"{new_file_path}.txt")

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
        self.remove_all_obf_files()
        with Live(table, refresh_per_second=4) as live:
            location = f"{os.getcwd()}\\tests\\tests_full\\*.bat"
            files = glob.glob(location, recursive=True)
            threads = []
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.controller, file) for file in files]
                for future in as_completed(futures):
                    threads.append(future.result())

        return self.failed

    def remove_all_obf_files(self, *args, **kwargs) -> None:
        """
        A method that removes all obf files.

        Args:
        - None

        Returns:
        - None
        """
        for file in glob.glob(f"{directory}\\tests_full\\*.bat"):
            if file.endswith("_obf.bat"):
                print(file)
                os.remove(file)
        for file in glob.glob(f"{directory}\\tests_full\\*.txt"):
            if file.endswith(".bat.txt"):
                print(file)
                os.remove(file)
        return

    def controller(self, file):
        file_path = os.path.join(os.getcwd(), file)
        if file.endswith("_obf.bat"):
            try:
                os.remove(file_path)
            except FileNotFoundError:
                pass
            return

        new_file_path = file_path.replace(".bat", "_obf.bat")

        self.check_output(file_path, new_file_path)

        try:
            os.remove(new_file_path)
        except FileNotFoundError:
            pass

        return


def test_everything():
    """
    A method that tests everything.

    Args:
    - None

    Returns:
    - None
    """
    new = RunAll()
    assert new.full_test_sequence() == False


if __name__ == "__main__":
    new = RunAll()
    if new.full_test_sequence():
        print("Failed")
    else:
        print("Passed")
