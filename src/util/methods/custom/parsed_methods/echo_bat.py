import random
import base64

from util.obfuscation.obf_oneline import Obfuscate_Single


class EchoBat:
    @staticmethod
    def echo_bat(parsed_code: dict) -> str:
        """
        This method takes a dictionary of parsed code and returns an obfuscated version of the code.
        If any of the bad_checks are true or any of the valid_checks are false, it returns an obfuscated version of the code.
        If the command length is invalid, it raises a ValueError.
        Otherwise, it randomly selects an obfuscation method and returns the obfuscated code.
        """
        bad_checks = [
            parsed_code["echo_to_file"],
            parsed_code["get_from_file"],
            parsed_code["variable"],
        ]
        valid_checks = [
            parsed_code["valid_command_length"],
        ]

        # check if any of the bad_checks are true or any of the valid_checks are false
        if any(bad_checks):
            return Obfuscate_Single(parsed_code["raw"]).out()

        if not all(valid_checks):
            raise ValueError(f"Invalid command length. Command == {parsed_code['raw']}")

        obfuscation_methods = [
            # self.label_method,
            # self.label_method2,
            EchoBat.powershell_method_enc,
            # self.mshta_method,
        ]

        random_method = random.choice(obfuscation_methods)
        return f"{EchoBat.random_scramble()}{random_method(parsed_code)}"

    @staticmethod
    def label_method(parsed_code: dict) -> str:
        """
        This method takes a dictionary of parsed code and returns a string.
        It is currently unused.
        """
        return 0

    @staticmethod
    def label_method2(parsed_code: dict) -> str:
        """
        This method takes a dictionary of parsed code and returns a string.
        It is currently unused.
        """
        return 0

    @staticmethod
    def powershell_method_enc(parsed_code: dict) -> str:
        """
        This method takes a dictionary of parsed code and returns an obfuscated version of the code using PowerShell.
        """
        code = parsed_code["raw"]
        code = code.replace("echo", "Write-Host")
        base64_utf_16_le_encoded_command = base64.b64encode(code.encode("utf-16-le")).decode("utf-8")
        powershell_options = [
            f"powershell.exe -ep bypass -noni -nop -e {base64_utf_16_le_encoded_command}",
        ]

        return Obfuscate_Single(random.choice(powershell_options)).out()

    @staticmethod
    def random_scramble() -> str:
        """
        This method returns a string that is either "TO_SCRAMBLE_PLZ" or an empty string, depending on a random chance.
        """
        random_chance = random.choice([True, False])
        if random_chance:
            return "TO_SCRAMBLE_PLZ"
        return ""
