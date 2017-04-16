# -*- coding: utf-8 -*-
from .constants import ALPHABET
from .utils import pair_up_characters


def decipher_character(enciphered_character, key):
    """
    Deciphers the enciphered character using the key.
    :param str enciphered_character: The enciphered character that should be deciphered. Should be string of length 1.
    :param str key: The key that should be used to decipher the enciphered character. Should be string of length 1.
    :return: The deciphered character. A string of length 1.
    :rtype: str
    """
    try:
        enciphered_character_index = ALPHABET.index(enciphered_character.upper())
        key_index = ALPHABET.index(key.upper())
    except ValueError:
        return enciphered_character

    deciphered_character_index = (enciphered_character_index - key_index) % 26

    return ALPHABET[deciphered_character_index]


def decipher(enciphered_text, key):
    """
    Deciphers the enciphered string using the key.
    :param str enciphered_text: The enciphered text that needs to be deciphered.
    :param str key: The key to decipher the enciphered text with.
    :return: The enciphered text deciphered with the key.
    :rtype: str
    """
    character_pairs = pair_up_characters(enciphered_text, key)
    return "".join(decipher_character(character, key_character) for character, key_character in character_pairs)
