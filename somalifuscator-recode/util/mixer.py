from levels.other.fud import Fud
import os


def mixer(code, file, down):
    original_file = file
    with open("mixer.bat", "w") as f:
        f.write(code)
    file = "mixer.bat"
    down = Fud(file=file, down=down)
    with open("mixer.bat.fud.bat", "r", encoding="utf-8", errors="ignore") as f:
        code_new = f.read()
    os.remove("mixer.bat")
    os.remove("mixer.bat.fud.bat")
    file = original_file
    return code_new
