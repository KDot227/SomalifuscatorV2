from util.common import *
from levels.ultimate.modules.gen_obf import obf_oneline


@staticmethod
def fake_ceaser_cipher():
    together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(
        cesar_val
    )
    together = together[:-4]
    return together


def fake_ceaser_cipher_obfuscated():
    """simple function to obfuscate the cipher"""
    cipher = fake_ceaser_cipher()
    obfuscated = obf_oneline(cipher)
    return obfuscated


def fake_KDOT():
    """makes fake KDOT var"""
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_order = "".join(random.sample(characters, len(characters)))
    return random_order
