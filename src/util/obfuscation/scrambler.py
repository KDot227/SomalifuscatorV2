import random

from util.methods.math_methods.bit_math import Bit_Math
from util.obfuscation.obf_oneline import Obfuscate_Single
from util.methods.anti_methods.anti_changes import AntiChanges


class Scrambler:
    def __init__(self):
        pass

    def scramble(self, code: list) -> list:
        """Take a list or arrays and scramble the ones that can be scrambled. This is the main function for this class.

        Args:
            code (list): The list of arrays to scramble with identifiers

        Returns:
            list: Returns a working scrambled list
        """
        self.before_code_array = []
        self.after_code_array = []
        self.dict_parser = {}
        self.used_pointers = []
        self.bit_math = Bit_Math()
        self.code = code
        for line in self.code:
            # Do other important checks here
            if line.startswith("TO_SCRAMBLE_PLZ"):
                line2 = line.replace("TO_SCRAMBLE_PLZ", "")
                output = self.full_scramble(line2)
                self.before_code_array.append(output)
                continue
            else:
                self.before_code_array.append(line)
                continue

        if len(self.after_code_array) > 0:
            self.shuffler(self.after_code_array)

        # we need to add "goto :EOF" that way the last line of code doesn't repeat forever
        self.before_code_array.append(f"{Obfuscate_Single('goto :EOF').out()}\n")

        return self.before_code_array + self.after_code_array

    def full_scramble(self, line: str) -> str:
        """Scramble the entire line and put a pointer for the line."""

        # pointer value is our first pointer that we are saving and using as the base of the label
        pointer_value = random.randint(100000, 1000000)
        while pointer_value in self.used_pointers:
            pointer_value = pointer_value = random.randint(100000, 1000000)
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
        set_command = Obfuscate_Single(f"set /a ans={math_problem}\ngoto %ans%\n:{self.escape_label}\n").out()

        # first value we add in after code
        out_command_values = self.bit_math.generate_math_problem(self.escape_label)
        math_problem2 = out_command_values[0]
        second_set_command = Obfuscate_Single(f":{pointer_value}\n").out()
        lined = f"{line}\n"

        last = Obfuscate_Single(f"set /a ans={math_problem2}\n{self.random_anti_method()}goto %ans%\n").out()
        # we make this a array so we can scramble it later and so it won't interfere with any of the other code and stay in its own place
        label_code = [second_set_command + lined + last]

        # add the set command to the before code array
        self.after_code_array.append(label_code)

        # add the label code to the after code array
        return set_command

    def shuffler(self, list_to_shuffle: list) -> list:
        # returns the list shuffled and turned back into one list instead of a list of lists
        out_array = []
        random.shuffle(list_to_shuffle)
        for array in list_to_shuffle:
            out_array += str(array)
        return out_array

    @staticmethod
    def random_anti_method() -> str:
        random_chance = random.randint(1, 15)
        if random_chance == 1:
            return f"{AntiChanges.tests()}\n"
        return ""