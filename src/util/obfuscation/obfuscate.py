import os
import re
import random
import string

from util.obfuscation.obf_oneline import Obfuscate_Single
from util.obfuscation.rans import ran1, ran2
from util.obfuscation.scrambler import Scrambler
from util.obfuscation.null_parser import NullParse

from util.supporting.gens import c_val
from util.supporting.settings import log, Settings
from util.supporting.types import Code_Block

from util.methods.anti_methods.anti_changes import AntiChanges
from util.methods.anti_methods.anti_s_screen import AntiSScreen
from util.methods.anti_methods.anti_console import AntiConsole

from util.methods.common.common import make_random_string, random_capitalization, pogdog

from util.methods.encryption_methods.cesar_cypher import CaesarCipher

from util.methods.dead_code.dead_code import DeadCode

letter_assignments_cypher = CaesarCipher.both(c_val.value)

code1 = f"%TO_SCRAMBLE_PLZ%@echo off"
code2 = f"{CaesarCipher.both(c_val.value)}"
code3 = "%TO_SCRAMBLE_PLZ%chcp 65001 > nul"

# %TO_SCRAMBLE_PLZ%


class Obfuscator:
    def __init__(
        self,
        file: str,
        double_click_check: bool = True,
        utf_16_bom: bool = True,
    ) -> None:
        self.new_file = f"{file[:-4]}_obf.bat"
        self.double_click = double_click_check
        self.utf_16_bom = utf_16_bom

        self.echo_var = "@echo off" if not Settings.debug else "@echo on"

        self.obfuscate(file)

    @staticmethod
    def random_spinners() -> str:
        spinners = [
            "aesthetic",
            "betaWave",
            "bounce",
            "bouncingBall",
            "bouncingBar",
            "material",
            "pong",
            "shark",
        ]

        return random.choice(spinners)

    # make reutrn bytes later
    def obfuscate(self, file):
        try:
            os.remove(f"{self.new_file}")
        except FileNotFoundError:
            log.warning("No Obfuscated file found, creating one...")

        with open(file, "r", encoding="utf8", errors="ignore") as f:
            self.data = f.readlines()
            # replace all instances of @echo off with the echo var
            if Settings.debug:
                self.data = [s.replace("@echo off", self.echo_var) for s in self.data]
            if Settings.remove_blank_lines:
                self.data = list(filter(lambda x: x.strip() != "", self.data))

        self.cesar_value = c_val.value

        self.ran_string_1 = make_random_string(special_chars=False)

        # FOMAT CODE HERE

        # fmt: off
        self.common_env_vars = [
            r"%ALLUSERSPROFILE%", r"%APPDATA%", r"%CD%", r"%CMDCMDLINE%", r"%CMDEXTVERSION%", r"%COMPUTERNAME%", r"%COMSPEC%", r"%DATE%", r"%ERRORLEVEL%", r"%HOMEDRIVE%", r"%HOMEPATH%", r"%NUMBER_OF_PROCESSORS%", r"%OS%", r"%PATH%", r"%PATHEXT%", r"%PROCESSOR_ARCHITECTURE%", r"%PROCESSOR_LEVEL%", r"%PROCESSOR_REVISION%", r"%PROMPT%", r"%RANDOM%", r"%SYSTEMDRIVE%", r"%SYSTEMROOT%", r"%TMP%", r"%TEMP%", r"%TIME%", r"%USERDOMAIN%", r"%USERNAME%", r"%USERPROFILE%", r"%WINDIR%",  r"%localappdata%",
            r"%0", r"%1", r"%2", r"%3", r"%4", r"%5", r"%6", r"%7", r"%8", r"%9", r"%*", r"%~dp0", r"%~dp1", r"%~dp2", r"%~dp3", r"%~dp4", r"%~dp5", r"%~dp6", r"%~dp7", r"%~dp8", r"%~dp9", r"%~f0", r"%~f1", r"%~f2", r"%~f3", r"%~f4", r"%~f5", r"%~f6", r"%~f7", r"%~f8", r"%~f9", r"%~nx0", r"%~nx1", r"%~nx2", r"%~nx3", r"%~nx4", r"%~nx5", r"%~nx6", r"%~nx7", r"%~nx8", r"%~nx9", r"%~s0", r"%~s1", r"%~s2", r"%~s3", r"%~s4", r"%~s5", r"%~s6", r"%~s7", r"%~s8", r"%~s9", r"%~t0", r"%~t1", r"%~t2", r"%~t3", r"%~t4", r"%~t5", r"%~t6", r"%~t7", r"%~t8", r"%~t9", r"%~x0", r"%~x1", r"%~x2", r"%~x3", r"%~x4", r"%~x5", r"%~x6", r"%~x7", r"%~x8", r"%~x9", r"%~a0",
            r"%~dpn0",r"%~dpnx0",
        ]
        # fmt: on

        self.used_env_vars = []

        for line in self.data:
            if any(env_var.lower() in line.lower() for env_var in self.common_env_vars):
                self.used_env_vars.append(
                    [
                        env_var
                        for env_var in self.common_env_vars
                        if env_var.lower() in line.lower()
                    ][0]
                )

        with open(self.new_file, "a+", encoding="utf8", errors="ignore") as f:
            f.write(random_capitalization("\n::Made by K.Dot using SomalifuscatorV2\n"))
            # f.write(
            #    "REM \xff\xfeS\x00o\x00m\x00a\x00l\x00i\x00f\x00u\x00s\x00c\x00a\x00t\x00o\x00r\x00 \x00i\x00s\x00 \x00v\x00e\x00r\x00y\x00 \x00c\x00o\x00o\x00l\x00 \x00m\x00y\x00 \x00b\x00r\x00o\x00t\x00h\x00a\x00 \x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00l\x00o\x00l\x00"
            # )
            characters = string.ascii_letters + string.digits
            random_order = "".join(random.sample(characters, len(characters)))

            f.write(
                Obfuscate_Single(code1.replace("@echo off", self.echo_var)).out() + "\n"
            )
            f.write(Obfuscate_Single(code2).out() + "\n")
            f.write(Obfuscate_Single(code3).out() + "\n")

            f.write(
                Obfuscate_Single(f"%TO_SCRAMBLE_PLZ%set KDOT={random_order}").out()
                + "\n"
            )

            regex_bat = re.compile(r"\w+=[^=]*%\w+%\b|\w+=[^=]*%\w+%\B")
            regex2 = re.compile(r"%(\w+)%")
            regex_batch_variable = re.compile(r"(?<!\\)%[^%\s]+%")
            escape_regex = re.compile(r"%escape%", re.IGNORECASE)

            for index, line in enumerate(self.data):
                log.debug(f"Processing line {index}")
                echo_check123 = False
                try:
                    if r"%errorlevel%" in self.data[index - 1].lower():
                        echo_check123 = True
                except IndexError:
                    pass
                if r"%errorlevel%" in line.lower():
                    echo_check123 = True
                try:
                    if r"%errorlevel%" in self.data[index + 1].lower():
                        echo_check123 = True
                except IndexError:
                    pass

                indents = False
                try:
                    # check if the previous line starts with a space or a tab
                    if self.data[index - 1].startswith(" ") or self.data[
                        index - 1
                    ].startswith("\t"):
                        indents = True
                except IndexError:
                    pass
                if self.data[index].startswith(" ") or self.data[index].startswith(
                    "\t"
                ):
                    indents = True
                try:
                    if self.data[index + 1].startswith(" ") or self.data[
                        index + 1
                    ].startswith("\t"):
                        indents = True
                except IndexError:
                    pass

                random_change_code = random.choice(range(1, 5))

                if random_change_code == 1 and not echo_check123 and not indents:
                    log.debug("Random change code True")
                    letter_assignments_cypher = CaesarCipher.both(c_val.value)
                    f.write(
                        Obfuscate_Single(letter_assignments_cypher, simple=False).out()
                        + "\n"
                    )

                random_dead_code = random.choice(range(1, 2))
                if random_dead_code == 1 and not echo_check123 and not indents:
                    log.debug("Random dead code True")
                    f.write(Obfuscate_Single(DeadCode().dead_code() + "\n").out())

                if line.startswith("::"):
                    log.debug("Comment True")
                    f.write(line + "\n")
                    continue

                elif line.startswith(":"):
                    log.debug("Label True")
                    f.write(line + "\n")
                    continue

                else:
                    for word in line.split():
                        # check if any of self.used_env_vars are in the line
                        if re.search(escape_regex, word):
                            log.debug("escape True")
                            f.write(word + " ")
                            continue

                        elif any(
                            env_var.lower() in word.lower()
                            for env_var in self.used_env_vars
                        ):
                            log.debug("env var True")
                            f.write(word + " ")
                            continue

                        elif re.search(regex_batch_variable, word):
                            # had to bust out chat gpt for this one
                            log.debug("ai is better than me")
                            f.write(word + " ")
                            continue

                        elif (
                            word.startswith(r"%")
                            or word.startswith(r"!")
                            or r"%%" in word
                        ):
                            log.debug("var True")
                            f.write(word + " ")
                            continue

                        elif "%~" in word:
                            log.debug("bat env var True")
                            f.write(word + " ")
                            continue

                        elif re.search(regex_bat, word):
                            log.debug("Regex True")
                            f.write(word + " ")
                            continue

                        elif re.search(regex2, word):
                            log.debug("regex2 True")
                            f.write(word + " ")
                            continue

                        elif word.startswith(":") and not word.startswith("::"):
                            log.debug("label True")
                            f.write(word + " ")
                            continue

                        else:
                            for char in word:
                                if char == "\n":
                                    f.write("\n")
                                    continue

                                elif char == " ":
                                    f.write(" ")

                                else:
                                    random_obf = [
                                        ran1(char),
                                        ran2(char, random_order=random_order),
                                    ]
                                    f.write(random.choice(random_obf))
                                    # f.write(char)
                            f.write(" ")
                    f.write(" ")
                f.write("\n")
            f.close()

            log.info(
                "Finished writing out code", extra={"highlighter": None, "markup": True}
            )

            # I could have just use an array for all of this but I like the readability of just writing to files and how easy it is. I could have also used touples but idc that much
            current_code = self.get_current_code()

            current_code.insert(
                1,
                Obfuscate_Single(
                    AntiChanges.first_line_echo_check(), simple=False
                ).out(),
            )

            # current_code = AntiChanges.ads_spammer(current_code)

            scrambler = Scrambler()
            fuck_up_code = scrambler.scramble(current_code)
            # fuck_up_code = current_code

            # progress.update(task2, advance=100)
            log.info(f"Finished scrambling {len(current_code)} arrays")

            out = [
                Obfuscate_Single(f"{self.echo_var}\n", simple=False).out()
            ] + fuck_up_code

            if Settings.hidden:
                out = AntiConsole.main(out)

            if Settings.bloat and not Settings.debug:
                out = pogdog(out)

            if not Settings.debug and self.utf_16_bom:
                out = [
                    f"{Obfuscate_Single('>nul 2>&1 && exit >nul 2>&1 || cls').out()}\n"
                ] + out
                self.convert_code_chunk_and_write_bytes(out)
            else:
                self.write_code_chunk(out)

            # progress.update(task3, advance=100)
            log.info("Finished writing out Bytes!")

            if Settings.smartscreen_bypass:
                out_path = self.new_file.split(".")[0][:-4] + ".rar"
                AntiSScreen(self.new_file).pack_file(out_path)
                os.remove(self.new_file)
            return 0

    def get_current_code(self) -> list:
        """Get's current code from the new file

        Returns:
            list: returns the current code
        """
        with open(self.new_file, "r+", encoding="utf8", errors="ignore") as f:
            current_code = f.readlines()
        return current_code

    def write_code_chunk(self, code_chunk: list) -> None:
        """Writes code chunk to the new file

        Args:
            code_chunk (list): Code chunk to write
        """
        with open(self.new_file, "w+", encoding="utf8", errors="ignore") as f:
            for array in code_chunk:
                f.writelines(array)

    def convert_code_chunk_and_write_bytes(self, code_chunk: Code_Block) -> None:
        out_hex = ["FF", "FE"]

        self.write_code_chunk(code_chunk)

        with open(self.new_file, "rb") as f:
            code = f.read()

        code = bytes.fromhex("".join(out_hex)) + code

        with open(self.new_file, "wb") as f:
            f.write(code)

    @staticmethod
    def add_scramble(code) -> str:
        if isinstance(code, list):
            for index, item in enumerate(code):
                # replace the string with %TO_SCRAMBLE_PLZ% + the string and apply it to add_scramble
                item = item.replace(item, "%TO_SCRAMBLE_PLZ%" + item)
                code[index] = item
            return "\n".join(code)
        else:
            code = code.split("\n")
            for index, item in enumerate(code):
                # replace the string with %TO_SCRAMBLE_PLZ% + the string and apply it to add_scramble
                item = item.replace(item, "%TO_SCRAMBLE_PLZ%" + item)
                code[index] = item
            return "\n".join(code)


if __name__ == "__main__":
    print(
        "KDot this is a message to yourself to grow a brain and stop running the wrong file."
    )
    os._exit(1)
