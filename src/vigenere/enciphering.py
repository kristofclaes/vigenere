# -*- coding: utf-8 -*-
from .constants import ALPHABET
from .utils import pair_up_characters

def encipher_character(character, key):
    """
    Enciphers the character using the key.
    :param str character: The character that should be enciphered. Should be string of length 1.
    :param str key: The key that should be used to encipher the character. Should be string of length 1.
    :return: The enciphered character. A string of length 1.
    :rtype: str
    """
    try:
        character_index = ALPHABET.index(character.upper())
        key_index = ALPHABET.index(key.upper())
    except ValueError:
        return character

    enciphered_character_index = (character_index + key_index) % 26

    return ALPHABET[enciphered_character_index]


def encipher(plaintext, key):
    """
    Enciphers the plaintext string using the key.
    :param str plaintext: The plaintext that needs to be enciphered.
    :param str key: The key to encipher the plaintext with.
    :return: The plaintext enciphered with the key.
    :rtype: str
    """
    character_pairs = pair_up_characters(plaintext, key)
    return "".join(encipher_character(character, key_character) for character, key_character in character_pairs)
