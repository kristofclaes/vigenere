# -*- coding: utf-8 -*-
from .constants import ALPHABET

def encipher_character(character, key):
    """
    Enciphers the character using the key.
    :param str character: The character that should be enciphered. Should be string of length 1.
    :param str key: The key that should be used to encipher the character. Should be string of length 1.
    :return: The enciphered character. A string of length 1.
    :rtype: str
    """
    try:
        character_index = ALPHABET.index(character)
        key_index = ALPHABET.index(key)
    except ValueError:
        return character

    enciphered_character_index = (character_index + key_index) % 26

    return ALPHABET[enciphered_character_index]
