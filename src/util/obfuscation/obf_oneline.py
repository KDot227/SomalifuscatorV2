import re
import random

from typing import List, Union, NewType

from util.supporting.settings import Settings
from util.supporting.types import Obfuscated_String

from util.methods.common.common import make_random_string, random_capitalization
from util.methods.custom.decorators.custom_decorators import check_string_length


class Obfuscate_Single:
    def __init__(
        self,
        code: Union[str, List[str]],
        simple: bool = False,
        ignore_carrots: bool = False,
    ) -> None:
        self.code = code
        self.simple = simple
        self.ignore_carrots = ignore_carrots
        self.out_code = ""

    @check_string_length
    def out(self) -> Obfuscated_String:
        if Settings.debug:
            return self.code
        """returns the desired obfuscated code

        Returns:
            str: desired obfuscated code
        """
        if isinstance(self.code, list):
            if self.simple:
                for line in self.code:
                    if "%TO_SCRAMBLE_PLZ%" in line:
                        line = line.replace("%TO_SCRAMBLE_PLZ%", "")
                        self.out_code += (
                            "%TO_SCRAMBLE_PLZ%" + self.obfuscate_simple(line) + "\n"
                        )
                    else:
                        self.out_code += self.obfuscate_simple(line) + "\n"
                return self.out_code
            else:
                for line in self.code:
                    if "%TO_SCRAMBLE_PLZ%" in line:
                        line = line.replace("%TO_SCRAMBLE_PLZ%", "")
                        self.out_code += (
                            "%TO_SCRAMBLE_PLZ%" + self.obfuscate_normal(line) + "\n"
                        )
                    else:
                        self.out_code += self.obfuscate_normal(line) + "\n"
                return self.out_code
        else:
            if self.simple:
                if self.code.count("\n") > 1:
                    self.code = self.code.splitlines()
                    for line in self.code:
                        if "%TO_SCRAMBLE_PLZ%" in line:
                            line = line.replace("%TO_SCRAMBLE_PLZ%", "")
                            self.out_code += (
                                "%TO_SCRAMBLE_PLZ%" + self.obfuscate_simple(line) + "\n"
                            )
                        else:
                            self.out_code += self.obfuscate_simple(line) + "\n"
                    return self.out_code
                if "%TO_SCRAMBLE_PLZ%" in self.code:
                    self.code = self.code.replace("%TO_SCRAMBLE_PLZ%", "")
                    return "%TO_SCRAMBLE_PLZ%" + self.obfuscate_simple(self.code) + "\n"
                else:
                    return self.obfuscate_simple(self.code) + "\n"
            else:
                if self.code.count("\n") > 1:
                    self.code = self.code.splitlines()
                    for line in self.code:
                        if "%TO_SCRAMBLE_PLZ%" in line:
                            line = line.replace("%TO_SCRAMBLE_PLZ%", "")
                            self.out_code += (
                                "%TO_SCRAMBLE_PLZ%" + self.obfuscate_normal(line) + "\n"
                            )
                        else:
                            self.out_code += self.obfuscate_normal(line) + "\n"
                    return self.out_code
                if "%TO_SCRAMBLE_PLZ%" in self.code:
                    self.code = self.code.replace("%TO_SCRAMBLE_PLZ%", "")
                    return "%TO_SCRAMBLE_PLZ%" + self.obfuscate_normal(self.code) + "\n"
                else:
                    return self.obfuscate_normal(self.code) + "\n"

    def obfuscate_normal(self, line: str) -> Obfuscated_String:
        if Settings.FUD:
            return self.obfuscate_simple(line)
        """Obfuscates code but this method is very simple and made for small lines of code that needs to be obfuscated

        Args:
            line (str): line to be obfuscated

        Returns:
            str: returns obfuscated line
        """
        line = line.strip()
        final_string = ""
        regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")
        regex2 = re.compile(r"%(\w+)%")
        for index, word in enumerate(line.split()):
            if index == 0:
                word = random_capitalization(word)
            if word.startswith("%"):
                final_string += f"{word} "
                continue
            if word.find("%~") != -1:
                final_string += f"{word} "
                continue
            if word.startswith("^") and not self.ignore_carrots:
                final_string += f"{word} "
                continue
            if word.startswith("::"):
                continue
            if word.startswith(":"):
                final_string += f"{word} "
                continue
            if re.match(regex_bat, word):
                final_string += f"{word} "
                continue
            if re.match(regex2, word):
                final_string += f"{word} "
                continue
            else:
                public = r"C:\Users\Public"
                weird = r"C:\Program Files (x86)\Common Files"
                program_1 = r"C:\Program Files"
                program_2 = r"C:\Program Files (x86)"
                driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
                # pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
                CommonProgramFiles = r"C:\Program Files\Common Files"
                CommonProgramW6432 = r"C:\Program Files\Common Files"
                # __APPDIR__ = "C:\\Windows\\system32\\"

                options = {
                    public: "PUBLIC",
                    weird: "COMMONPROGRAMFILES(X86)",
                    program_1: "PROGRAMFILES",
                    program_2: "PROGRAMFILES(X86)",
                    driver_stuff: "DRIVERDATA",
                    # pathext: "PATHEXT",
                    CommonProgramFiles: "COMMONPROGRAMFILES",
                    CommonProgramW6432: "COMMONPROGRAMW6432",
                    # __APPDIR__: "__APPDIR__",
                }

                for index, char in enumerate(word):
                    random_chance = random.choice([True, False])

                    if random_chance:
                        final_string += self.obfuscate_simple(char)
                        continue

                    new_lists = list(options)
                    random_posotive_negative = random.choice([True, False])

                    filtered_lists = [i for i in new_lists if char in i]

                    if len(filtered_lists) == 0:
                        final_string += (
                            f"{char}%{make_random_string(special_chars=False)}%"
                        )
                        continue

                    new = random.choice(filtered_lists)

                    if random_posotive_negative:
                        ammount = [i for i, letter in enumerate(new) if letter == char]
                        random_index = random.choice(ammount)
                        new2 = options[new]
                        negative_index = random_index - len(new)
                        final_string += (
                            f"%{random_capitalization(new2)}:~{negative_index},1%"
                        )
                    else:
                        ammount = [i for i, letter in enumerate(new) if letter == char]
                        random_index = random.choice(ammount)
                        new2 = options[new]
                        final_string += (
                            f"%{random_capitalization(new2)}:~{random_index},1%"
                        )
            final_string += " "
        return final_string

    def obfuscate_simple(self, char_line: str) -> Obfuscated_String:
        """Very simple obfuscated method for chars that aren't in any arrays

        Args:
            char_line (str): line to obf / char to obf
        Returns:
            str: returns obfuscated line / char
        """
        # return char_line
        char_line = char_line.strip()
        if len(char_line) == 1:
            return f"%{make_random_string((7, 9), special_chars=False)}%{char_line}%{make_random_string((7, 9), special_chars=False)}%"
        final_string = ""
        regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")
        regex2 = re.compile(r"%(\w+)%")
        for word in char_line.split():
            if word.startswith("%TO_SCRAMBLE_PLZ%"):
                final_string += f"{word} "
            elif word.startswith(":"):
                final_string += f"{word} "
            elif word.startswith("%"):
                final_string += f"{word} "
            elif word.find("%~") != -1:
                final_string += f"{word} "
            elif word.startswith("^") and not self.ignore_carrots:
                final_string += f"{word} "
            elif word.startswith("::"):
                pass
            elif re.match(regex_bat, word):
                final_string += f"{word} "
            elif re.match(regex2, word):
                final_string += f"{word} "
            else:
                for char in word:
                    final_string += f"%{make_random_string((7, 9), special_chars=False)}%{char}%{make_random_string((7, 9), special_chars=False)}%"
            final_string += " "
        return final_string
