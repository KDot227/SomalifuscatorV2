import random
import string
from random import randint
import kdot
from main import *


cesar_val = randint(1, 13)

__author__ = "K.Dot#4044 and Godfather"


def caesar_cipher_rotations(rotation):
    """Generates the Caesar cipher for a given rotation value."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


def caesar_cipher_rotations_upper(rotation):
    """Generates the Caesar cipher for a given rotation value. (CAPITAL LETTERS ONLY)"""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}1={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(cesar_val)
together = together[:-4]

kdot.check()

regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")

env_vars = [
    r"%ALLUSERSPROFILE%",
    r"%APPDATA%",
    r"%CD%",
    r"%CMDCMDLINE%",
    r"%CMDEXTVERSION%",
    r"%COMPUTERNAME%",
    r"%COMSPEC%",
    r"%DATE%",
    r"%ERRORLEVEL%",
    r"%HOMEDRIVE%",
    r"%HOMEPATH%",
    r"%NUMBER_OF_PROCESSORS%",
    r"%OS%",
    r"%PATH%",
    r"%PATHEXT%",
    r"%PROCESSOR_ARCHITECTURE%",
    r"%PROCESSOR_LEVEL%",
    r"%PROCESSOR_REVISION%",
    r"%PROMPT%",
    r"%RANDOM%",
    r"%SYSTEMDRIVE%",
    r"%SYSTEMROOT%",
    r"%TMP%",
    r"%TEMP%",
    r"%TIME%",
    r"%USERDOMAIN%",
    r"%USERNAME%",
    r"%USERPROFILE%",
    r"%WINDIR%",
    r"%0",
    r"%1",
    r"%2",
    r"%3",
    r"%4",
    r"%5",
    r"%6",
    r"%7",
    r"%8",
    r"%9",
    r"%*",
    r"%~dp0",
    r"%~dp1",
    r"%~dp2",
    r"%~dp3",
    r"%~dp4",
    r"%~dp5",
    r"%~dp6",
    r"%~dp7",
    r"%~dp8",
    r"%~dp9",
    r"%~f0",
    r"%~f1",
    r"%~f2",
    r"%~f3",
    r"%~f4",
    r"%~f5",
    r"%~f6",
    r"%~f7",
    r"%~f8",
    r"%~f9",
    r"%~nx0",
    r"%~nx1",
    r"%~nx2",
    r"%~nx3",
    r"%~nx4",
    r"%~nx5",
    r"%~nx6",
    r"%~nx7",
    r"%~nx8",
    r"%~nx9",
    r"%~s0",
    r"%~s1",
    r"%~s2",
    r"%~s3",
    r"%~s4",
    r"%~s5",
    r"%~s6",
    r"%~s7",
    r"%~s8",
    r"%~s9",
    r"%~t0",
    r"%~t1",
    r"%~t2",
    r"%~t3",
    r"%~t4",
    r"%~t5",
    r"%~t6",
    r"%~t7",
    r"%~t8",
    r"%~t9",
    r"%~x0",
    r"%~x1",
    r"%~x2",
    r"%~x3",
    r"%~x4",
    r"%~x5",
    r"%~x6",
    r"%~x7",
    r"%~x8",
    r"%~x9",
    r"%~a0",
    r"%~dpn0",
    r"%~dpnx0",
]


class Ultimate:
    def __init__(self, utf_16=True, check_bypass=False, file_content=None) -> None:
        self.utf_16 = utf_16
        self.check_bypass = check_bypass
        self.file_content = file_content
        self.new_code = []

    def Main(self):
        line = ""
        self.potential_values = {
            "echo": self.echo,
            "set": self.set_,
            "setlocal": self.setlocal,
            "if": self.if_,
            "for": self.for_,
            "goto": self.goto,
            "call": self.call,
            "pause": self.pause,
            "exit": self.exit,
        }

        for index, line in enumerate(self.file_content):
            line = line.strip()
            if line == "":
                continue
            split_line = line.split(" ")
            first_word = split_line[0].lower()
            try:
                self.new_code.append(self.potential_values.get(first_word)(line))
            except Exception:
                echo_check123 = False
                try:
                    if r"%errorlevel%" in self.file_content[index - 1].lower():
                        echo_check123 = True
                except IndexError:
                    pass
                if r"%errorlevel%" in line.lower():
                    echo_check123 = True
                try:
                    if r"%errorlevel%" in self.file_content[index + 1].lower():
                        echo_check123 = True
                except IndexError:
                    pass
                self.new_code.append(self.obf_normal(line, echo_check123))
        return self.new_code

    def echo(self, line: str) -> str:
        choices = {
            "for_loop": self.for_loop,
            "mshta": self.mshta,
            "powershell": self.powershell,
        }
        pick = random.choice(list(choices.keys()))
        return choices.get(pick)(line)

    def set_(self, line: str) -> str:
        return line

    def setlocal(self, line: str) -> str:
        return line

    def if_(self, line: str) -> str:
        return line

    def for_(self, line: str) -> str:
        return line

    def goto(self, line: str) -> str:
        return line

    def call(self, line: str) -> str:
        return line

    def pause(self, line: str) -> str:
        return line

    def exit(self, line: str) -> str:
        return line

    def obf_normal(self, line: str, echo_check: bool) -> str:
        return self.obf_oneline(line) + "\n"

    def mshta(self, line):
        chars = [ord(c) for c in line]
        # example output = "Chr(89) & Chr(111)& Chr(117) & Chr(114) & Chr(32) & Chr(109) & Chr(97) & Chr(109) & Chr(97) & Chr(32)"
        chars = " & ".join([f"Chr({c})" for c in chars])
        return self.obf_oneline(
            f'mshta vbscript:execute("CreateObject(""Scripting.FileSystemObject"").GetStandardStream(1).Write({chars}):Close")|more'
        )

    def powershell(self, line):
        return line

    def for_loop(self, line):
        pass

    def ran1(self, char):
        # caesar cipher rotation shi
        choices = [self.make_random_string(), self.make_random_string()]
        randomed = random.choice(choices)
        if char in string.ascii_letters:
            if char.islower():
                coded0 = self.caesar_cipher_rotation(char)
                coded = coded0.replace(coded0, f"%{coded0}%")
                return f"{coded}%{randomed}%"
            else:
                coded0 = self.caesar_cipher_rotation_UPPER(char)
                coded = coded0.replace(coded0, f"%{coded0}1%")
                return f"{coded}%{randomed}%"
        else:
            return f"{char}%{randomed}%"

    def ran2(self, char, random_order):
        # fasho could have used dict for this but idc its already done
        public = r"C:\Users\Public"
        weird = r"C:\Program Files (x86)\Common Files"
        program_1 = r"C:\Program Files"
        program_2 = r"C:\Program Files (x86)"
        psmodule_path = r"C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
        driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
        comspec = r"C:\WINDOWS\system32\cmd.exe"
        pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

        list_of_all = [
            public,
            weird,
            program_1,
            program_2,
            psmodule_path,
            driver_stuff,
            comspec,
            pathext,
        ]

        corosponding = [
            "PUBLIC",
            "COMMONPROGRAMFILES(X86)",
            "PROGRAMFILES",
            "PROGRAMFILES(X86)",
            "PSMODULEPATH",
            "DRIVERDATA",
            "COMSPEC",
            "PATHEXT",
        ]

        new_lists = []

        for i in list_of_all:
            if char in i:
                new_lists.append(i)

        if len(new_lists) > 0:
            if char == " ":
                return char
            new = random.choice(new_lists)
            if char in new:
                if new == psmodule_path:
                    index = new.index(char)
                    new = corosponding[list_of_all.index(new)]
                    return f"%{self.random_capitalization(new)}:~{index},1%"
                else:
                    index = new.index(char)
                    new = corosponding[list_of_all.index(new)]
                    return f"%{self.random_capitalization(new)}:~{index},1%"
        else:
            if char in string.ascii_letters:
                var = f"%{self.random_capitalization('KDOT')}:~{random_order.index(char)},1%"
                return var
            else:
                return char

    # def ran3(self, char):
    #    if char in string.ascii_letters:
    #        escape = "^"
    #        return f"{escape}{char}"
    #    else:
    #        return char'

    def ran3(self, line):
        random_letter = random.choice(string.ascii_letters)
        random_number = random.randint(1, 99)
        return f"for /l %%{random_letter} in ( {random_number}, {random_number}, {random_number} ) do ( {line} )\n"

    def random_dead_code(self, entire_array):
        """Dead code that just won't be executed so it can be whatever. If u wanna add more its all u"""
        dead_code = [
            "echo Best Batch Obfuscated By KDot and Godfather\n",
            "if 0 == 0 (echo Best Batch Obfuscated By KDot and Godfather)\n",
            f"set KDOT={self.fake_KDOT()}\n",
            f"{self.fake_ceaser_cipher()}\n",
            f"{self.fake_ceaser_cipher_obfuscated()}\n",
            f"set somalifuscator=op_asf\n",
        ]
        if eicar:
            dead_code.append(
                "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n"
            )
        for array in entire_array:
            if randint(0, 3) == 3:
                option = random.choice(dead_code)
                if (
                    option
                    # it's funny cause it's still fud even unobfuscated
                    == "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n"
                ):
                    scated = option
                else:
                    scated = self.obf_oneline(option)
                new_string = "".join(scated)
                new_string = [new_string]
                entire_array.insert(entire_array.index(array), new_string)

        return entire_array

    def vm_test(self):
        codes = [
            # r"""for /f "tokens=2 delims==" %%a in ('wmic computersystem get manufacturer /value') do set manufacturer=%%a\nfor /f "tokens=2 delims==" %%a in ('wmic computersystem get model /value') do set model=%%a\nif "%manufacturer%"=="Microsoft Corporation" if "%model%"=="Virtual Machine" exit\nif "%manufacturer%"=="VMware, Inc." exit\nif "%model%"=="VirtualBox" exit""",
            # r"""for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "Total Physical Memory"') do ( set available_memory=%%a ) & set available_memory=%available_memory: =% & set available_memory=%available_memory:M=% & set available_memory=%available_memory:B=% & set /a available_memory=%available_memory% / 1024 / 1024 & if not %available_memory% gtr 4 ( exit /b 1 )""",
            # I love batch so much I gave up and used powershell
            """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$VM=Get-WmiObject -Class Win32_ComputerSystem ; if ($VM.Model -match 'Virtual') { Write-Host 'Virtual Machine Detected. Exiting script.' ; taskkill /F /IM cmd.exe }\""""
            # """powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "$tr=(Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory / 1KB ; $trgb=[math]::Round($tr / 1024, 2) ; if ($trgb -lt 8) { Write-Host 'Less than 8gb ram exiting' ; pause }\""""
        ]
        # ill add more one day
        return self.obf_oneline(random.choice(codes))

    def byte_check(self):
        choices = [
            """powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -Command \"$bytes = [System.IO.File]::ReadAllBytes('%~f0') ; if (($bytes[0] -ne 0xFF) -or ($bytes[1] -ne 0xFE) -or ($bytes[2] -ne 0x26)) { Write-Host 'The first 3 bytes of the file are not FF FE 0A.' ; taskkill /F /IM cmd.exe }\"""",
        ]

        choice = random.choice(choices)
        obfus = self.obf_oneline(choice)
        return obfus

    def tests(self):
        # I just made this cause editing it the other way would be annoying
        choices = [self.first_line_echo_check()]
        if anti_vm:
            choices.append(self.vm_test())

        if utf_16_bom and not self.level == "exe2bat":
            choices.append(self.byte_check())

        if debug:
            choices = [self.first_line_echo_check()]
        return choices

    def fake_ceaser_cipher_obfuscated(self):
        """simple function to obfuscate the cipher"""
        cipher = self.fake_ceaser_cipher()
        obfuscated = self.obf_oneline(cipher)
        return obfuscated

    def fake_KDOT(self):
        """makes fake KDOT var"""
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_order = "".join(random.sample(characters, len(characters)))
        return random_order

    def make_xor(self, number: int, hex_check: bool = True):
        """makes xor key"""
        ans = number

        if ans < 0:
            return self.random_oct_hex(ans)

        binary_string = bin(ans)[2:]

        choices = [0, 1]

        random_binary = [random.choice(choices) for i in range(len(binary_string))]

        random2 = "".join(str(i) for i in random_binary)
        random2 = int(random2, 2)

        fixed_binary = [
            int(binary_string[i]) ^ int(random_binary[i])
            for i in range(len(binary_string))
        ]

        fixed2 = "".join(str(i) for i in fixed_binary)
        fixed2 = int(fixed2, 2)

        if hex_check:
            random_tf = random.randint(1, 3)
            if not recursive_xor:
                random_tf = 2
            try:
                if random_tf != 1:
                    return f"({self.random_oct_hex(random2)} ^^ {self.random_oct_hex(fixed2)})"
                else:
                    return f"({self.make_xor(random2)} ^^ {self.make_xor(fixed2)})"
            except RecursionError:
                return (
                    f"({self.random_oct_hex(random2)} ^^ {self.random_oct_hex(fixed2)})"
                )
        else:
            return f"({hex(random2)} ^^ {hex(fixed2)})"

    def generate_math_problem(self, answer: int):
        """Entire point of this is to make a math problem for the set /a. We do this cause kids need a calculator but once they see that there are octals and hexadecimals they'll prolly give up lmao"""
        # no division since we don't want floats BUT we can use division in the answer since its how you undo multiplication
        # but im not gonna do this cause it still makes floats and im slow
        operators = ["+", "-"]
        opp1 = random.choice(operators)
        opp2 = random.choice(operators)
        num1 = random.randint(10000, 10000000)
        num2 = random.randint(10000, 10000000)

        # maybe add division and multiplication to the problem using even dividers and getting remainder to check if zero.

        problem = f"{answer} {opp1} {num1} {opp2} {num2}"
        ans = eval(problem)

        # make new problem from original answer

        if opp1 == "+":
            opp1 = "-"
        else:
            opp1 = "+"

        if opp2 == "+":
            opp2 = "-"
        else:
            opp2 = "+"

        # randomly do hex or oct to ans instead of all just hex
        choices = [True, False]
        problem2 = f"{self.random_oct_hex(ans) if random.choice(choices) else self.make_xor(ans)} {opp1} {self.random_oct_hex(num1) if random.choice(choices) else self.make_xor(num1)} {opp2} {self.random_oct_hex(num2) if random.choice(choices) else self.make_xor(num2)}"
        problem23 = f"{ans} {opp1} {num1} {opp2} {num2}"

        ans2 = eval(problem23)

        while ans < 0:
            operators = ["+", "-"]
            opp1 = random.choice(operators)
            opp2 = random.choice(operators)
            num1 = random.randint(10000, 10000000)
            num2 = random.randint(10000, 10000000)

            problem = f"{answer} {opp1} {num1} {opp2} {num2}"
            ans = eval(problem)

            # make new problem from original answer

            if opp1 == "+":
                opp1 = "-"
            else:
                opp1 = "+"

            if opp2 == "+":
                opp2 = "-"
            else:
                opp2 = "+"

            # for some reason if number is negative only hex will work idk why and im not tryna figure it out
            # mental health > octals
            problem2 = f"{hex(ans)} {opp1} {self.random_oct_hex(num1)} {opp2} {self.random_oct_hex(num2)}"
            problem23 = f"{ans} {opp1} {num1} {opp2} {num2}"

            ans2 = eval(problem23)

        return problem2, ans2

    def scrambler(self, codeed):
        """This absolutely beautiful function takes the code, puts it into a nested array of goto values that all point to each other then obfuscates tf outta it."""
        original_lines = codeed

        for index, line in enumerate(original_lines):
            # not sure if echo really makes a difference but batch does some weird things sometimes
            echo_check123 = False
            try:
                if r"%errorlevel%" in original_lines[index - 1].lower():
                    echo_check123 = True
            except IndexError:
                pass
            # This should never have an index error since it's the current itteration in the list
            # if it does get an error then u got other issues. Also at that point dont make an issue just pray to god (or whoever or dont pray idc) and restart ur pc
            if r"%errorlevel%" in line.lower():
                echo_check123 = True
            try:
                if r"%errorlevel%" in original_lines[index + 1].lower():
                    echo_check123 = True
            except IndexError:
                pass
            if not echo_check123:
                random_number = random.randint(1, 4)
                if random_number == 1:
                    # add a label that doesn't do anything
                    label = f":{self.make_random_label_no_working()}\n"
                    original_lines.insert(index, label)

        original_lines = [
            item for item in original_lines if item not in [";", "\n", ";\n"]
        ]

        self.dict_thing = {}

        main_list = []

        for index, item in enumerate(original_lines):
            echo_check123 = False
            # check if %errorlevel% is in the previous line and the current line and next line and if it is then set it to True
            try:
                if r"%errorlevel%" in original_lines[index - 1].lower():
                    echo_check123 = True
            except IndexError:
                pass
            # This should never have an index error since it's the current itteration in the list
            # if it does get an error then u got other issues. Also at that point dont make an issue just pray to god (or whoever or dont pray idc) and restart ur pc
            if r"%errorlevel%" in item.lower():
                echo_check123 = True
            try:
                if r"%errorlevel%" in original_lines[index + 1].lower():
                    echo_check123 = True
            except IndexError:
                pass
            t = self.generate_math_problem(answer=random.randint(100000, 10000000))
            self.dict_thing[item] = [
                t[0],
                t[1],
                index,
                echo_check123,
            ]

        # I use ; infront of everything cause it gets rid of syntax highlight on vscode and notepad++ lmao

        # NOTE everything in this for loop is the most confusing and worse coding I have ever done in my life. I am sorry for whoever is trying to read, imrpove or just understand what is going on especially if you have no prior knowledge of batch
        for index, (key, value) in enumerate(self.dict_thing.items()):
            if index == 0:
                remem = [
                    f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(value[0])}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                ]
            part_1 = f";:{value[1]}\n"
            part_2 = f";{key}\n"
            if hell and unicode:
                badded = (
                    r" ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็"
                    * random.randint(10, 20)
                )
                try:
                    random_t_f = random.choice([True, False])
                    if random_t_f:
                        dead = list(self.dict_thing.values())[index + 1][1]
                        random_working_value = random.choice(
                            list(self.dict_thing.values())
                        )
                        while random_working_value[1] == dead:
                            random_working_value = random.choice(
                                list(self.dict_thing.values())
                            )
                        run = self.deadcodes(
                            good_label=str(dead), bad_label=random_working_value[1]
                        )
                        part_3 = f"{run}\n::{badded}\n"
                    else:
                        maybe_echo_check = random.randint(1, 3)
                        if maybe_echo_check == 1 and not value[3]:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n::{badded}\n::{badded}\n::{badded}\n{self.obf_oneline(random.choice(self.tests()))}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                        else:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n::{badded}\n::{badded}\n::{badded}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                except Exception:
                    part_3 = f";{self.random_semi_and_comma(self.obf_oneline('goto'))} :EOF\n::{badded}\n::{badded}\n::{badded}\n"
            else:
                try:
                    random_t_f = random.choice([True, False])
                    if random_t_f:
                        dead = list(self.dict_thing.values())[index + 1][1]
                        random_working_value = random.choice(
                            list(self.dict_thing.values())
                        )
                        while random_working_value[1] == dead:
                            random_working_value = random.choice(
                                list(self.dict_thing.values())
                            )
                        run = self.deadcodes(
                            good_label=str(dead), bad_label=random_working_value[1]
                        )
                        part_3 = f"{run}\n"
                    else:
                        maybe_echo_check = random.randint(1, 3)
                        if maybe_echo_check == 1 and not value[3]:
                            print(value[3])
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n{self.obf_oneline(random.choice(self.tests()))}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                        else:
                            part_3 = f";{self.obf_oneline('set')} /a {self.obf_oneline('ans')}={self.obf_oneline(list(self.dict_thing.values())[index + 1][0])}\n;{self.random_semi_and_comma(self.obf_oneline('goto'))} :%ans%\n"
                except Exception:
                    part_3 = f";{self.random_semi_and_comma(self.obf_oneline('goto'))} :EOF\n"

            main_list.append([part_1, part_2, part_3])

        random.shuffle(main_list)

        main_list = self.random_inserts(main_list)

        main_list = self.random_dead_code(main_list)

        main_list = self.bad_labels_and_dead_code(main_list)

        if random_spacing:
            main_list = self.more_dead_comments(main_list)

        if pogdog_fun:
            main_list = self.pogdog(main_list)

        # pointer that points to first line of the actual code.
        main_list.insert(0, remem)

        return main_list

    def deadcodes(self, good_label, bad_label):
        """not really deadcode but it just makes it hard for kids to understand"""
        # gotta love %random%
        # hehehehe
        RANNUM = randint(32769, 99999)
        # This is absolute hell for anyone trying to deobfuscate this
        label123 = bad_label
        if self.rep_num < 5:
            examples = [
                f"if %random% equ {RANNUM} ( goto :{label123} ) else ( goto :{good_label} )",
                f"if not 0 neq 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System32 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if not %cd% == %cd% ( goto :{label123} ) else ( goto :{good_label} )",
                f"if 0 equ 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System3 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %cd% == %cd% ( goto :{good_label} ) else ( goto :{label123} )",
                f"if chcp leq 1 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %CD% == %__CD__% ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %~dp0==%__cd__% ( goto :{good_label} ) else ( goto :{label123} )",
            ]
        else:
            examples = [
                f"if %random% equ {RANNUM} ( goto :{label123} ) else ( goto :{good_label} )",
                f"if not 0 neq 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System32 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if not %cd% == %cd% ( goto :{label123} ) else ( goto :{good_label} )",
                f"if 0 equ 0 ( goto :{good_label} ) else ( goto :{label123} )",
                f"if exist C:\Windows\System3 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %cd% == %cd% ( goto :{good_label} ) else ( goto :{label123} )",
                f"if chcp leq 1 ( goto :{label123} ) else ( goto :{good_label} )",
                f"if not defined KDOT ( goto :EOF ) else ( goto :{good_label} )",
                f"if not defined f ( goto :EOF ) else ( goto :{good_label} )",
                f"if %CD% == %__CD__% ( goto :{label123} ) else ( goto :{good_label} )",
                f"if %~dp0==%__cd__% ( goto :{good_label} ) else ( goto :{label123} )",
            ]
        if echo_weird:
            random_maybe = random.choice([True, False])
            code_examples = [
                "::Made with somalifuscator",
                "::discord.gg/batch",
                "::https://sped.lol",
                "::KDot > Batch",
            ]
            if random_maybe:
                coded = f"{random.choice(code_examples)} ^\n {random.choice(examples)} ^\n exit /b 0\n{random.choice(examples)}"
                for _ in range(3):
                    examples.append(coded)
            else:
                coded = f"{random.choice(code_examples)} ^\n exit /b 0\n {random.choice(examples)}"
                for _ in range(3):
                    examples.append(coded)

        randomed = random.choice(examples)
        obfuscated = self.obf_oneline(randomed)
        self.rep_num += 1
        return obfuscated

    def random_inserts(self, main_list):
        listes = [
            ";::Made by K.Dot and Godfather\n",
            ";::Good luck deobfuscating\n",
            ";::Made with Somalifuscator\n",
            ";::discord.gg/batch\n",
            ";::... --- -- .- .-.. .. ..-. ..- ... -.-. .- - --- .-. / --- -. / - --- .--.",
        ]
        for i in range(len(main_list)):
            if i == 0:
                continue
            else:
                random_int = randint(1, 10)
                if random_int == 10:
                    list_choice = random.choice(listes)
                    list_choice = self.random_capitalization(list_choice)
                    main_list.insert(i, [list_choice])

        return main_list

    def bad_labels_and_dead_code(self, main_list):
        """inserts labels that are valid but won't do anything since they have a zero width space infront. This mainly messes up looking at it from a text editor. You can still goto it if you use the weird translated bytes."""
        main_dict = self.dict_thing.copy()
        new_list = []
        types = [True, False]
        doskey_options = [
            "dir",
            "echo",
            "for",
            "if",
            "set",
            "goto",
            "cd",
            "",
        ]
        bad_insert = "GODFATHER"
        for item in main_dict.values():
            strung = str(item[1])
            strung = ";:" + bad_insert + strung
            new_list.append(strung)
        for array in main_list:
            # if next word contains %errorlevel% in lowercase in current itteration then skip
            if r"%errorlevel%" in array[0].lower():
                pass
            else:
                random_choci = random.choice(types)
                if random_choci:
                    random_chance = randint(1, 3)
                    if random_chance == 5:
                        random_label = random.choice(new_list)
                        random_place = randint(0, len(array))
                        array.insert(random_place, random_label)
                else:
                    doskey = f"doskey {random.choice(doskey_options)}={random.choice(doskey_options)}"
                    array.append(self.obf_oneline(doskey))
        return main_list

    def first_line_echo_check(self):
        if not echo_check:
            return "\n"
        """basically just checks the entire file for the word echo. If it finds it then it will kill the process. Also the no debug checks to see if the user is double clicking the file instead of running it through a different application"""
        # I hate people who echo
        self.checked123 = True
        # This is for when I run through vscode but I can't since it just finna close itself
        self.debug = True
        if not double_click_check:
            self.debug = True
        if self.check_bypass:
            return ""
        if self.debug:
            if self.checked123 == True:
                command = (
                    r'echo @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( ( goto ) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                    + "\n"
                )
                self.checked123 = False
                return command
            else:
                command = (
                    r'echo @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( ( goto ) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat'
                    + "\n"
                )
                return command
        else:
            if self.checked123 == True:
                command = (
                    """net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q close.bat >nul 2>&1 & exit )\necho @echo off > close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                    + "\n"
                )
                self.checked123 = False
                return command
            else:
                command = (
                    """net session >nul 2>&1 || IF /I %0 NEQ "%~dpnx0" ( del /f /q close.bat >nul 2>&1 & exit )\necho @echo off >> close.bat && echo findstr /i "echo" "%~f0" >> close.bat && echo if %%errorlevel%% == 0 ( taskkill /f /im cmd.exe ) else ( (goto) ^2^>^n^u^l ^& del "%%~f0" ) >> close.bat && call close.bat"""
                    + "\n"
                )
                return command

    def anti_check_error(self, code):
        """This just checks to see if the first byte of the file is the utf-16 BOM. If it is then it clears screen otherwise it exits."""
        strung = ">nul 2>&1 && exit >nul 2>&1 || cls \n@echo off\n"
        strung = self.obf_oneline(strung)
        code.insert(0, strung)

        # There is a 99% chance I could have just used .encode() but im just lazy like that if u gotta problem wit it make a pr

        with open("placeholder.bat", "w", encoding="utf-8", errors="ignore") as f:
            f.writelines(code)
        with open("placeholder.bat", "rb") as f:
            code = f.read()

        os.remove("placeholder.bat")

        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE"])

        out_hex.extend(["{:02X}".format(b) for b in code])

        return out_hex

    @staticmethod
    def make_random_string(length_nums=(5, 7)):
        length = random.randint(*length_nums)
        stringed = "".join(
            random.choice(
                # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
                # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$(),.?@[]_"
            )
            for _ in range(length)
        )
        # yes this has happened to me before and echo check terms it
        while "echo" in stringed.lower():
            stringed = "".join(
                random.choice(
                    # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
                    # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                )
                for _ in range(length)
            )
        return stringed

    @staticmethod
    def random_capitalization(string):
        return "".join(random.choice([char.upper(), char.lower()]) for char in string)

    @staticmethod
    def make_random_label_no_working():
        # 911 lol
        length = random.choice([9, 11])
        return "".join(random.choice(chinese_characters) for _ in range(length))

    @staticmethod
    def fake_ceaser_cipher():
        together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(
            cesar_val
        )
        together = together[:-4]
        return together

    @staticmethod
    def more_dead_comments(main_list) -> list:
        code_examples = [
            "::Made with somalifuscator",
            "::discord.gg/batch",
            "::https://sped.lol",
        ]
        for _ in range(len(main_list)):
            random_chance = random.choice([True, False])
            if random_chance:
                main_list.insert(
                    random.randint(0, len(main_list)),
                    random.choice(code_examples),
                )
        return main_list

    def obf_oneline(self, line):
        final_string = ""
        for word in line.split(" "):
            if word.startswith("%"):
                final_string += word + " "
                continue
            if word.find("%~") != -1:
                final_string += word + " "
                continue
            if word.startswith("^"):
                final_string += word + " "
                continue
            if word.startswith("::"):
                final_string += word + " "
                continue
            else:
                for char in word:
                    # fasho could have used dict for this but idc its already done
                    public = r"C:\Users\Public"
                    weird = r"C:\Program Files (x86)\Common Files"
                    program_1 = r"C:\Program Files"
                    program_2 = r"C:\Program Files (x86)"
                    psmodule_path = r"C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
                    driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
                    comspec = r"C:\WINDOWS\system32\cmd.exe"
                    pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

                    list_of_all = [
                        public,
                        weird,
                        program_1,
                        program_2,
                        psmodule_path,
                        driver_stuff,
                        comspec,
                        pathext,
                    ]

                    corosponding = [
                        "PUBLIC",
                        "COMMONPROGRAMFILES(X86)",
                        "PROGRAMFILES",
                        "PROGRAMFILES(X86)",
                        "PSMODULEPATH",
                        "DRIVERDATA",
                        "COMSPEC",
                        "PATHEXT",
                    ]

                    new_lists = []

                    for i in list_of_all:
                        if char in i:
                            new_lists.append(i)

                    if len(new_lists) > 0:
                        if char == " ":
                            final_string += char
                        new = random.choice(new_lists)
                        if char in new:
                            if new == psmodule_path:
                                index = new.index(char)
                                new = corosponding[list_of_all.index(new)]
                                final_string += (
                                    f"%{self.random_capitalization(new)}:~{index},1%"
                                )
                            else:
                                index = new.index(char)
                                new = corosponding[list_of_all.index(new)]
                                final_string += (
                                    f"%{self.random_capitalization(new)}:~{index},1%"
                                )
                    else:
                        if unicode:
                            final_string += f"%‮%{char}%‮%"
                        else:
                            random_string = "".join(
                                random.choice(string.ascii_letters)
                                for _ in range(randint(5, 7))
                            )
                            final_string += f"%{random_string}%{char}%{random_string}%"
                final_string += " "

        return final_string

    @staticmethod
    def random_oct_hex(ans: int):
        choices = [hex(ans), oct(ans), ans]
        decided = random.choice(choices)
        if decided == oct(ans):
            return "0" + str(decided[2:])
        elif decided == hex(ans):
            random_quotes = random.choice([True, False])
            if random_quotes:
                return '"' + str(decided) + '"'
            return decided
        else:
            return decided

    @staticmethod
    def random_semi_and_comma(string):
        symbols = [";", ",", " ", "     "]
        random_symbols = "".join(random.choice(symbols) for _ in range(randint(3, 7)))
        new_string = random_symbols + string + random_symbols
        return new_string

    @staticmethod
    def pogdog(entire_array):
        if not unicode:
            return entire_array
        uni = r"็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็ ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็"
        for array in entire_array:
            if randint(0, 3) == 3:
                scated = uni * 2
                new_string = [scated]
                entire_array.insert(entire_array.index(array), new_string)

        return entire_array

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


file_contents = ["@echo off\n", "echo this is a test\n", "pause\n", "exit\n"]
ultimate = Ultimate(file_content=file_contents)
output = ultimate.Main()

print(output)
