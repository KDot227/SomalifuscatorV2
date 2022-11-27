from random import randint
import random, codecs, string, os, time

try:
    from pystyle import *
except:
    os.system("python -m pip install pystyle")
    from pystyle import *

try:
    from tqdm import tqdm
except:
    os.system("python -m pip install tqdm")
    from tqdm import tqdm

try:
    import colorama
except ImportError:
    os.system("python -m pip install colorama")
    import colorama
colorama.deinit()

__author__ = 'K.Dot#0001'

#this is just the rot13 code and echo off. U can deobf if u want idc
code = r"""
@echo off
set "n=a" && set "o=b" && set "p=c" && set "q=d" && set "r=e" && set "s=f" && set "t=g" && set "u=h" && set "v=i" && set "w=j" && set "x=k" && set "y=l" && set "z=m" && set "a=n" && set "b=o" && set "c=p" && set "d=q" && set "e=r" && set "f=s" && set "g=t" && set "h=u" && set "i=v" && set "j=w" && set "k=x" && set "l=y" && set "m=z" && set "N1=A" && set "O1=B" && set "P1=C" && set "Q1=D" && set "R1=E" && set "S1=F" && set "T1=G" && set "U1=H" && set "V1=I" && set "W1=J" && set "X1=K" && set "Y1=L" && set "Z1=M" && set "A1=N" && set "B1=O" && set "C1=P" && set "D1=Q" && set "E1=R" && set "F1=S" && set "G1=T" && set "H1=U" && set "I1=V" && set "J1=W" && set "K1=X" && set "L1=Y" && set "M1=Z"
"""
if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    os._exit(0)
banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001\n\n
""")

options = """
[1] Level 1 (Recommended to use AFTER 2)
[2] Level 2
[3] Level 3
[clean] cleans the code to try and fix any common errors
[all] does 1, 2, 3 and clean
[fud] makes it undetectable by everything on virustotal
"""
 
print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))

class Main:
    def __init__(self):
        self.carrot = False
        self.label = False
        self.file = input("File: ")
        if os.path.exists(self.file):
            print(options)
            self.level = input("What level of obfuscation do you want? -> ")
            if self.level == "1":
                self.level1()
            elif self.level == "2":
                self.level2()
            elif self.level == "3":
                self.level3()
            elif self.level == "clean":
                self.clean()
            elif self.level == "all":
                self.all()
            elif self.level == "fud":
                self.fud()
            else:
                print("Invalid option")
                time.sleep(3)
                Main()
        else:
            print("That file does not exist!")
            time.sleep(3)
            Main()
            
    def make_random_string(self):
        length = randint(5, 8)
        return ''.join(random.choice(string.ascii_letters) for i in range(length))
            
    def level1(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level1.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level1.bat", "a+", encoding="utf-8") as f:
            f.write(code)
            for line in data:
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
                            random = self.make_random_string()
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = codecs.encode(char, 'rot_13')
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random}%")
                                else:
                                    coded0 = codecs.encode(char, 'rot_13').upper()
                                    coded = coded0.replace(coded0, f'%{coded0}1%')
                                    f.write(f"{coded}%{random}%")
                            else:
                                f.write(f"{char}%{random}%")
                                
    def level2(self):
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        random_order = ''.join(random.sample(characters, len(characters)))
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level2.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level2.bat", "a+", encoding="utf-8") as f:
            f.write(f"set KDOT={random_order}\n")
            for line in data:
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
                                var = f"%KDOT:~{random_order.index(char)},1%"
                                f.write(var)
                            else:
                                f.write(char)
                                
    def level3(self):
        out_hex = []

        #lowkey overkill lmao
        out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
        with open(f'{self.file}','rb') as f:
                penis = f.read()

        out_hex.extend(['{:02X}'.format(b) for b in penis])

        with open(f'{self.file}.level3.bat', 'wb') as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))
                
    def clean(self):
        with open(self.file, 'r') as f:
            contents = f.read()
        with open(f'{self.file}.cleaned.bat', 'a+') as f:
            contents.replace("%~f0%", "%~f0")
            contents.replace("%~dp0%", "%~dp0")
            contents.replace("%~dpn0%", "%~dpn0")
            f.write(contents)
            
    def all(self):
        names = []
        self.level1()
        self.file = f"{self.file}.level1.bat"
        names.append(self.file)
        self.level2()
        self.file = f"{self.file}.level2.bat"
        names.append(self.file)
        self.clean()
        self.file = f"{self.file}.cleaned.bat"
        names.append(self.file)
        self.level3()
        os.rename(f"{self.file}.level3.bat", "FINAL.bat")
        for name in names:
            os.remove(name)
        print("FINAL.bat is the finished product!")
        time.sleep(5)
        os._exit(0)
        
    def fud(self):
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.fud.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.fud.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot\n")
            for line in data:
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
                            random = self.make_random_string()
                            f.write(f"{char}%{random}%")                        

if __name__ == "__main__":
    Main()
