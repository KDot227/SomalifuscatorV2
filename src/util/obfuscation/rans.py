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
            coded0 = CaesarCipher.get(
                char=char, rotation_value=c_val.value, upper=False
            )
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

    public = "C:\\Users\\Public"
    weird = "C:\\Program Files (x86)\\Common Files"
    program_1 = "C:\\Program Files"
    program_2 = "C:\\Program Files (x86)"
    driver_stuff = "C:\\Windows\\System32\\Drivers\\DriverData"
    # pathext = ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
    CommonProgramFiles = "C:\\Program Files\\Common Files"
    CommonProgramFiles_x86 = "C:\\Program Files (x86)\\Common Files"
    CommonProgramW6432 = "C:\\Program Files\\Common Files"

    key_vars = {
        "PUBLIC": (public, "None"),
        "COMMONPROGRAMFILES(X86)": (weird, "None"),
        "PROGRAMFILES": (program_1, "None"),
        "PROGRAMFILES(X86)": (program_2, "None"),
        "DRIVERDATA": (driver_stuff, "None"),
        # "PATHEXT": (pathext, "None"),
        "COMMONPROGRAMFILES": (CommonProgramFiles, "None"),
        "COMMONPROGRAMFILES(X86)": (CommonProgramFiles_x86, "None"),
        "COMMONPROGRAMW6432": (CommonProgramW6432, "None"),
        "USERPROFILE": ("C:\\Users\\", "R"),
        "TEMP": ("\\AppData\\Local\\Temp", "L"),
        "TMP": ("\\AppData\\Local\\Temp", "L"),
        "LOCALAPPDATA": ("\\AppData\\Local", "L"),
        "APPDATA": ("\\AppData\\Roaming", "L"),
        # "ONEDRIVE": ("\\OneDrive", "L"),
        # "ONEDRIVECONSUMER": ("\\OneDrive", "L"),
        "OS": ("Windows_NT", "None"),
        "SYSTEMDRIVE": ("C:", "None"),
    }

    if Settings.double_click_check:
        key_vars["SESSIONNAME"] = ("Console", "None")

    # see if the first value of any of the keys contains the char
    possible_vars = []
    for key, value in key_vars.items():
        if char in value[0]:
            possible_vars.append(key)
    if len(possible_vars) > 0:
        random_var = random.choice(possible_vars)
        value, modifier = key_vars[random_var]
        valid_indexs = [i for i, letter in enumerate(value) if letter == char]
        if modifier == "None":
            # NONE means both work
            positive_index = random.choice([True, False])
            if positive_index:
                random_positive_index = random.choice(valid_indexs)
                return f"%{random_var}:~{random_positive_index},1%"
            else:
                random_positive_index = random.choice(valid_indexs)
                negative_index = random_positive_index - len(value)
                return f"%{random_var}:~{negative_index},1%"
        elif modifier == "R":
            random_positive_index = random.choice(valid_indexs)
            return f"%{random_var}:~{random_positive_index},1%"

        elif modifier == "L":
            random_positive_index = random.choice(valid_indexs)
            negative_index = random_positive_index - len(value)
            return f"%{random_var}:~{negative_index},1%"
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
    # pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
    CommonProgramFiles = r"C:\Program Files\Common Files"
    CommonProgramFiles_x86 = r"C:\Program Files (x86)\Common Files"
    CommonProgramW6432 = r"C:\Program Files\Common Files"
    list_of_all = [
        public,
        weird,
        program_1,
        program_2,
        driver_stuff,
        # pathext,
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
        # "PATHEXT",
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
