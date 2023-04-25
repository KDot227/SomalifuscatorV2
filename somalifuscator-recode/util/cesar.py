import random

cesar_val = random.randint(1, 13)


def caesar_cipher_rotations(rotation):
    """Generates the Caesar cipher for a given rotation value."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)


def caesar_cipher_rotations_upper(rotation):
    """Generates the Caesar cipher for a given rotation value. (CAPITAL LETTERS ONLY)"""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    cipher_pairs = [
        f'set "{rotated_alphabet[i]}1={c}" && ' for i, c in enumerate(alphabet)
    ]

    return "".join(cipher_pairs)

def caesar_cipher_rotation(letter):
    """Returns the Caesar cipher rotation for a given letter and rotation value."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    letter_index = alphabet.index(letter.lower())
    rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
    rotated_letter = rotated_alphabet[letter_index]

    return rotated_letter

def caesar_cipher_rotation_UPPER(letter):
    """Returns the Caesar cipher rotation for a given letter and rotation value."""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter_index = alphabet.index(letter.upper())
    rotated_alphabet = alphabet[cesar_val:] + alphabet[:cesar_val]
    rotated_letter = rotated_alphabet[letter_index]

    return rotated_letter

together = caesar_cipher_rotations(cesar_val) + caesar_cipher_rotations_upper(cesar_val)
together = together[:-4]