import os
import glob
import subprocess

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("File Name")
table.add_column("Level")

obfuscator_path = os.path.join(os.getcwd(), "src", "main.py")

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


def check_output(file_path, new_file_path):
    # out = subprocess.Popen(f"{file_location}", shell=True, env=custom_env).communicate()
    command1 = f"{file_path}"
    command2 = f"{new_file_path}"

    out_old = subprocess.Popen(command1, shell=True, env=custom_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out_new = subprocess.Popen(command2, shell=True, env=custom_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    exit_code_old = out_old.returncode
    exit_code_new = out_new.returncode

    if exit_code_old == exit_code_new:
        table.add_row(file_path, "[green]Obfuscated Correctly[/green]")
    else:
        table.add_row(file_path, "[red]Error[/red]")
    return


with Live(table, refresh_per_second=4) as live:  # update 4 times a second to feel fluid
    location = f"{os.getcwd()}\\tests\\tests_full\\*.bat"
    files = glob.glob(location, recursive=True)
    for file in files:
        os.system("cls")
        file_path = os.path.join(os.getcwd(), file)
        if file.endswith("_obf.bat"):
            os.remove(file_path)
            continue
        os.system(f"python {obfuscator_path} -f {file_path}")

        new_file_path = file_path.replace(".bat", "_obf.bat")

        check_output(file_path, new_file_path)

        os.remove(new_file_path)
