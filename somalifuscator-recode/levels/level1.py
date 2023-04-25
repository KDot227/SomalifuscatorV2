import os, string

from util.common import make_random_string
from util.cesar import caesar_cipher_rotation, caesar_cipher_rotation_UPPER

from rich.progress import track

class level1:
    def __init__(self, file, code_new) -> None:
        self.file = file
        self.code_new = code_new
        self.main()
    
    def main(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level1.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
            data = f.readlines()
        with open(
            f"{self.file}.level1.bat", "a+", encoding="utf-8", errors="ignore"
        ) as f:
            f.write(self.code_new)
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
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = caesar_cipher_rotation(char)
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random}%")
                                else:
                                    coded0 = caesar_cipher_rotation_UPPER(char)
                                    coded = coded0.replace(coded0, f"%{coded0}1%")
                                    f.write(f"{coded}%{random}%")
                            else:
                                f.write(f"{char}%{random}%")