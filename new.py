from rich import *
from rich.progress import *

# read bat file and print the output with syntax highlighting

with open("test.bat", "r") as f:
    lines = f.readlines()
    # print lines with syntax highlighting
    for line in lines:
        print(line, end="")

input("Press Enter to continue...")
