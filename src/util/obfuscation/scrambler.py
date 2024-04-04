import re
import random

from util.methods.math_methods.bit_math import Bit_Math
from util.obfuscation.obf_oneline import Obfuscate_Single
from util.methods.anti_methods.anti_changes import AntiChanges

from util.methods.common.common import (
    random_semi_and_comma,
    random_single_carrot,
    random_capitalization,
    random_spaces,
)

from util.supporting.settings import log
from util.supporting.types import Code_Block


class Scrambler:
    def __init__(self):
        self.scramble_regex = r":[0-9]+"

    def scramble(self, code: list, checks: bool = True) -> Code_Block:
        """Take a list or arrays and scramble the ones that can be scrambled. This is the main function for this class.

        Args:
            code (list): The list of arrays to scramble with identifiers

        Returns:
            list: Returns a working scrambled list
        """
        self.checks = checks
        self.before_code_array = []
        self.after_code_array = []
        self.dict_parser = {}
        self.used_pointers = []
        self.bit_math = Bit_Math()
        self.code = code
        for line in self.code:
            # Do other important checks here
            if line.startswith("%TO_SCRAMBLE_PLZ%"):
                line2 = line.replace("%TO_SCRAMBLE_PLZ%", "")
                output = self.full_scramble(line2)
                self.before_code_array.append(output)
                continue
            else:
                self.before_code_array.append(line)
                continue

        if len(self.after_code_array) > 0:
            self.shuffler(self.after_code_array)

        # we need to add "goto :EOF" that way the last line of code doesn't repeat forever
        self.before_code_array.append("goto :EOF\n")

        self.after_code_array = self.flood(self.after_code_array)

        return self.before_code_array + self.after_code_array

    def full_scramble(self, line: str) -> str:
        """Scramble the entire line and put a pointer for the line."""

        # pointer value is our first pointer that we are saving and using as the base of the label
        pointer_value = random.randint(100000, 1000000)
        while pointer_value in self.used_pointers:
            pointer_value = random.randint(100000, 1000000)
        self.used_pointers.append(pointer_value)

        # the escape label is the label that we are using to go back to the normal part of our script after we are done with the scrambled part
        self.escape_label = random.randint(100000, 1000000)
        while self.escape_label in self.used_pointers:
            self.escape_label = random.randint(100000, 1000000)
        self.used_pointers.append(self.escape_label)

        # first value we add in before code
        set_command_values = self.bit_math.generate_math_problem(pointer_value)
        math_problem = set_command_values[0]

        # first value we add in before code this goes to the code and allows it to go back to the normal part of the script
        set_command = Obfuscate_Single(
            f"s{random_single_carrot('et')}{Scrambler.random_single_space()}/{random_single_carrot('a')} a{random_single_carrot(random_capitalization('ns') + '=')}{math_problem}\ng{random_single_carrot(random_capitalization('oto'))} {random_semi_and_comma()} %{random_capitalization('ans')}%\n:{self.escape_label}\n",
            simple=False,
        ).out()

        # first value we add in after code
        out_command_values = self.bit_math.generate_math_problem(self.escape_label)
        math_problem2 = out_command_values[0]
        second_set_command = Obfuscate_Single(f":{pointer_value}\n", simple=False).out()
        lined = f"{line}\n"

        if self.checks:
            last = Obfuscate_Single(
                f"set /a ans={math_problem2}\n{self.random_anti_method()}goto %ans%\n",
                simple=False,
            ).out()
        else:
            last = Obfuscate_Single(
                f"set /a ans={math_problem2}\ngoto %ans%\n", simple=False
            ).out()
        # we make this a array so we can scramble it later and so it won't interfere with any of the other code and stay in its own place
        label_code = [second_set_command + lined + last]

        # add the set command to the before code array
        self.after_code_array.append(label_code)

        # add the label code to the after code array
        return set_command

    def shuffler(self, list_to_shuffle: list) -> list:
        # returns the list shuffled and turned back into one list instead of a list of lists
        out_array = random.sample(list_to_shuffle, len(list_to_shuffle))
        return [str(array) for array in out_array]

    def flood(self, code_arrays: list) -> list:
        self.good_values = {}
        for index, array in enumerate(code_arrays):
            main_string = array[0].splitlines()
            for sub_string in main_string:
                # see if self.scramble_regex matches the sub_string
                if not re.match(self.scramble_regex, sub_string):
                    continue
                # last line has a space and we dont be liking that
                self.good_values[index] = sub_string[:-1]
        for key, value in self.good_values.items():
            key_range = list(range(key + 1, len(code_arrays)))
            if len(key_range) <= 3:
                continue
            # add value to random values in code_arrays that appear in the key range
            random_ammount = random.randint(1, 3)
            for _ in range(random_ammount):
                random_index = random.choice(key_range)
                code_arrays[random_index].append(value + "\n")
        return code_arrays

    @staticmethod
    def random_anti_method() -> str:
        random_chance = random.randint(1, 3)
        if random_chance == 1:
            use = AntiChanges.tests()
            log.debug(f"Using {use[1]} as anti method")
            return f"{use[0]}\n"
        return ""

    @staticmethod
    def random_single_space() -> str:
        random_chance = random.randint(1, 5)
        if not random_chance == 1:
            return " "
        return ""
