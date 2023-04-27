import random, os, string
from rich.progress import track


class level2:
    def __init__(self, file, *args, **kwargs) -> None:
        super().__init__()
        self.file = file
        self.main()

    def main(self):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level2.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
            data = f.readlines()
        with open(
            f"{self.file}.level2.bat", "a+", encoding="utf-8", errors="ignore"
        ) as f:
            f.write(f"set KDOT={random_order}\nchcp 65001 > nul\n")
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
                            if char in string.ascii_letters:
                                vard = f"%KDOT:~{random_order.index(char)},1%"
                                f.write(vard)
                            else:
                                f.write(char)
