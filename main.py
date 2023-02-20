import time
import os

try:
    from rich.progress import track
    from zipfile import ZipFile
    from random import randint
    from pystyle import *
    import colorama
    import requests
    import random
    import codecs
    import string
except:
    print(
        "You don't have the required modules installed. Please run the setup.bat file to fix this."
    )
    time.sleep(5)
    os._exit(1)

colorama.deinit()

__author__ = "K.Dot#0001"

cesar_val = randint(1, 13)


def caesar_cipher_rotations(rotation):
    """Generates the Caesar cipher for a given rotation value."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


def caesar_cipher_rotations_upper(rotation):
    """Generates the Caesar cipher for a given rotation value."""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}1={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(cesar_val)
together = together[:-4]


code = f"""@echo off
{together}
chcp 65001 > nul
"""
if __author__ != "\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31":
    os._exit(0)
banner = Center.XCenter(
    """
███████╗ ██████╗ ███╗   ███╗ █████╗ ██╗     ██╗███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██║██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║   ██║██╔████╔██║███████║██║     ██║█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║   ██║██║╚██╔╝██║██╔══██║██║     ██║██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 Made by Godfather and K.Dot#4044\n\n
"""
)

options = (
    r"""
[1] Level 1 (Recommended to use AFTER 2)
[2] Level 2
[3] Level 3
[4] Level 4 (NOTE: Don't end your files with exit when its done with this command or it might break. (same with pause))
[5] Level 5 (NOTE: THIS WAS NOT MADE BY ME IT WAS MADE BY https://www.dostips.com/forum/memberlist.php?mode=viewprofile&u=2258 W mans btw)
[clean] cleans the code to try and fix any common errors
[all] does 1, 2, 3 and clean
[fud] makes it undetectable by everything on virustotal
[ultimate] The Ultimate batch obfuscation (nowhere near done... but beta out now.)
[embed] Embeds powershell code in a batch file. (they run bat file but it reruns as ps1/powershell)
[exe] Simple Bat2Exe with self extracting zip (usually low detections too)
[exe2] Second method for Bat2Exe (usually low detections but may increase over time)
[COMING SOON] [exe3] Third method for Bat2Exe (100% fud)

[?] (If you want to use built in variables such as %~dp0 etc wrap them in percent signes then run the clean mode afterwards.)
"""
    + "\n\n"
)


class AutoUpdate:
    def __init__(self):
        self.code = (
            "https://raw.githubusercontent.com/KDot227/Somalifuscator/main/main.py"
        )
        self.bypass = False
        username = os.getlogin()
        if username == "this1":
            self.bypass = True
        self.update()

    def update(self):
        if not self.bypass:
            print("Checking for updates...")
            code = requests.get(self.code, timeout=10).text
            with open(__file__, "r", encoding="utf-8") as f:
                main_code = f.read()
            if code != main_code:
                print("Updating...")
                with open(__file__, "w", encoding="utf-8") as f:
                    f.write(code)
                os.startfile(__file__)
                os._exit(0)
            else:
                print("No updates found!")


class Main:
    def __init__(self):
        # if u on linux kys
        os.system("cls")
        print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))
        self.carrot = False
        self.label = False
        self.file = Write.Input("File to obfuscate -> ", Colors.rainbow, interval=0.05)
        if os.path.exists(self.file):
            print(Colorate.Vertical(Colors.yellow_to_red, options, 2))
            self.level = Write.Input(
                "What level of Obfuscation do you want? -> ",
                Colors.rainbow,
                interval=0.05,
            )
            self.level_dict = {
                "1": self.level1,
                "2": self.level2,
                "3": self.level3,
                "4": self.level4,
                "5": self.level5,
                "clean": self.clean,
                "all": self.all,
                "fud": self.fud,
                "ultimate": self.ultimate,
                "embed": self.embed,
                "exe": self.bat2exe,
                "exe2": self.bat2exe2,
            }

            pick = self.level_dict.get(self.level)
            if pick is not None:
                self.mixer()
                pick()
            else:
                print("Invalid option")
                time.sleep(3)
                Main()
        else:
            print(Colors.red + "That file does not exist!" + Colors.reset)
            time.sleep(3)
            Main()

    def make_random_string(self):
        length = randint(5, 8)
        return "".join(
            random.choice(
                # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            for i in range(length)
        )

    def caesar_cipher_rotation(self, letter):
        """Returns the Caesar cipher rotation for a given letter and rotation value."""
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        letter_index = alphabet.index(letter.lower())
        rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
        rotated_letter = rotated_alphabet[letter_index]

        return rotated_letter

    def caesar_cipher_rotation_UPPER(self, letter):
        """Returns the Caesar cipher rotation for a given letter and rotation value."""
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        letter_index = alphabet.index(letter.upper())
        rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
        rotated_letter = rotated_alphabet[letter_index]

        return rotated_letter

    def mixer(self):
        original_file = self.file
        with open("mixer.bat", "w") as f:
            f.write(code)
        self.file = "mixer.bat"
        self.fud()
        with open("mixer.bat.fud.bat", "r", encoding="utf-8") as f:
            self.code_new = f.read()
        os.remove("mixer.bat")
        os.remove("mixer.bat.fud.bat")
        self.file = original_file

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
                            random = self.make_random_string()
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = self.caesar_cipher_rotation(char)
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random}%")
                                else:
                                    coded0 = self.caesar_cipher_rotation_UPPER(char)
                                    coded = coded0.replace(coded0, f"%{coded0}1%")
                                    f.write(f"{coded}%{random}%")
                            else:
                                f.write(f"{char}%{random}%")

    def level2(self):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        carrot = False
        var = False
        try:
            os.remove(f"{self.file}.level2.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level2.bat", "a+", encoding="utf-8") as f:
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

    def level3(self):
        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(
            ["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"]
        )
        with open(f"{self.file}", "rb") as f:
            penis = f.read()

        out_hex.extend(["{:02X}".format(b) for b in penis])

        with open(f"{self.file}.level3.bat", "wb") as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))

    def clean(self):
        with open(self.file, "r", encoding="utf-8") as f:
            contents = f.read()
        with open(f"{self.file}.cleaned.bat", "a+", encoding="utf-8") as f:
            # if there are any others that people use please make a pr and add them.
            batch_vars = [
                "%~dp0",
                "%~f0",
                "%~n0",
                "%~x0",
                "%~dpnx0",
            ]
            batch_vars_to_replace = [
                r"%~dp0%",
                r"%~f0%",
                r"%~n0%",
                r"%~x0%",
                r"%~dpnx0%",
            ]
            for i in range(len(batch_vars)):
                contents = contents.replace(batch_vars_to_replace[i], batch_vars[i])
            f.write(contents)

    def all(self):
        names = []
        self.level2()
        self.file = f"{self.file}.level2.bat"
        names.append(self.file)
        self.level1()
        self.file = f"{self.file}.level1.bat"
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
                            random = self.make_random_string()
                            f.write(f"{char}%{random}%")

    def ultimate(self) -> None:
        # ultimate mode
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.ultimate.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot\n")
            f.write(self.code_new)
            characters = (
                "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            random_order = "".join(random.sample(characters, len(characters)))
            f.write(f"set KDOT={random_order}\n")
            for line in track(
                data, description="[bold green]Obfuscating", total=len(data)
            ):
                random_bool = random.choice([True, False])
                if line.startswith("::"):
                    f.write(line)
                    continue
                elif line.startswith(":"):
                    f.write(line)
                    continue
                else:
                    if random_bool == True:
                        f.write(";")
                    for word in line.split():
                        if word.startswith("%"):
                            f.write(word + " ")
                            continue
                        else:
                            for char in word:
                                if char == "\n":
                                    f.write("\n")
                                    continue
                                elif char == " ":
                                    f.write(" ")
                                    continue
                                else:
                                    # random_obf = [self.ran1(char), self.ran2(char, random_order), self.ran3(char), self.ran4(char)]
                                    # I'll fix this someday
                                    random_obf = [
                                        self.ran1(char),
                                        self.ran2(char, random_order),
                                        self.ran4(char),
                                    ]
                                    f.write(f"{random.choice(random_obf)}")
                            f.write(" ")
                    f.write("\n")
        with open(f"{self.file}.ultimate.bat", "r", encoding="utf-8") as f:
            data = f.readlines()
        messed_up = self.scrambler(data)
        with open(f"{self.file}.ultimate.bat", "w", encoding="utf-8") as f:
            for array in messed_up:
                for thing in array:
                    f.write(thing.strip() + "\n")

    def ran1(self, char):
        random = self.make_random_string()
        if char in string.ascii_letters:
            if char.islower():
                coded0 = codecs.encode(char, "rot_13")
                coded = coded0.replace(coded0, f"%{coded0}%")
                return f"{coded}%{random}%"
            else:
                coded0 = codecs.encode(char, "rot_13").upper()
                coded = coded0.replace(coded0, f"%{coded0}1%")
                return f"{coded}%{random}%"
        else:
            return f"{char}%{random}%"

    def ran2(self, char, random_order):
        public = r"C:\Users\Public"
        weird = r"C:\Program Files (x86)\Common Files"
        if char in public:
            return f"%public:~{public.index(char)},1%"
        elif char in weird:
            return f"%CommonProgramFiles(x86):~{weird.index(char)},1%"
        else:
            if char in string.ascii_letters:
                var = f"%KDOT:~{random_order.index(char)},1%"
                return var
            else:
                return char

    def ran3(self, char):
        if char in string.ascii_letters:
            escape = "^"
            return f"{escape}{char}"
        else:
            return char

    def ran4(self, char):
        return char

    def true_statement(self, line):
        true_statements = [
            "if exist C:\Windows\System32 ( {} )",
            "if not 0 neq 0 ( {} )",
        ]
        random_statement = random.choice(true_statements)
        return random_statement.format(line)

    def obliterate(self):
        # The best obfuscation method involving encoding
        # I ain't nowhere near done with this yet :skull:
        # (it does work tho stg | and its op asf)
        pass

    def embed(self):
        starting_code_normal = """<# :validbatch
@echo off
setlocal
cd /d "%~dp0"

echo K.Dot up

powershell.exe -ep Bypass -Command "IEX $([System.IO.File]::ReadAllText('%~f0'))"
goto :eof
#>"""
        starting_code_to_obf = """@echo off
setlocal
cd /d "{%~dp0}"

echo K.Dot up

powershell -ep Bypass -Command "IEX $([System.IO.File]::ReadAllText('{%~f0}'))"
goto :eof
"""
        ps1_file_location = Write.Input(
            "Enter the location of the ps1 file: ", Colors.rainbow, interval=0.05
        )
        try:
            with open(ps1_file_location, "r", encoding="utf-8") as f:
                data = f.readlines()
        except FileNotFoundError:
            print("File not found!")
            time.sleep(3)
            Main()
        obfuscate = Write.Input(
            "Would you like to obfuscate the batch code? (y/n): ",
            Colors.rainbow,
            interval=0.05,
        )
        if obfuscate.lower() == "y":
            with open("place_holder.bat", "w", encoding="utf-8") as f:
                f.write(starting_code_to_obf)
                self.file = "place_holder.bat"
            self.ultimate()
            os.remove("place_holder.bat")
            os.rename("place_holder.bat.ultimate.bat", "embed.bat")
            with open("embed.bat", "r+", encoding="utf-8") as f:
                data2 = f.readlines()
                data2_size = len(data2)
                data2.insert(0, "<# :validkdot\n")
                data2.insert(data2_size + 1, "#>\n")
                data2 += data
            with open("embed.bat", "w+", encoding="utf-8") as f:
                f.writelines(data2)
        else:
            # I can FASHO make this a lot cleaner and better but im too lazy rn (split string into list instead of reading it from file :skull:)
            with open("embed.bat", "w", encoding="utf-8") as f:
                f.write(starting_code_normal)
            with open("embed.bat", "r+", encoding="utf-8") as f:
                data2 = f.readlines()
            with open("embed.bat", "w", encoding="utf-8") as f:
                data2_size = len(data2)
                data2.insert(data2_size, "\n")
                data2 += data
                f.writelines(data2)

    def scrambler(self, codeed):
        # lowkey broken rn
        dead_code = Write.Input(
            "Would you like to add dead code? (y/n): ", Colors.rainbow, interval=0.05
        )
        if dead_code.lower() == "y":
            dead_code = True
        else:
            dead_code = False
        original_lines = codeed

        dict_thing = {}

        main_list = []

        for index, item in enumerate(original_lines):
            dict_thing[item] = [
                "".join(
                    random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(10)
                ),
                index,
            ]

        for index, (key, value) in enumerate(dict_thing.items()):
            if index == 0:
                remem = [f"goto {value[0]}\n"]
            part_1 = f":{value[0]}\n"
            part_2 = f"{key}\n"
            try:
                part_3 = f"goto {list(dict_thing.values())[value[1]+1][0]}\n"
            except IndexError:
                part_3 = f"goto :EOF\n"

            main_list.append([part_1, part_2, part_3])

        random.shuffle(main_list)
        main_list.insert(0, remem)

        if dead_code == True:
            low = random.randint(1, 3)
            medium = random.randint(4, 6)
            high = random.randint(7, 9)
            extreme = random.randint(10, 12)
            dead_code_examples = [
                "if not 0 == 0 goto :EOF\n",
                "if not exist C:\Windows\System32 goto :EOF\n",
                "if %penis% == 'yes' goto nah\n",
            ]

            type = Write.Input(
                "What type of dead code do you want? (low/medium/high/extreme): ",
                Colors.rainbow,
                interval=0.05,
            )
            if type.lower() == "low":
                for i in range(low):
                    main_list.insert(
                        random.randint(0, len(main_list)), dead_code_examples
                    )
            elif type.lower() == "medium":
                for i in range(medium):
                    main_list.insert(
                        random.randint(0, len(main_list)), dead_code_examples
                    )
            elif type.lower() == "high":
                for i in range(high):
                    main_list.insert(
                        random.randint(0, len(main_list)), dead_code_examples
                    )
            elif type.lower() == "extreme":
                for i in range(extreme):
                    main_list.insert(
                        random.randint(0, len(main_list)), dead_code_examples
                    )
            else:
                print("Invalid option!")
                time.sleep(3)
                Main()

        return main_list

    def level4(self):
        # Level 4 as promised. (I lowkey skidded it from someone else but i cant remember who :skull:) W mans tho ong
        # Also I can remake this instead of using JScript, etc
        batch_code = """@if (@CodeSection == @Batch) @then


@echo off
setlocal DisableDelayedExpansion

if "%~1" equ "" echo Usage: Obfuscate filename.bat & goto :EOF
if not exist "%~1" echo File not found: "%~1" & goto :EOF

set "at=@"
set "pass=%random%"
(
   echo %at%if (@Pass == @X%pass%^) @begin
   echo    @echo off
   echo    CScript //nologo //E:JScript.Encode "%%~F0" ^> %pass%.bat
   echo    call %pass%
   echo    del /f /q %pass%.bat
   echo    exit /B
   echo %at%end 
   echo //**Start Encode**
   echo var a = new Array(^);

   set "i=0"
   for /F "usebackq delims=" %%a in ("%~1") do (
      set /A i+=1
      set "line=%%a"
      setlocal EnableDelayedExpansion
      echo a[!i!] = '!line:'=\x27!';
      endlocal
   )

   setlocal EnableDelayedExpansion
   echo for ( var i=1; i^<=!i!; ++i ^) WScript.Stdout.WriteLine(a[i]^);
) > "%~N1.tmp"

CScript //nologo //E:JScript "%~F0" "%~N1.tmp"
::rename "%~N1.tmp" "%~N1.bat"
::del "%~N1.tmp"
rename "%~N1.tmp" "%~N1.encoded.bat"
goto :EOF


@end

//Made by some guy on stack overflow (I can't find the post anymore + I delete the old comments I had :sob:)
//I had to edit it a lil bit to make it work again. (It didn't work at all for me before)

var fileToEncode = WScript.Arguments(0);

var oFSO = WScript.CreateObject("Scripting.FileSystemObject");
var oFile = oFSO.GetFile(fileToEncode);
var oStream = oFile.OpenAsTextStream(1);
var sSourceFile = oStream.ReadAll();
oStream.Close();

var oEncoder = WScript.CreateObject("Scripting.Encoder");
var sDest = oEncoder.EncodeScriptFile(".js", sSourceFile, 0, "")

var edited_name = fileToEncode.replace(".bat", ".encoded.bat");

var oStream = oFSO.OpenTextFile(fileToEncode, 2, true);
oStream.Write(sDest);
oStream.Close();"""
        with open("level4.bat", "w") as f:
            f.writelines(batch_code)
        os.system("level4.bat " + self.file)
        file_name = self.file.replace(".bat", ".encoded.bat")
        os.rename(f"{file_name}", f"{self.file}.level4.bat")
        os.remove("level4.bat")

    def level5(self):
        batch_code = r"""@echo off
setlocal disableDelayedExpansion
if /i "%~1" equ "/m" set "/m=/m" & shift /1
set "in=%~1"
if not defined in echo Error: Missing inputFile>&2&exit /b
set "out=%~2"
if not defined out set "out=%~dpn1_obfuscated%~x1"
set "find={[:<][^}]*}|^[^:\r\n]?[ \t=,;\xFF]*:[^ \t:\r\n+]*[ \t:\r\n+]?|%%%%|%%\*|%%(?:~[fdpnxsatz]*(?:\$[^:\r\n]+:)?)?[0-9]|%%[^%%\r\n]+%%|%%@[\x20-\x24\x26-\x7E]"
set "repl=$txt=$0@$txt='%%'+String.fromCharCode($0.charCodeAt(0)+129)+'%%'"

setlocal enableDelayedExpansion
set "str1="
set "x=x"
for %%A in (2 3 4 5 6 7) do @for %%B in (0 1 2 3 4 5 6 7 8 9 A B C D E F) do set "str1=!str1!\x%%A%%B"
set "str1=%str1:~0,-4%"
set "str1=%str1:\x22=%\x22"
set "str1=%str1:\x24\x25=DDDD%"
call jrepl x str1 /m /x /v /s x /rtn lo
set "lo=!lo:DDDD=$!"

set "str2="
for %%A in (A B C D E F) do @for %%B in (0 1 2 3 4 5 6 7 8 9 A B C D E F) do set "str2=!str2!\x%%A%%B"
set "str2=%str2:~4%"
set "str2=%str2:\xA3=%\xA3"
set "str2=%str2:\xA6=%"
call jrepl x str2 /m /x /v /s x /rtn hi
call jrepl "" "%%%%=%%%%" /m /x /s hi /rtn hi2

call :write <"!in!" >"!out!"
exit /b

:write
echo @echo off^&(if defined @lo@ goto !hi:~0,1!)^&setlocal disableDelayedExpansion^&for /f "delims=:. tokens=2" %%%%A in ('chcp') do set "@chcp@=chcp %%%%A>nul"^&chcp 708^>nul^&set ^^^^"@args@=%%*"
echo set "@lo@=!lo!"
echo set "@hi@=!hi2!"
echo (setlocal enableDelayedExpansion^&for /l %%%%N in (0 1 93) do set "^!@hi@:~%%%%N,1^!=^!@lo@:~%%%%N,1^!")^&cmd /c ^^^^^""%%~f0" ^^!@args@^^!"
echo %%@chcp@%%^&exit /b
echo :!hi:~0,1!
jrepl "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"^
      "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"^
      %/m% /t "" /p "{[^:}][^}]*}" | jrepl find repl %/m% /t @ /v /x /jq
exit /b """
        with open("level5.bat", "w") as f:
            f.write(batch_code)
        r = requests.get(
            "https://www.dostips.com/forum/download/file.php?id=605", timeout=10
        )
        with open("jrepl.zip", "wb") as f:
            f.write(r.content)
        with ZipFile("jrepl.zip", "r") as zipObj:
            zipObj.extractall()
        os.remove("jrepl.zip")
        os.system("level5.bat " + self.file)
        os.remove("level5.bat")
        os.remove("JREPL.bat")
        file = self.file.replace(".bat", "_obfuscated.bat")
        os.rename(f"{file}", f"{self.file}.level5.bat")

    def bat2exe(self):
        code = """[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
"""
        current_dir = os.getcwd()
        bat_file_name = os.path.basename(self.file)
        exe_name = bat_file_name[:-4] + ".exe"

        app_launched = "AppLaunched=cmd /c " + '"' + bat_file_name + '"'
        target = f"TargetName={exe_name}"
        file_0 = f"FILE0={bat_file_name}"
        source_files = f"[SourceFiles]\nSourceFiles0={current_dir}"
        extra = f"[SourceFiles0]\n%FILE0%="

        to_write = [app_launched, target, file_0, source_files, extra]
        with open("setup.sed", "a+") as f:
            f.write(self.code_new)
            for item in to_write:
                f.write(item + "\n")
        os.system("iexpress /n /q /m setup.sed")
        os.remove("setup.sed")
        print(f"Exe file saved as {exe_name}")

    def bat2exe2(self):
        warning = Write.Input(
            "WARNING: This method requires you to download a exe file from the github repo and run it. Are you ok with this? (y/n): ",
            Colors.rainbow,
            interval=0.05,
        )
        if warning.lower() == "n":
            time.sleep(3)
            Main()
        else:
            r = requests.get(
                "https://github.com/KDot227/Somalifuscator/releases/download/Bat2Exe_Method1/Bat2Exe.exe"
            )
            with open("Bat2Exe.exe", "wb") as f:
                f.write(r.content)
            os.system("start Bat2Exe.exe")
            time.sleep(3)


if __name__ == "__main__":
    AutoUpdate()
    Main()
    print("Done!")
    more = Write.Input(
        "Do you want to obfuscate another file? (y/n): ", Colors.rainbow, interval=0.05
    )
    if more.lower() == "y":
        os.system("cls")
        Main()
    else:
        time.sleep(1)
        os._exit(0)
