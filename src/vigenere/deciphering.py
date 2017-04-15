# -*- coding: utf-8 -*-
from .constants import ALPHABET


def decipher_character(enciphered_character, key):
    """
    Deciphers the enciphered character using the key.
    :param str enciphered_character: The enciphered character that should be deciphered. Should be string of length 1.
    :param str key: The key that should be used to decipher the enciphered character. Should be string of length 1.
    :return: The deciphered character. A string of length 1.
    :rtype: str
    """
    try:
        enciphered_character_index = ALPHABET.index(enciphered_character)
        key_index = ALPHABET.index(key)
    except ValueError:
        return enciphered_character

    deciphered_character_index = (enciphered_character_index - key_index) % 26

    return ALPHABET[deciphered_character_index]
