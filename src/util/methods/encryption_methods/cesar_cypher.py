import string
import random


class CaesarCipher:
    @staticmethod
    def get(rotation_value: int, char: str, upper: bool = False) -> str:
        """
        Returns the rotated character.

        Args:
            rotation_value (int): The number of positions to rotate the character by.
            char (str): The character to rotate.
            upper (bool, optional): Whether the character is uppercase. Defaults to False.

        Returns:
            str: The rotated character.
        """
        alphabet = list(string.ascii_uppercase) if upper else list(string.ascii_lowercase)
        rotated_alphabet = alphabet[rotation_value:] + alphabet[:rotation_value]
        return rotated_alphabet[alphabet.index(char)]

    @staticmethod
    def lower(rotation_value: int) -> str:
        """
        Generates the Caesar cipher for a given rotation value. (lower letters only)

        Args:
            rotation_value (int): The number of positions to rotate the alphabet by.
            set_var (str, optional): The variable name to use for the cipher pairs. Defaults to None.

        Returns:
            str: The Caesar cipher for the given rotation value.
        """
        alphabet = list(string.ascii_lowercase)
        rotated_alphabet = alphabet[rotation_value:] + alphabet[:rotation_value]
        cipher_pairs = [f"""{CaesarCipher.get_random_scramble()}{CaesarCipherHelper.add_on(f'set "{rotated_alphabet[i]}={c}"')}\n""" for i, c in enumerate(alphabet)]

        return "".join(cipher_pairs)

    @staticmethod
    def upper(rotation_value: int) -> str:
        """
        Generates the Caesar cipher for a given rotation value. (CAPITAL LETTERS ONLY)

        Args:
            rotation_value (int): The number of positions to rotate the alphabet by.
            set_var (str, optional): The variable name to use for the cipher pairs. Defaults to None.

        Returns:
            str: The Caesar cipher for the given rotation value.
        """
        alphabet = list(string.ascii_uppercase)
        rotated_alphabet = alphabet[rotation_value:] + alphabet[:rotation_value]
        cipher_pairs = [f"""{CaesarCipher.get_random_scramble()}{CaesarCipherHelper.add_on(f'set "{rotated_alphabet[i]}1={c}"')}\n""" for i, c in enumerate(alphabet)]

        return "".join(cipher_pairs)

    @staticmethod
    def both(rotation_value: int) -> str:
        """
        Generates the Caesar cipher for a given rotation value. (BOTH UPPER AND LOWER)

        Args:
            rotation_value (int): The number of positions to rotate the alphabet by.
            set_var (str, optional): The variable name to use for the cipher pairs. Defaults to None.

        Returns:
            str: The Caesar cipher for the given rotation value.
        """
        return CaesarCipher.lower(rotation_value) + CaesarCipher.upper(rotation_value)

    @staticmethod
    def get_random_scramble() -> str:
        """
        Returns a random string to scramble the cipher pairs.

        Returns:
            str: The random string.
        """
        random_choice = random.choice([True, False])
        if random_choice:
            return "TO_SCRAMBLE_PLZ"
        return ""


class CaesarCipherHelper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_on(string: str) -> str:
        valid_commands = [
            f"for /l %%{CaesarCipherHelper.get_random_string_var(1)} in ({CaesarCipherHelper.get_random_number_var(1, 10)}, {CaesarCipherHelper.get_random_number_var(1, 10)}, {CaesarCipherHelper.get_random_number_var(21, 100)}) do ( {string} )",
            # f"for /f %%{CaesarCipherHelper.get_random_string_var(1)} in ('dir /b') do ( {string} )",
            # f"",
        ]

        return random.choice(valid_commands)

    @staticmethod
    def get_random_string_var(ammount: int) -> str:
        return "".join(random.choice(string.ascii_lowercase) for _ in range(ammount))

    @staticmethod
    def get_random_number_var(min1: int, max1: int) -> int:
        return random.randint(min1, max1)
