from util.settings import *
from util.common import *
from levels.ultimate.modules.anti_things import *
from levels.ultimate.modules.dead_stuff import *
from levels.ultimate.modules.math_stuff import *
from levels.ultimate.modules.misc import *
import random


def scrambler(codeed, level):
    """This absolutely beautiful function takes the code, puts it into a nested array of goto values that all point to each other then obfuscates tf outta it."""
    original_lines = codeed
    rep_num = 10

    for index, line in enumerate(original_lines):
        # not sure if echo really makes a difference but batch does some weird things sometimes
        echo_check123 = False
        try:
            if r"%errorlevel%" in original_lines[index - 1].lower():
                echo_check123 = True
        except IndexError:
            pass
        # This should never have an index error since it's the current itteration in the list
        # if it does get an error then u got other issues. Also at that point dont make an issue just pray to god (or whoever or dont pray idc) and restart ur pc
        if r"%errorlevel%" in line.lower():
            echo_check123 = True
        try:
            if r"%errorlevel%" in original_lines[index + 1].lower():
                echo_check123 = True
        except IndexError:
            pass
        if not echo_check123:
            random_number = random.randint(1, 4)
            if random_number == 1:
                # add a label that doesn't do anything
                label = f":{make_random_label_no_working()}\n"
                original_lines.insert(index, label)

    original_lines = [item for item in original_lines if item not in [";", "\n", ";\n"]]

    dict_thing = {}

    main_list = []

    for index, item in enumerate(original_lines):
        echo_check123 = False
        # check if %errorlevel% is in the previous line and the current line and next line and if it is then set it to True
        try:
            if r"%errorlevel%" in original_lines[index - 1].lower():
                echo_check123 = True
        except IndexError:
            pass
        # This should never have an index error since it's the current itteration in the list
        # if it does get an error then u got other issues. Also at that point dont make an issue just pray to god (or whoever or dont pray idc) and restart ur pc
        if r"%errorlevel%" in item.lower():
            echo_check123 = True
        try:
            if r"%errorlevel%" in original_lines[index + 1].lower():
                echo_check123 = True
        except IndexError:
            pass
        t = generate_math_problem(answer=random.randint(100000, 10000000))
        dict_thing[item] = [
            t[0],
            t[1],
            index,
            echo_check123,
        ]

    # I use ; infront of everything cause it gets rid of syntax highlight on vscode and notepad++ lmao

    # NOTE everything in this for loop is the most confusing and worse coding I have ever done in my life. I am sorry for whoever is trying to read, imrpove or just understand what is going on especially if you have no prior knowledge of batch
    for index, (key, value) in enumerate(dict_thing.items()):
        if index == 0:
            remem = [
                f";{obf_oneline('set')} /a {obf_oneline('ans')}={obf_oneline(value[0])}\n;{random_semi_and_comma(obf_oneline('goto'))} :%ans%\n"
            ]
        part_1 = f";:{value[1]}\n"
        part_2 = f";{key}\n"
        if hell and unicode:
            badded = (
                r" ็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็"
                * random.randint(10, 20)
            )
            try:
                random_t_f = random.choice([True, False])
                if random_t_f:
                    dead = list(dict_thing.values())[index + 1][1]
                    random_working_value = random.choice(list(dict_thing.values()))
                    while random_working_value[1] == dead:
                        random_working_value = random.choice(list(dict_thing.values()))
                    run = deadcodes(
                        good_label=str(dead),
                        bad_label=random_working_value[1],
                        rep_num=rep_num,
                    )
                    rep_num += 1
                    part_3 = f"{run}\n::{badded}\n"
                else:
                    maybe_echo_check = random.randint(1, 3)
                    if maybe_echo_check == 1 and not value[3]:
                        part_3 = f";{obf_oneline('set')} /a {obf_oneline('ans')}={obf_oneline(list(dict_thing.values())[index + 1][0])}\n::{badded}\n::{badded}\n::{badded}\n{obf_oneline(random.choice(tests(level)))}\n;{random_semi_and_comma(obf_oneline('goto'))} :%ans%\n"
                    else:
                        part_3 = f";{obf_oneline('set')} /a {obf_oneline('ans')}={obf_oneline(list(dict_thing.values())[index + 1][0])}\n::{badded}\n::{badded}\n::{badded}\n;{random_semi_and_comma(obf_oneline('goto'))} :%ans%\n"
            except Exception:
                part_3 = f";{random_semi_and_comma(obf_oneline('goto'))} :EOF\n::{badded}\n::{badded}\n::{badded}\n"
        else:
            try:
                random_t_f = random.choice([True, False])
                if random_t_f:
                    dead = list(dict_thing.values())[index + 1][1]
                    random_working_value = random.choice(list(dict_thing.values()))
                    while random_working_value[1] == dead:
                        random_working_value = random.choice(list(dict_thing.values()))
                    run = deadcodes(
                        good_label=str(dead),
                        bad_label=random_working_value[1],
                        rep_num=rep_num,
                    )
                    rep_num += 1
                    part_3 = f"{run}\n"
                else:
                    maybe_echo_check = random.randint(1, 3)
                    if maybe_echo_check == 1 and not value[3]:
                        print(value[3])
                        part_3 = f";{obf_oneline('set')} /a {obf_oneline('ans')}={obf_oneline(list(dict_thing.values())[index + 1][0])}\n{obf_oneline(random.choice(tests(level)))}\n;{random_semi_and_comma(obf_oneline('goto'))} :%ans%\n"
                    else:
                        part_3 = f";{obf_oneline('set')} /a {obf_oneline('ans')}={obf_oneline(list(dict_thing.values())[index + 1][0])}\n;{random_semi_and_comma(obf_oneline('goto'))} :%ans%\n"
            except Exception:
                part_3 = f";{random_semi_and_comma(obf_oneline('goto'))} :EOF\n"

        # with open("out2.bat", "w", encoding="utf8", errors="ignore") as f:
        #    f.write(part_1 + part_2 + part_3)
        # input()

        main_list.append([part_1, part_2, part_3])

    random.shuffle(main_list)

    main_list = random_inserts(main_list)

    main_list = random_dead_code(main_list)

    main_list = bad_labels_and_dead_code(main_list, dict_thing)

    if random_spacing:
        main_list = more_dead_comments(main_list)

    if pogdog_fun:
        main_list = pogdog(main_list)

    # pointer that points to first line of the actual code.
    main_list.insert(0, remem)

    return main_list
