# -*- coding: utf-8 -*-
from vigenere.utils import pair_up_characters


def test_pair_up_with_text_and_key_of_same_length():
    """Tests that the characters of a text and a key are paired up correctly when they are of the same length."""
    pairs = pair_up_characters('ABC', 'DEF')

    assert pairs == [('A', 'D'), ('B', 'E'), ('C', 'F')]


def test_pair_up_with_text_longer_than_key():
    """Tests that the characters of a text and a key are paired up correctly when the text is longer than the key."""
    pairs = pair_up_characters('ABC', 'DE')

    assert pairs == [('A', 'D'), ('B', 'E'), ('C', 'D')]


def test_pair_up_with_key_longer_than_text():
    """Tests that the characters of a text and a key are paired up correctly when the key is longer than the text."""
    pairs = pair_up_characters('AB', 'DEF')

    assert pairs == [('A', 'D'), ('B', 'E')]
