# -*- coding: utf-8 -*-
import pytest
from vigenere.enciphering import encipher_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'),
    ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'),
    ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')
])
def test_encipher_character_a(key, enciphered_character):
    assert encipher_character('A', key) == enciphered_character
    assert encipher_character('a', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'),
    ('J', 'K'), ('K', 'L'), ('L', 'M'), ('M', 'N'), ('N', 'O'), ('O', 'P'), ('P', 'Q'), ('Q', 'R'), ('R', 'S'),
    ('S', 'T'), ('T', 'U'), ('U', 'V'), ('V', 'W'), ('W', 'X'), ('X', 'Y'), ('Y', 'Z'), ('Z', 'A')
])
def test_encipher_character_b(key, enciphered_character):
    assert encipher_character('B', key) == enciphered_character
    assert encipher_character('b', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'G'), ('F', 'H'), ('G', 'I'), ('H', 'J'), ('I', 'K'),
    ('J', 'L'), ('K', 'M'), ('L', 'N'), ('M', 'O'), ('N', 'P'), ('O', 'Q'), ('P', 'R'), ('Q', 'S'), ('R', 'T'),
    ('S', 'U'), ('T', 'V'), ('U', 'W'), ('V', 'X'), ('W', 'Y'), ('X', 'Z'), ('Y', 'A'), ('Z', 'B')
])
def test_encipher_character_c(key, enciphered_character):
    assert encipher_character('C', key) == enciphered_character
    assert encipher_character('c', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'D'), ('B', 'E'), ('C', 'F'), ('D', 'G'), ('E', 'H'), ('F', 'I'), ('G', 'J'), ('H', 'K'), ('I', 'L'),
    ('J', 'M'), ('K', 'N'), ('L', 'O'), ('M', 'P'), ('N', 'Q'), ('O', 'R'), ('P', 'S'), ('Q', 'T'), ('R', 'U'),
    ('S', 'V'), ('T', 'W'), ('U', 'X'), ('V', 'Y'), ('W', 'Z'), ('X', 'A'), ('Y', 'B'), ('Z', 'C')
])
def test_encipher_character_d(key, enciphered_character):
    assert encipher_character('D', key) == enciphered_character
    assert encipher_character('d', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K'), ('H', 'L'), ('I', 'M'),
    ('J', 'N'), ('K', 'O'), ('L', 'P'), ('M', 'Q'), ('N', 'R'), ('O', 'S'), ('P', 'T'), ('Q', 'U'), ('R', 'V'),
    ('S', 'W'), ('T', 'X'), ('U', 'Y'), ('V', 'Z'), ('W', 'A'), ('X', 'B'), ('Y', 'C'), ('Z', 'D')
])
def test_encipher_character_e(key, enciphered_character):
    assert encipher_character('E', key) == enciphered_character
    assert encipher_character('e', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'F'), ('B', 'G'), ('C', 'H'), ('D', 'I'), ('E', 'J'), ('F', 'K'), ('G', 'L'), ('H', 'M'), ('I', 'N'),
    ('J', 'O'), ('K', 'P'), ('L', 'Q'), ('M', 'R'), ('N', 'S'), ('O', 'T'), ('P', 'U'), ('Q', 'V'), ('R', 'W'),
    ('S', 'X'), ('T', 'Y'), ('U', 'Z'), ('V', 'A'), ('W', 'B'), ('X', 'C'), ('Y', 'D'), ('Z', 'E')
])
def test_encipher_character_f(key, enciphered_character):
    assert encipher_character('F', key) == enciphered_character
    assert encipher_character('f', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'G'), ('B', 'H'), ('C', 'I'), ('D', 'J'), ('E', 'K'), ('F', 'L'), ('G', 'M'), ('H', 'N'), ('I', 'O'),
    ('J', 'P'), ('K', 'Q'), ('L', 'R'), ('M', 'S'), ('N', 'T'), ('O', 'U'), ('P', 'V'), ('Q', 'W'), ('R', 'X'),
    ('S', 'Y'), ('T', 'Z'), ('U', 'A'), ('V', 'B'), ('W', 'C'), ('X', 'D'), ('Y', 'E'), ('Z', 'F')
])
def test_encipher_character_g(key, enciphered_character):
    assert encipher_character('G', key) == enciphered_character
    assert encipher_character('g', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'H'), ('B', 'I'), ('C', 'J'), ('D', 'K'), ('E', 'L'), ('F', 'M'), ('G', 'N'), ('H', 'O'), ('I', 'P'),
    ('J', 'Q'), ('K', 'R'), ('L', 'S'), ('M', 'T'), ('N', 'U'), ('O', 'V'), ('P', 'W'), ('Q', 'X'), ('R', 'Y'),
    ('S', 'Z'), ('T', 'A'), ('U', 'B'), ('V', 'C'), ('W', 'D'), ('X', 'E'), ('Y', 'F'), ('Z', 'G')
])
def test_encipher_character_h(key, enciphered_character):
    assert encipher_character('h', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'I'), ('B', 'J'), ('C', 'K'), ('D', 'L'), ('E', 'M'), ('F', 'N'), ('G', 'O'), ('H', 'P'), ('I', 'Q'),
    ('J', 'R'), ('K', 'S'), ('L', 'T'), ('M', 'U'), ('N', 'V'), ('O', 'W'), ('P', 'X'), ('Q', 'Y'), ('R', 'Z'),
    ('S', 'A'), ('T', 'B'), ('U', 'C'), ('V', 'D'), ('W', 'E'), ('X', 'F'), ('Y', 'G'), ('Z', 'H')
])
def test_encipher_character_i(key, enciphered_character):
    assert encipher_character('I', key) == enciphered_character
    assert encipher_character('i', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'J'), ('B', 'K'), ('C', 'L'), ('D', 'M'), ('E', 'N'), ('F', 'O'), ('G', 'P'), ('H', 'Q'), ('I', 'R'),
    ('J', 'S'), ('K', 'T'), ('L', 'U'), ('M', 'V'), ('N', 'W'), ('O', 'X'), ('P', 'Y'), ('Q', 'Z'), ('R', 'A'),
    ('S', 'B'), ('T', 'C'), ('U', 'D'), ('V', 'E'), ('W', 'F'), ('X', 'G'), ('Y', 'H'), ('Z', 'I')
])
def test_encipher_character_j(key, enciphered_character):
    assert encipher_character('J', key) == enciphered_character
    assert encipher_character('j', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'K'), ('B', 'L'), ('C', 'M'), ('D', 'N'), ('E', 'O'), ('F', 'P'), ('G', 'Q'), ('H', 'R'), ('I', 'S'),
    ('J', 'T'), ('K', 'U'), ('L', 'V'), ('M', 'W'), ('N', 'X'), ('O', 'Y'), ('P', 'Z'), ('Q', 'A'), ('R', 'B'),
    ('S', 'C'), ('T', 'D'), ('U', 'E'), ('V', 'F'), ('W', 'G'), ('X', 'H'), ('Y', 'I'), ('Z', 'J')
])
def test_encipher_character_k(key, enciphered_character):
    assert encipher_character('K', key) == enciphered_character
    assert encipher_character('k', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'L'), ('B', 'M'), ('C', 'N'), ('D', 'O'), ('E', 'P'), ('F', 'Q'), ('G', 'R'), ('H', 'S'), ('I', 'T'),
    ('J', 'U'), ('K', 'V'), ('L', 'W'), ('M', 'X'), ('N', 'Y'), ('O', 'Z'), ('P', 'A'), ('Q', 'B'), ('R', 'C'),
    ('S', 'D'), ('T', 'E'), ('U', 'F'), ('V', 'G'), ('W', 'H'), ('X', 'I'), ('Y', 'J'), ('Z', 'K')
])
def test_encipher_character_l(key, enciphered_character):
    assert encipher_character('L', key) == enciphered_character
    assert encipher_character('l', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'M'), ('B', 'N'), ('C', 'O'), ('D', 'P'), ('E', 'Q'), ('F', 'R'), ('G', 'S'), ('H', 'T'), ('I', 'U'),
    ('J', 'V'), ('K', 'W'), ('L', 'X'), ('M', 'Y'), ('N', 'Z'), ('O', 'A'), ('P', 'B'), ('Q', 'C'), ('R', 'D'),
    ('S', 'E'), ('T', 'F'), ('U', 'G'), ('V', 'H'), ('W', 'I'), ('X', 'J'), ('Y', 'K'), ('Z', 'L')
])
def test_encipher_character_m(key, enciphered_character):
    assert encipher_character('M', key) == enciphered_character
    assert encipher_character('m', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'N'), ('B', 'O'), ('C', 'P'), ('D', 'Q'), ('E', 'R'), ('F', 'S'), ('G', 'T'), ('H', 'U'), ('I', 'V'),
    ('J', 'W'), ('K', 'X'), ('L', 'Y'), ('M', 'Z'), ('N', 'A'), ('O', 'B'), ('P', 'C'), ('Q', 'D'), ('R', 'E'),
    ('S', 'F'), ('T', 'G'), ('U', 'H'), ('V', 'I'), ('W', 'J'), ('X', 'K'), ('Y', 'L'), ('Z', 'M')
])
def test_encipher_character_n(key, enciphered_character):
    assert encipher_character('N', key) == enciphered_character
    assert encipher_character('n', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'O'), ('B', 'P'), ('C', 'Q'), ('D', 'R'), ('E', 'S'), ('F', 'T'), ('G', 'U'), ('H', 'V'), ('I', 'W'),
    ('J', 'X'), ('K', 'Y'), ('L', 'Z'), ('M', 'A'), ('N', 'B'), ('O', 'C'), ('P', 'D'), ('Q', 'E'), ('R', 'F'),
    ('S', 'G'), ('T', 'H'), ('U', 'I'), ('V', 'J'), ('W', 'K'), ('X', 'L'), ('Y', 'M'), ('Z', 'N')
])
def test_encipher_character_o(key, enciphered_character):
    assert encipher_character('O', key) == enciphered_character
    assert encipher_character('o', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'P'), ('B', 'Q'), ('C', 'R'), ('D', 'S'), ('E', 'T'), ('F', 'U'), ('G', 'V'), ('H', 'W'), ('I', 'X'),
    ('J', 'Y'), ('K', 'Z'), ('L', 'A'), ('M', 'B'), ('N', 'C'), ('O', 'D'), ('P', 'E'), ('Q', 'F'), ('R', 'G'),
    ('S', 'H'), ('T', 'I'), ('U', 'J'), ('V', 'K'), ('W', 'L'), ('X', 'M'), ('Y', 'N'), ('Z', 'O')
])
def test_encipher_character_p(key, enciphered_character):
    assert encipher_character('P', key) == enciphered_character
    assert encipher_character('p', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'Q'), ('B', 'R'), ('C', 'S'), ('D', 'T'), ('E', 'U'), ('F', 'V'), ('G', 'W'), ('H', 'X'), ('I', 'Y'),
    ('J', 'Z'), ('K', 'A'), ('L', 'B'), ('M', 'C'), ('N', 'D'), ('O', 'E'), ('P', 'F'), ('Q', 'G'), ('R', 'H'),
    ('S', 'I'), ('T', 'J'), ('U', 'K'), ('V', 'L'), ('W', 'M'), ('X', 'N'), ('Y', 'O'), ('Z', 'P')
])
def test_encipher_character_q(key, enciphered_character):
    assert encipher_character('Q', key) == enciphered_character
    assert encipher_character('q', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'R'), ('B', 'S'), ('C', 'T'), ('D', 'U'), ('E', 'V'), ('F', 'W'), ('G', 'X'), ('H', 'Y'), ('I', 'Z'),
    ('J', 'A'), ('K', 'B'), ('L', 'C'), ('M', 'D'), ('N', 'E'), ('O', 'F'), ('P', 'G'), ('Q', 'H'), ('R', 'I'),
    ('S', 'J'), ('T', 'K'), ('U', 'L'), ('V', 'M'), ('W', 'N'), ('X', 'O'), ('Y', 'P'), ('Z', 'Q')
])
def test_encipher_character_r(key, enciphered_character):
    assert encipher_character('R', key) == enciphered_character
    assert encipher_character('r', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'S'), ('B', 'T'), ('C', 'U'), ('D', 'V'), ('E', 'W'), ('F', 'X'), ('G', 'Y'), ('H', 'Z'), ('I', 'A'),
    ('J', 'B'), ('K', 'C'), ('L', 'D'), ('M', 'E'), ('N', 'F'), ('O', 'G'), ('P', 'H'), ('Q', 'I'), ('R', 'J'),
    ('S', 'K'), ('T', 'L'), ('U', 'M'), ('V', 'N'), ('W', 'O'), ('X', 'P'), ('Y', 'Q'), ('Z', 'R')
])
def test_encipher_character_s(key, enciphered_character):
    assert encipher_character('S', key) == enciphered_character
    assert encipher_character('s', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'T'), ('B', 'U'), ('C', 'V'), ('D', 'W'), ('E', 'X'), ('F', 'Y'), ('G', 'Z'), ('H', 'A'), ('I', 'B'),
    ('J', 'C'), ('K', 'D'), ('L', 'E'), ('M', 'F'), ('N', 'G'), ('O', 'H'), ('P', 'I'), ('Q', 'J'), ('R', 'K'),
    ('S', 'L'), ('T', 'M'), ('U', 'N'), ('V', 'O'), ('W', 'P'), ('X', 'Q'), ('Y', 'R'), ('Z', 'S')
])
def test_encipher_character_t(key, enciphered_character):
    assert encipher_character('T', key) == enciphered_character
    assert encipher_character('t', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'U'), ('B', 'V'), ('C', 'W'), ('D', 'X'), ('E', 'Y'), ('F', 'Z'), ('G', 'A'), ('H', 'B'), ('I', 'C'),
    ('J', 'D'), ('K', 'E'), ('L', 'F'), ('M', 'G'), ('N', 'H'), ('O', 'I'), ('P', 'J'), ('Q', 'K'), ('R', 'L'),
    ('S', 'M'), ('T', 'N'), ('U', 'O'), ('V', 'P'), ('W', 'Q'), ('X', 'R'), ('Y', 'S'), ('Z', 'T')
])
def test_encipher_character_u(key, enciphered_character):
    assert encipher_character('U', key) == enciphered_character
    assert encipher_character('u', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'V'), ('B', 'W'), ('C', 'X'), ('D', 'Y'), ('E', 'Z'), ('F', 'A'), ('G', 'B'), ('H', 'C'), ('I', 'D'),
    ('J', 'E'), ('K', 'F'), ('L', 'G'), ('M', 'H'), ('N', 'I'), ('O', 'J'), ('P', 'K'), ('Q', 'L'), ('R', 'M'),
    ('S', 'N'), ('T', 'O'), ('U', 'P'), ('V', 'Q'), ('W', 'R'), ('X', 'S'), ('Y', 'T'), ('Z', 'U')
])
def test_encipher_character_v(key, enciphered_character):
    assert encipher_character('V', key) == enciphered_character
    assert encipher_character('v', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'W'), ('B', 'X'), ('C', 'Y'), ('D', 'Z'), ('E', 'A'), ('F', 'B'), ('G', 'C'), ('H', 'D'), ('I', 'E'),
    ('J', 'F'), ('K', 'G'), ('L', 'H'), ('M', 'I'), ('N', 'J'), ('O', 'K'), ('P', 'L'), ('Q', 'M'), ('R', 'N'),
    ('S', 'O'), ('T', 'P'), ('U', 'Q'), ('V', 'R'), ('W', 'S'), ('X', 'T'), ('Y', 'U'), ('Z', 'V')
])
def test_encipher_character_w(key, enciphered_character):
    assert encipher_character('W', key) == enciphered_character
    assert encipher_character('w', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'X'), ('B', 'Y'), ('C', 'Z'), ('D', 'A'), ('E', 'B'), ('F', 'C'), ('G', 'D'), ('H', 'E'), ('I', 'F'),
    ('J', 'G'), ('K', 'H'), ('L', 'I'), ('M', 'J'), ('N', 'K'), ('O', 'L'), ('P', 'M'), ('Q', 'N'), ('R', 'O'),
    ('S', 'P'), ('T', 'Q'), ('U', 'R'), ('V', 'S'), ('W', 'T'), ('X', 'U'), ('Y', 'V'), ('Z', 'W')
])
def test_encipher_character_x(key, enciphered_character):
    assert encipher_character('X', key) == enciphered_character
    assert encipher_character('x', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'Y'), ('B', 'Z'), ('C', 'A'), ('D', 'B'), ('E', 'C'), ('F', 'D'), ('G', 'E'), ('H', 'F'), ('I', 'G'),
    ('J', 'H'), ('K', 'I'), ('L', 'J'), ('M', 'K'), ('N', 'L'), ('O', 'M'), ('P', 'N'), ('Q', 'O'), ('R', 'P'),
    ('S', 'Q'), ('T', 'R'), ('U', 'S'), ('V', 'T'), ('W', 'U'), ('X', 'V'), ('Y', 'W'), ('Z', 'X')
])
def test_encipher_character_y(key, enciphered_character):
    assert encipher_character('Y', key) == enciphered_character
    assert encipher_character('y', key) == enciphered_character


@pytest.mark.parametrize('key,enciphered_character', [
    ('A', 'Z'), ('B', 'A'), ('C', 'B'), ('D', 'C'), ('E', 'D'), ('F', 'E'), ('G', 'F'), ('H', 'G'), ('I', 'H'),
    ('J', 'I'), ('K', 'J'), ('L', 'K'), ('M', 'L'), ('N', 'M'), ('O', 'N'), ('P', 'O'), ('Q', 'P'), ('R', 'Q'),
    ('S', 'R'), ('T', 'S'), ('U', 'T'), ('V', 'U'), ('W', 'V'), ('X', 'W'), ('Y', 'X'), ('Z', 'Y')
])
def test_encipher_character_z(key, enciphered_character):
    assert encipher_character('Z', key) == enciphered_character
    assert encipher_character('z', key) == enciphered_character


@pytest.mark.parametrize('character', ['1', '.', '"', '?', '!'])
@pytest.mark.parametrize('key', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
def test_enciphering_unknown_character_returns_character(character, key):
    assert encipher_character(character, key) == character


@pytest.mark.parametrize('character', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
@pytest.mark.parametrize('key', ['1', '.', '"', '?', '!'])
def test_enciphering_with_unknown_key_returns_character(character, key):
    assert encipher_character(character, key) == character
