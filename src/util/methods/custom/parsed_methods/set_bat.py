import random

from util.methods.custom.parsed_methods.command_wrapers_universal.command_wrappers import CommandWrappers

from util.methods.common.common import escape_batch, make_random_string, random_scramble

from util.obfuscation.obf_oneline import Obfuscate_Single


class SetBat:
    @staticmethod
    def set_bat(parsed_code: dict) -> str:
        command = parsed_code["raw"]
        command = command.strip()

        # if "/a" or "/p" in args.lower():
        #    return Obfuscate_Single(CommandWrappers.outside_command(args)).out()

        methods = [
            SetBat.for_loop,
            SetBat.if_statement,
            # SetBat.ads,
        ]

        return random.choice(methods)(command)

    @staticmethod
    def for_loop(args: str) -> str:
        return random_scramble() + Obfuscate_Single(CommandWrappers.for_loop(command=args), False).out() + "\n"

    @staticmethod
    def if_statement(args: str) -> str:
        return random_scramble() + Obfuscate_Single(CommandWrappers.outside_command(command=args), False).out() + "\n"

    @staticmethod
    def ads(args: str) -> str:
        command = args.split()[0]
        good_args = escape_batch(command)

        random_num1 = random.randint(100, 10000)
        random_char = make_random_string((1, 1), False)

        struct = f'echo {good_args} > %~f0:{random_num1}\nfor /f "usebackq delims=φ" %%{random_char} in (%~f0:{random_num1}) do %%{random_char}\n'
        return Obfuscate_Single(random_scramble() + struct).out()
