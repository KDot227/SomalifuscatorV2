import os
import glob
import time
import subprocess
from rich.live import Live
from rich.table import Table

class FileManager:
    def __init__(self, directory):
        self.directory = directory

    def delete_files(self, remove_endings, recursive=False):
        for root, _, files in os.walk(self.directory, topdown=recursive):
            for file in files:
                if any(file.endswith(x) for x in remove_endings):
                    os.remove(os.path.join(root, file))

    def test_files(self, python_file):
        for file in glob.glob(os.path.join(self.directory, "*.bat")):
            os.system(f"python {python_file} -f {file}")

class OutputChecker:
    def __init__(self, custom_env):
        self.custom_env = custom_env
        self.table = self.initialize_table()

    @staticmethod
    def initialize_table():
        table = Table()
        table.add_column("File Name")
        table.add_column("Level")
        table.add_column("Difference")
        return table

    def check_output(self, file_path, new_file_path):
        result1 = subprocess.run(f"{file_path} > output1.txt", shell=True, env=self.custom_env, capture_output=True)
        result2 = subprocess.run(f"{new_file_path} > output2.txt", shell=True, env=self.custom_env, capture_output=True)

        inside1 = self.read_file("output1.txt")
        inside2 = self.read_file("output2.txt")

        self.safe_file_removal("output1.txt")
        self.safe_file_removal("output2.txt")

        self.compare_outputs(inside1, inside2, file_path)

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r", encoding="utf8") as f:
            return f.read().strip()

    def compare_outputs(self, inside1, inside2, file_path):
        if inside1 == inside2:
            self.table.add_row(file_path, "[green]Obfuscated Correctly[/green]", "NONE")
        else:
            diff = set(inside1.split()) ^ set(inside2.split())
            self.table.add_row(file_path, "[red]Error[/red]", str(diff))

    @staticmethod
    def safe_file_removal(file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass

class RunAll:
    def __init__(self):
        self.directory = os.path.join(os.getcwd(), 'tests')
        self.python_file = os.path.join(os.getcwd(), 'src', 'main.py')
        self.custom_env = self.get_custom_env()
        self.file_manager = FileManager(self.directory)
        self.output_checker = OutputChecker(self.custom_env)

    @staticmethod
    def get_custom_env():
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
        custom_env = os.environ.copy()
        custom_env.update(env_vars)
        return custom_env

    def menu(self):
        menu_options = """
        1.) Delete all obfuscated files
        2.) Obfuscate all files
        3.) Run all tests
        4.) Delete all obfuscated files in ALL test directories
        """
        choice = input("What would you like to do?\n" + menu_options + "\n> ")
        choice_list = {
            "1": lambda: self.file_manager.delete_files(["_obf.bat", ".rar"]),
            "2": lambda: self.file_manager.test_files(self.python_file),
            "3": self.full_test_sequence,
            "4": lambda: self.file_manager.delete_files(["_obf.bat", ".rar"], recursive=True),
        }
        if choice in choice_list:
            choice_list[choice]()

    def full_test_sequence(self):
        with Live(self.output_checker.table, refresh_per_second=4) as live:
            files = glob.glob(os.path.join(self.directory, 'tests_full', "*.bat"), recursive=True)
            for file in files:
                file_path = os.path.join(os.getcwd(), file)
                if file.endswith("_obf.bat"):
                    self.output_checker.safe_file_removal(file_path)
                    continue

                subprocess.run(f"python {self.python_file} -f {file_path}", shell=True, capture_output=True)
                new_file_path = file_path.replace(".bat", "_obf.bat")
                self.output_checker.check_output(file_path, new_file_path)
                self.output_checker.safe_file_removal(new_file_path)

        time.sleep(3)
        self.output_checker.safe_file_removal("output1.txt")
        self.output_checker.safe_file_removal("output2.txt")

if __name__ == "__main__":
    run_all = RunAll()
    while True:
        run_all.menu()
        input("Press any key to continue...")
        os.system("cls")
