from util.supporting.gens import c_val
from util.supporting.settings import log

from util.methods.common.common import *
from util.methods.encryption_methods.cesar_cypher import CaesarCipher


def ran0(char, *args, **kwargs) -> str:
    """
    This function takes a character and returns it as is.

    :param char: The character to be returned.
    :return: The input character.
    """
    return char


def ran1(char, *args, **kwargs) -> str:
    """
    This function takes a character and obfuscates it using Caesar Cipher encryption. The obfuscated character is then
    inserted into a string with a randomly generated string.

    :param char: The character to be obfuscated.
    :return: A string containing the obfuscated character and a randomly generated string.
    """
    choices = [make_random_string()]
    randomed = random.choice(choices)
    if char in string.ascii_letters:
        if char.islower():
            coded0 = CaesarCipher.get(char=char, rotation_value=c_val.value, upper=False)
            coded = coded0.replace(coded0, f"%{coded0}%")
            return f"{coded}%{randomed}%"
        else:
            coded0 = CaesarCipher.get(char=char, rotation_value=c_val.value, upper=True)
            coded = coded0.replace(coded0, f"%{coded0}1%")
            return f"{coded}%{randomed}%"
    else:
        return f"{char}%{randomed}%"


def ran2(char, random_order: str, return_ran1: bool = True, *args, **kwargs) -> str:
    """
    This function takes a character and obfuscates it using a variety of methods, including Caesar Cipher encryption and
    environment variable strings. The obfuscated character is then inserted into a string with a randomly generated
    string.

    :param char: The character to be obfuscated.
    :param random_order: A string used to seed the random number generator.
    :param return_ran1: A boolean indicating whether to return the output of ran1 if no other obfuscation method is
    applicable.
    :return: A string containing the obfuscated character and a randomly generated string.
    """
    one_in_five = random.choice([True, False, False, False, False])
    if one_in_five and char in string.ascii_letters:
        random_order_index = random_order.index(char)
        return f"%KDOT:~{random_order_index},1%"
    public = r"C:\Users\Public"
    weird = r"C:\Program Files (x86)\Common Files"
    program_1 = r"C:\Program Files"
    program_2 = r"C:\Program Files (x86)"
    driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
    pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
    CommonProgramFiles = r"C:\Program Files\Common Files"
    CommonProgramFiles_x86 = r"C:\Program Files (x86)\Common Files"
    CommonProgramW6432 = r"C:\Program Files\Common Files"
    # __APPDIR__ = "C:\\WINDOWS\\system32\\"
    list_of_all = [
        public,
        weird,
        program_1,
        program_2,
        driver_stuff,
        pathext,
        CommonProgramFiles,
        CommonProgramFiles_x86,
        CommonProgramW6432,
        # __APPDIR__,
    ]
    corosponding = [
        "PUBLIC",
        "COMMONPROGRAMFILES(X86)",
        "PROGRAMFILES",
        "PROGRAMFILES(X86)",
        "DRIVERDATA",
        "PATHEXT",
        "COMMONPROGRAMFILES",
        "COMMONPROGRAMFILES(X86)",
        "COMMONPROGRAMW6432",
        # "__APPDIR__",
    ]
    new_lists = []
    char_counter = 0
    for i in list_of_all:
        if char in i:
            new_lists.append(i)
            char_counter += i.count(char)
    random_posotive_negative = False
    if len(new_lists) > 0:
        if char == " ":
            return char
        new = random.choice(new_lists)
        if char not in string.ascii_letters:
            return char
        if char in new:
            if random_posotive_negative:
                random_index = random.choice([i for i, letter in enumerate(new) if letter == char])
                new2 = corosponding[list_of_all.index(new)]
                negative_index = random_index - len(new)
                return f"%{random_capitalization(new2)}:~{negative_index},1%"
            else:
                random_index = random.choice([i for i, letter in enumerate(new) if letter == char])
                new = corosponding[list_of_all.index(new)]
                return f"%{random_capitalization(new)}:~{random_index},1%"
    else:
        if return_ran1:
            return ran1(char)
        else:
            if char not in string.ascii_letters:
                return char
            random_order_index = random_order.index(char)
            return f"%KDOT:~{random_order_index},1%"


def ran3(char, random_order: str, *args, **kwargs) -> str:
    """
    This function generates a random path and corresponding environment variable, and uses them to create a valid
    environment variable string. It also randomly selects one of three other functions (ran0, ran1, or ran2) to
    generate a string of obfuscated code, which is then inserted into the environment variable string.

    :param char: The character to be obfuscated.
    :param random_order: A string used to seed the random number generator.
    :return: A string containing a valid environment variable with obfuscated code inserted.
    """
    allowed_chars = string.ascii_letters + string.digits + "():\\"

    public = r"C:\Users\Public"
    weird = r"C:\Program Files (x86)\Common Files"
    program_1 = r"C:\Program Files"
    program_2 = r"C:\Program Files (x86)"
    driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
    pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
    CommonProgramFiles = r"C:\Program Files\Common Files"
    CommonProgramFiles_x86 = r"C:\Program Files (x86)\Common Files"
    CommonProgramW6432 = r"C:\Program Files\Common Files"
    list_of_all = [
        public,
        weird,
        program_1,
        program_2,
        driver_stuff,
        pathext,
        CommonProgramFiles,
        CommonProgramFiles_x86,
        CommonProgramW6432,
    ]
    corosponding = [
        "PUBLIC",
        "COMMONPROGRAMFILES(X86)",
        "PROGRAMFILES",
        "PROGRAMFILES(X86)",
        "DRIVERDATA",
        "PATHEXT",
        "COMMONPROGRAMFILES",
        "COMMONPROGRAMFILES(X86)",
        "COMMONPROGRAMW6432",
    ]

    # Select a random path and corresponding environment variable
    random_path = random.choice(corosponding)
    corosponding_index = corosponding.index(random_path)
    out = list_of_all[corosponding_index]

    # Select a random obfuscation function
    random_ran = random.choice(
        [
            ran0,
            ran1,
            ran2,
        ]
    )

    if not char in allowed_chars:
        # %public:C:\Users\Public=echo test%
        random_corosponding = random.choice(corosponding)
        coro_index = corosponding.index(random_corosponding)
        all_list = list_of_all[coro_index]
        out_start = f"%{random_corosponding}:{all_list}={char}%"
        log.debug("ran3")
        return out_start

    # Generate obfuscated code

    good_code = random_ran(char=char, return_ran1=False, random_order=random_order)

    # If the obfuscated code doesn't start with '%', generate a new string of obfuscated code
    if not good_code.startswith("%"):
        return ran2(char=char, return_ran1=True, random_order=random_order)

    # Create a valid environment variable string with the obfuscated code inserted
    valid_text = f"%{random_path}:{out}=%{good_code}"
    return valid_text


def ran4(char, *args, **kwargs) -> str:
    pass
