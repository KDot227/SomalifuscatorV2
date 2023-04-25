import os, random, re

from rich.progress import Progress
from util.settings import *


class Ultimate:
    def __init__(
        self, file, utf_16=True, check_bypass=False, debug=False, *args, **kwargs
    ) -> None:
        self.file = file
        self.utf_16 = utf_16
        self.check_bypass = check_bypass
        self.debug = False

    def main(self) -> None:
        if self.debug:
            self.check_bypass = True
            utf_16 = False
        # progress bar things
        with Progress() as progress:
            task1 = progress.add_task("[bold green]Searching through file", total=100)
            task1andhalf = progress.add_task("[bold green]Obfuscating", total=100)
            task2 = progress.add_task("[bold green]Adding Anti Echo", total=100)
            task3 = progress.add_task("[bold green]Cleaning Obfuscated Code", total=100)
            task4 = progress.add_task(
                "[bold green]Cleaning up Echo Commands", total=100
            )
            task5 = progress.add_task(
                "[bold green]Writing Out-Bytes to File", total=100
            )
            try:
                os.remove(f"{self.file}.ultimate.bat")
            except:
                pass
            # cool thing
            # mshta vbscript:execute("CreateObject(""Scripting.FileSystemObject"").GetStandardStream(1).Write(Chr(89) & Chr(111)& Chr(117) & Chr(114) & Chr(32) & Chr(109) & Chr(97) & Chr(109) & Chr(97) & Chr(32) ):Close")|more
            # ultimate mode
            with open(self.file, "r", encoding="utf-8", errors="ignore") as f:
                data = f.readlines()

            # This took way longer than it should have
            # Basically the entire point of it is to turn multiline commands that could be oneline into just oneline commands. I'm guessing this will break for anything larger than like 30 lines. If that's the cause then do if not stuff

            # basic parsing of the file and changing things that need to be changed

            new_lines = []
            i = 0
            while i < len(data):
                line = data[i].strip()

                if line.endswith("("):
                    while not line.endswith(")"):
                        i += 1
                        next_line = data[i].strip()
                        # Add '&' between lines cause it can't just do stuff like allat
                        line += " & " + next_line

                    line = line.replace("\n", " ").replace("\r", "")
                    line = " ".join(line.split())

                    # regex cause im a RE tard
                    # that was funny asf ngl
                    matches = re.findall(r"\((.*?)\)", line)
                    for match in matches:
                        if match.startswith(" &"):
                            modified_match = match[2:-2]
                            line = line.replace(match, modified_match)
                        else:
                            modified_match = match

                if line:
                    new_lines.append(line + "\n")
                i += 1

            data = new_lines.copy()

            if scramble_labels:
                unique_labels = set(re.findall(r":\w+", " ".join(data)))

                label_mappings = {}

                for label in unique_labels:
                    random_string = self.make_random_string((8, 9))
                    label_mappings[label] = ":" + random_string

                for i in range(len(data)):
                    for label in label_mappings:
                        data[i] = data[i].replace(label, label_mappings[label])

            data = data.copy()

            if self.self.debug:
                with open("debug1.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(data)

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

            self.used_env_vars = []

            for env_var in env_vars:
                if env_var in data:
                    self.used_env_vars.append(env_var)

            # if ads:
            #    lines = data.copy()
            #    new_lines = []
            #    maybe = False
            #
            #    for line in lines:
            #        line = line.lower()
            #        # basic checks
            #        if (
            #            line.startswith("echo")
            #            and not line.startswith("echo @")
            #            and ("&" not in line or "^&" in line)
            #        ):
            #            maybe = True
            #            new_lines.append(
            #                line.strip()
            #                + " > somali.txt:kdot & more < somali.txt:kdot\n"
            #            )
            #        else:
            #            new_lines.append(line)
            #
            #    new_lines.reverse()
            #    for index, line in enumerate(new_lines):
            #        if (
            #            line.startswith("echo")
            #            and not line.startswith("echo @")
            #            and maybe
            #        ):
            #            new_lines[index] = line.strip() + " & del somali.txt\n"
            #            break
            #    new_lines.reverse()
            #
            #    data = new_lines.copy()

            if self.debug:
                with open("debug1_2.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(data)

            progress.update(task1, advance=100)
            with open(
                f"{self.file}.ultimate.bat", "a+", encoding="utf-8", errors="ignore"
            ) as f:
                # self.potential_values = {
                #    "echo": self.echo,
                #    "set": self.set_,
                #    "setlocal": self.setlocal,
                #    "if": self.if_,
                #    "for": self.for_,
                #    "goto": self.goto,
                #    "call": self.call,
                #    "pause": self.pause,
                #    "exit": self.exit,
                # }
                f.write(self.random_capitalization("::Made by K.Dot and Godfather\n"))
                f.write(self.code_new)
                characters = (
                    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                )
                random_order = "".join(random.sample(characters, len(characters)))
                f.write(self.obf_oneline(f"set KDOT={random_order}\n"))
                # for line in track(
                #    data, description="[bold green]Obfuscating", total=len(data)
                # ):
                # This regex is basically tryna get variables that are set to a value. For example if someone has set "starttime=%time%"
                regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")
                for index, line in enumerate(data):
                    progress.update(task1andhalf, advance=100 / len(data))
                    random_bool = random.choice([True, False])
                    # first_word = line.split()[0]
                    # error_level_next = False
                    # try:
                    #    if r"%errorlevel%" in data[index - 1].lower():
                    #        error_level_next = True
                    # except IndexError:
                    #    pass
                    # if r"%errorlevel%" in line.lower():
                    #    error_level_next = True
                    # try:
                    #    if r"%errorlevel%" in data[index + 1].lower():
                    #        error_level_next = True
                    # except IndexError:
                    #    pass
                    bad_words = ["set", "&", "nul", ">"]
                    # why do some of these break? no idea lmao
                    carrot_case = (
                        False
                        if any(word in line.lower() for word in bad_words)
                        else True
                    )
                    if for_loop:
                        random_bool_2 = random.choice([True, False])
                        if random_bool_2 and not line.startswith(":"):
                            line = self.ran3(line=line)
                    if line.startswith("::"):
                        f.write(line + "\n")
                        continue
                    elif line.startswith(":"):
                        f.write(line + "\n")
                        continue
                        # TODO add label obf
                    # elif first_word in self.potential_values:
                    #    output_obf = self.potential_values[first_word](
                    #        line, error_level_next
                    #    )
                    #    print("worked")
                    #    f.write(output_obf + "\n")
                    #    continue
                    else:
                        if random_bool == True:
                            symbols = [";", ",", " ", "     "]
                            random_symbols = "".join(
                                random.choice(symbols)
                                for _ in range(random.randint(3, 7))
                            )
                            f.write(random_symbols)
                        for word in line.split():
                            if any(
                                env_var.lower() in word.lower() for env_var in env_vars
                            ):
                                f.write(word + " ")
                                continue
                            elif word.startswith("%") or word.startswith("!"):
                                f.write(self.random_capitalization(word) + " ")
                                continue
                            elif re.match(regex_bat, word):
                                # regex be my bae
                                f.write(word + " ")
                                continue
                            elif word.startswith(":") and not word.startswith("::"):
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
                                        random_obf = [
                                            self.ran1(char),
                                            self.ran2(
                                                char, random_order, carrot=carrot_case
                                            ),
                                        ]
                                        f.write(f"{random.choice(random_obf)}")
                                f.write(" ")
                        f.write("\n")
            # ignore everything below this until the function ends I could have made this 100x better but I'm lazy
            with open(
                f"{self.file}.ultimate.bat", "r", encoding="utf-8", errors="ignore"
            ) as f:
                news = f.readlines()
            if self.debug:
                with open("debug2.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(news)
            news.insert(2, self.obf_oneline(self.first_line_echo_check()))
            messed_up = self.scrambler(news)
            progress.update(task2, advance=100)
            with open(
                f"{self.file}.ultimate.bat", "w", encoding="utf-8", errors="ignore"
            ) as f:
                for array in messed_up:
                    for thing in array:
                        f.write(thing.strip() + "\n")
            if self.debug:
                with open("debug3.bat", "w", encoding="utf-8", errors="ignore") as f:
                    for array in messed_up:
                        for thing in array:
                            f.write(thing.strip() + "\n")
            progress.update(task3, advance=100)
            with open(
                f"{self.file}.ultimate.bat", "r", encoding="utf-8", errors="ignore"
            ) as f:
                data = f.readlines()
                # add echo off to the first line
                data.insert(0, "@echo off\n")
                for i in range(len(data)):
                    if "echo" in data[i]:
                        data[i] = data[i].replace(
                            "echo", r"%GODFATHER%e%GODFATHER%c%GODFATHER%h%GODFATHER%o"
                        )
                    if not data[i].startswith(";") or not data[i].startswith("; "):
                        new = self.random_semi_and_comma(data[i])
                        data[i] = new
            if self.debug:
                with open("debug4.bat", "w", encoding="utf-8", errors="ignore") as f:
                    f.writelines(data)
            progress.update(task4, advance=100)
            if utf_16_bom and utf_16:
                out_hex = self.anti_check_error(code=data)
                with open(f"{self.file}.ultimate.bat", "wb") as f:
                    for i in out_hex:
                        f.write(bytes.fromhex(i))
            else:
                with open(
                    f"{self.file}.ultimate.bat", "w", encoding="utf-8", errors="ignore"
                ) as f:
                    for line in data:
                        f.write(line)
            progress.update(task5, advance=100)
