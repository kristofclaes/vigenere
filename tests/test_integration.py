# -*- coding: utf-8 -*-
import pytest
from vigenere.enciphering import encipher_character
from vigenere.deciphering import decipher_character

@pytest.mark.parametrize('character', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
@pytest.mark.parametrize('key', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
def test_encipher_decipher_character(character, key):
    """Tests that enciphered characters are deciphered to the same character when the same key is used."""
    enciphered_character = encipher_character(character, key)
    assert decipher_character(enciphered_character, key) == character
