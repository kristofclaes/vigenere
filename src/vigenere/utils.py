# -*- coding: utf-8 -*-
from itertools import cycle


def pair_up_characters(text, key):
    """
    Takes a text for enciphering or deciphering and a key and pairs up each character from the text with the correct
    character from the key.
    :param str text: The text that needs to be enciphered or deciphered.
    :param str key: The key to use for enciphering or deciphering.
    :return: A list of tuples where the first element of the tuple is character from the text and the second element of
             the tuple is the corresponding character of the key.
    :rtype: list
    """
    return list(zip(text, cycle(key)))
