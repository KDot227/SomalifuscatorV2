import os
from rich.progress import track

from util.common import random_capitalization, make_random_string


def Fud(file, down) -> bool:
    carrot = False
    var = False
    try:
        os.remove(f"{file}.fud.bat")
    except:
        pass
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        data = f.readlines()
    with open(f"{file}.fud.bat", "a+", encoding="utf-8", errors="ignore") as f:
        f.write(random_capitalization("::Made by K.Dot and Godfather\n"))
        # this is so I don't have to see the status bar when using mixer
        if down == False:
            for line in data:
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)
                        elif var == True:
                            f.write(char)
                        elif "\n" in char:
                            f.write(char)
                        else:
                            random = make_random_string()
                            f.write(f"{char}%{random}%")
        else:
            for line in track(
                data, description="[bold green]Obfuscating", total=len(data)
            ):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)
                        elif var == True:
                            f.write(char)
                        elif "\n" in char:
                            f.write(char)
                        else:
                            random = make_random_string()
                            f.write(f"{char}%{random}%")
    down = not down
    return down