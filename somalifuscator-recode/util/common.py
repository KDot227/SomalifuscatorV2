import random

from util.settings import chinese_characters

from util.cesar import caesar_cipher_rotations, caesar_cipher_rotations_upper, cesar_val

@staticmethod
def make_random_string(length_nums=(5, 7)):
    length = random.randint(*length_nums)
    stringed = "".join(
        random.choice(
            # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
            # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
            # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$(),.?@[]_"
        )
        for _ in range(length)
    )
    # yes this has happened to me before and echo check terms it
    while "echo" in stringed.lower():
        stringed = "".join(
            random.choice(
                # Batch has a specific issue with characters that aren't in the normal ASCII table cause if u got them in a variable it will make the variable explode. I fixed this before by changing the chcp to 65001 but sometimes that wouldn't fix things
                # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐"
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            for _ in range(length)
        )
    return stringed

@staticmethod
def random_capitalization(string):
    return "".join(random.choice([char.upper(), char.lower()]) for char in string)

@staticmethod
def make_random_label_no_working():
    # 911 lol
    length = random.choice([9, 11])
    return "".join(random.choice(chinese_characters) for _ in range(length))

@staticmethod
def fake_ceaser_cipher():
    together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(
        cesar_val
    )
    together = together[:-4]
    return together