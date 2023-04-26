import random

from levels.ultimate.modules.fake_stuff import *
from levels.ultimate.modules.gen_obf import obf_oneline
from util.settings import *


def random_dead_code(entire_array):
    """Dead code that just won't be executed so it can be whatever. If u wanna add more its all u"""
    dead_code = [
        "echo Best Batch Obfuscated By KDot and Godfather\n",
        "if 0 == 0 (echo Best Batch Obfuscated By KDot and Godfather)\n",
        f"set KDOT={fake_KDOT()}\n",
        f"{fake_ceaser_cipher()}\n",
        f"{fake_ceaser_cipher_obfuscated()}\n",
        f"set somalifuscator=op_asf\n",
    ]
    if eicar:
        dead_code.append(
            "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n"
        )
    for array in entire_array:
        if random.randint(0, 3) == 3:
            option = random.choice(dead_code)
            if (
                option
                # it's funny cause it's still fud even unobfuscated
                == "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n"
            ):
                scated = option
            else:
                scated = obf_oneline(option)
            new_string = "".join(scated)
            new_string = [new_string]
            entire_array.insert(entire_array.index(array), new_string)

    return entire_array


def deadcodes(good_label, bad_label, rep_num):
    """not really deadcode but it just makes it hard for kids to understand"""
    # gotta love %random%
    # hehehehe
    RANNUM = random.randint(32769, 99999)
    # This is absolute hell for anyone trying to deobfuscate this
    label123 = bad_label
    if rep_num < 5:
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
            coded = f"{random_capitalization(random.choice(code_examples))} ^\n {random.choice(examples)} ^\n exit /b 0\n{random.choice(examples)}"
            for _ in range(3):
                examples.append(coded)
        else:
            coded = f"{random_capitalization(random.choice(code_examples))} ^\n exit /b 0\n {random.choice(examples)}"
            for _ in range(3):
                examples.append(coded)

    randomed = random.choice(examples)
    obfuscated = obf_oneline(randomed)
    rep_num += 1
    return obfuscated
