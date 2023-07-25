import re
from util.obfuscation.obf_oneline import Obfuscate_Single


class IfBat:
    @staticmethod
    def if_bat(parsed_code: dict) -> str:
        raw_code = parsed_code["raw"]
        regex = r"if [^)]* (.*\n)+.*\)"
        if re.search(regex, raw_code):
            print(raw_code)
            return Obfuscate_Single(raw_code).out()
        else:
            return raw_code
