import random

from util.common import random_capitalization
from levels.ultimate.modules.gen_obf import obf_oneline


def random_inserts(main_list):
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
            random_int = random.randint(1, 10)
            if random_int == 10:
                list_choice = random_capitalization(random.choice(listes))
                main_list.insert(i, [list_choice])

    return main_list


def bad_labels_and_dead_code(main_list, dict_thing):
    """inserts labels that are valid but won't do anything since they have a zero width space infront. This mainly messes up looking at it from a text editor. You can still goto it if you use the weird translated bytes."""
    main_dict = dict_thing
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
                random_chance = random.randint(1, 3)
                if random_chance == 5:
                    random_label = random.choice(new_list)
                    random_place = random.randint(0, len(array))
                    array.insert(random_place, random_label)
            else:
                doskey = f"doskey {random.choice(doskey_options)}={random.choice(doskey_options)}"
                array.append(obf_oneline(doskey))
    return main_list


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
                random_capitalization(random.choice(code_examples)),
            )
    return main_list
