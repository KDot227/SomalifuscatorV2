import re
import random

from util.methods.common.common import (
    random_capitalization,
    all_,
    pogdog,
    make_random_label_no_working,
    make_random_string,
)

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

        # for some reason I have to use simple here not too sure why but it works so I'm not gonna question it
        last = Obfuscate_Single(f"set /a ans={math_problem2}\ngoto %ans%\n").out()
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

    # def insert_random_lablels(self, code: list) -> list:
    #    for index, line in enumerate(code):
    #        echo_check123 = False
    #        try:
    #            if r"%errorlevel%" in code[index - 1].lower():
    #                echo_check123 = True
    #        except IndexError:
    #            pass
    #        # This should never have an index error since it's the current itteration in the list
    #        # if it does get an error then u got other issues. Also at that point dont make an issue just pray to god (or whoever or dont pray idc) and restart ur pc
    #        if r"%errorlevel%" in line.lower():
    #            echo_check123 = True
    #        try:
    #            if r"%errorlevel%" in code[index + 1].lower():
    #                echo_check123 = True
    #        except IndexError:
    #            pass
    #        if not echo_check123:
    #            random_number = random.randint(1, 4)
    #            if random_number == 1:
    #                # add a label that doesn't do anything
    #                label = f":{make_random_label_no_working()}\n"
    #                code.insert(index, label)
    #    return code

    # def random_inserts(self, main_list):
    #    listes = [
    #        ";::Made by K.Dot and Godfather\n",
    #        ";::Good luck deobfuscating\n",
    #        ";::Made with Somalifuscator\n",
    #        ";::discord.gg/batch\n",
    #        ";::... --- -- .- .-.. .. ..-. ..- ... -.-. .- - --- .-. / --- -. / - --- .--.\n",
    #    ]
    #    for i in range(len(main_list)):
    #        if i == 0:
    #            continue
    #        else:
    #            random_int = random.randint(1, 10)
    #            if random_int == 10:
    #                list_choice = random_capitalization(random.choice(listes))
    #                main_list.insert(i, [list_choice])


#
#    return main_list
#
# def random_dead_code(self, entire_array):
#    """Dead code that just won't be executed so it can be whatever. If u wanna add more its all u"""
#    dead_code = [
#        "echo Best Batch Obfuscated By K.Dot and Godfather\n",
#        "if 0 == 0 (echo Best Batch Obfuscated By K.Dot and Godfather)\n",
#        # f"set KDOT={''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))}\n",
#        # f"{CaesarCipher('both', random.randint(1, 13)).out()}\n",
#        f"set somalifuscator=op_asf\n",
#    ]
#    for array in entire_array:
#        if random.randint(0, 3) == 3:
#            option = random.choice(dead_code)
#            scated = Obfuscate_Single(option).out()
#            new_string = "".join(scated)
#            new_string = [new_string]
#            entire_array.insert(entire_array.index(array), new_string)
#
#    return entire_array
#
# def bad_labels_and_dead_code(self, main_list):
#    """inserts labels that are valid but won't do anything since they have a zero width space infront. This mainly messes up looking at it from a text editor. You can still goto it if you use the weird translated bytes."""
#    main_dict = self.dict_assigner.copy()
#    new_list = []
#    types = [True, False]
#    doskey_options = [
#        "dir",
#        "echo",
#        "for",
#        "if",
#        "set",
#        "goto",
#        "cd",
#        "",
#    ]
#    bad_insert = "GODFATHER"
#    for item in main_dict.values():
#        strung = str(item[1])
#        strung = ";:" + bad_insert + strung
#        new_list.append(strung)
#    for array in main_list:
#        # if next word contains %errorlevel% in lowercase in current itteration then skip
#        if r"%errorlevel%" in array[0].lower():
#            pass
#        else:
#            random_choci = random.choice(types)
#            if random_choci:
#                random_chance = random.randint(1, 3)
#                if random_chance == 5:
#                    random_label = random.choice(new_list)
#                    random_place = random.randint(0, len(array))
#                    array.insert(random_place, random_label + "\n")
#            else:
#                doskey = f"doskey {random.choice(doskey_options)}={random.choice(doskey_options)}\n"
#                array.append(Obfuscate_Single(doskey).out())
#    return main_list
#
# def deadcodes(self, good_label, bad_label):
#    """not really deadcode but it just makes it hard for kids to understand"""
#    RANNUM = random.randint(32769, 99999)
#    examples = [
#        f"if %random% equ {RANNUM} ( goto :{bad_label} ) else ( goto :{good_label} )",
#        f"if not 0 neq 0 ( goto :{good_label} ) else ( goto :{bad_label} )",
#        f"if exist C:\Windows\System32 ( goto :{good_label} ) else ( goto :{bad_label} )",
#        f"if not %cd% == %cd% ( goto :{bad_label} ) else ( goto :{good_label} )",
#        f"if 0 equ 0 ( goto :{good_label} ) else ( goto :{bad_label} )",
#        f"if exist C:\Windows\System3 ( goto :{bad_label} ) else ( goto :{good_label} )",
#        f"if %cd% == %cd% ( goto :{good_label} ) else ( goto :{bad_label} )",
#        f"if chcp leq 1 ( goto :{bad_label} ) else ( goto :{good_label} )",
#        f"if %CD% == %__CD__% ( goto :{bad_label} ) else ( goto :{good_label} )",
#    ]
#    code_examples = [
#        "::Made with somalifuscator",
#        "::discord.gg/batch",
#        "::https://sped.lol",
#        "::KDot > Batch",
#    ]
#    random_maybe = random.choice([True, False])
#    if random_maybe:
#        coded = f"{random_capitalization(random.choice(code_examples))} ^\n {random.choice(examples)} ^\n exit /b 0\n{random.choice(examples)}"
#        for _ in range(3):
#            examples.append(coded)
#    else:
#        coded = f"{random_capitalization(random.choice(code_examples))} ^\n exit /b 0\n {random.choice(examples)}"
#        for _ in range(3):
#            examples.append(coded)
#
#    randomed = random.choice(examples)
#    obfuscated = Obfuscate_Single(randomed).out()
#    return obfuscated + "\n"
