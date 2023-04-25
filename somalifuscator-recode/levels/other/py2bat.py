import time, os
from pystyle import *


class py2bat:
    def __init__(self) -> None:
        self.main()

    def py2bat(self):
        # https://stackoverflow.com/questions/4571244/creating-a-bat-file-for-python-script
        # I had another way of doing this but it was absolute dog compared to this method
        start_code = """
0<0# : ^
'''
@echo off
echo batch
python "%~f0" %*
exit /b 0
'''
"""
        python_code = Write.Input("Enter the path to the python file: ", Colors.green)
        if not os.path.isfile(python_code):
            print("File does not exist!")
            time.sleep(3)
            os._exit(1)
        with open(python_code, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
        with open("py2bat.bat", "w", encoding="utf-8", errors="ignore") as f:
            f.write(start_code + data)
