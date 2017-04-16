# -*- coding: utf-8 -*-
import pytest
from vigenere.deciphering import decipher_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'A'), ('B', 'Z'), ('C', 'Y'), ('D', 'X'), ('E', 'W'), ('F', 'V'), ('G', 'U'), ('H', 'T'), ('I', 'S'),
    ('J', 'R'), ('K', 'Q'), ('L', 'P'), ('M', 'O'), ('N', 'N'), ('O', 'M'), ('P', 'L'), ('Q', 'K'), ('R', 'J'),
    ('S', 'I'), ('T', 'H'), ('U', 'G'), ('V', 'F'), ('W', 'E'), ('X', 'D'), ('Y', 'C'), ('Z', 'B')
])
def test_decipher_character_a(key, deciphered_character):
    assert decipher_character('A', key) == deciphered_character
    assert decipher_character('a', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'B'), ('B', 'A'), ('C', 'Z'), ('D', 'Y'), ('E', 'X'), ('F', 'W'), ('G', 'V'), ('H', 'U'), ('I', 'T'),
    ('J', 'S'), ('K', 'R'), ('L', 'Q'), ('M', 'P'), ('N', 'O'), ('O', 'N'), ('P', 'M'), ('Q', 'L'), ('R', 'K'),
    ('S', 'J'), ('T', 'I'), ('U', 'H'), ('V', 'G'), ('W', 'F'), ('X', 'E'), ('Y', 'D'), ('Z', 'C')
])
def test_decipher_character_b(key, deciphered_character):
    assert decipher_character('B', key) == deciphered_character
    assert decipher_character('b', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'C'), ('B', 'B'), ('C', 'A'), ('D', 'Z'), ('E', 'Y'), ('F', 'X'), ('G', 'W'), ('H', 'V'), ('I', 'U'),
    ('J', 'T'), ('K', 'S'), ('L', 'R'), ('M', 'Q'), ('N', 'P'), ('O', 'O'), ('P', 'N'), ('Q', 'M'), ('R', 'L'),
    ('S', 'K'), ('T', 'J'), ('U', 'I'), ('V', 'H'), ('W', 'G'), ('X', 'F'), ('Y', 'E'), ('Z', 'D')
])
def test_decipher_character_c(key, deciphered_character):
    assert decipher_character('C', key) == deciphered_character
    assert decipher_character('c', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'D'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'Z'), ('F', 'Y'), ('G', 'X'), ('H', 'W'), ('I', 'V'),
    ('J', 'U'), ('K', 'T'), ('L', 'S'), ('M', 'R'), ('N', 'Q'), ('O', 'P'), ('P', 'O'), ('Q', 'N'), ('R', 'M'),
    ('S', 'L'), ('T', 'K'), ('U', 'J'), ('V', 'I'), ('W', 'H'), ('X', 'G'), ('Y', 'F'), ('Z', 'E')
])
def test_decipher_character_d(key, deciphered_character):
    assert decipher_character('D', key) == deciphered_character
    assert decipher_character('d', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'E'), ('B', 'D'), ('C', 'C'), ('D', 'B'), ('E', 'A'), ('F', 'Z'), ('G', 'Y'), ('H', 'X'), ('I', 'W'),
    ('J', 'V'), ('K', 'U'), ('L', 'T'), ('M', 'S'), ('N', 'R'), ('O', 'Q'), ('P', 'P'), ('Q', 'O'), ('R', 'N'),
    ('S', 'M'), ('T', 'L'), ('U', 'K'), ('V', 'J'), ('W', 'I'), ('X', 'H'), ('Y', 'G'), ('Z', 'F')
])
def test_decipher_character_e(key, deciphered_character):
    assert decipher_character('E', key) == deciphered_character
    assert decipher_character('e', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'F'), ('B', 'E'), ('C', 'D'), ('D', 'C'), ('E', 'B'), ('F', 'A'), ('G', 'Z'), ('H', 'Y'), ('I', 'X'),
    ('J', 'W'), ('K', 'V'), ('L', 'U'), ('M', 'T'), ('N', 'S'), ('O', 'R'), ('P', 'Q'), ('Q', 'P'), ('R', 'O'),
    ('S', 'N'), ('T', 'M'), ('U', 'L'), ('V', 'K'), ('W', 'J'), ('X', 'I'), ('Y', 'H'), ('Z', 'G')
])
def test_decipher_character_f(key, deciphered_character):
    assert decipher_character('F', key) == deciphered_character
    assert decipher_character('f', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'G'), ('B', 'F'), ('C', 'E'), ('D', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'A'), ('H', 'Z'), ('I', 'Y'),
    ('J', 'X'), ('K', 'W'), ('L', 'V'), ('M', 'U'), ('N', 'T'), ('O', 'S'), ('P', 'R'), ('Q', 'Q'), ('R', 'P'),
    ('S', 'O'), ('T', 'N'), ('U', 'M'), ('V', 'L'), ('W', 'K'), ('X', 'J'), ('Y', 'I'), ('Z', 'H')
])
def test_decipher_character_g(key, deciphered_character):
    assert decipher_character('G', key) == deciphered_character
    assert decipher_character('g', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E'), ('E', 'D'), ('F', 'C'), ('G', 'B'), ('H', 'A'), ('I', 'Z'),
    ('J', 'Y'), ('K', 'X'), ('L', 'W'), ('M', 'V'), ('N', 'U'), ('O', 'T'), ('P', 'S'), ('Q', 'R'), ('R', 'Q'),
    ('S', 'P'), ('T', 'O'), ('U', 'N'), ('V', 'M'), ('W', 'L'), ('X', 'K'), ('Y', 'J'), ('Z', 'I')
])
def test_decipher_character_h(key, deciphered_character):
    assert decipher_character('H', key) == deciphered_character
    assert decipher_character('h', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'I'), ('B', 'H'), ('C', 'G'), ('D', 'F'), ('E', 'E'), ('F', 'D'), ('G', 'C'), ('H', 'B'), ('I', 'A'),
    ('J', 'Z'), ('K', 'Y'), ('L', 'X'), ('M', 'W'), ('N', 'V'), ('O', 'U'), ('P', 'T'), ('Q', 'S'), ('R', 'R'),
    ('S', 'Q'), ('T', 'P'), ('U', 'O'), ('V', 'N'), ('W', 'M'), ('X', 'L'), ('Y', 'K'), ('Z', 'J')
])
def test_decipher_character_i(key, deciphered_character):
    assert decipher_character('I', key) == deciphered_character
    assert decipher_character('i', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'J'), ('B', 'I'), ('C', 'H'), ('D', 'G'), ('E', 'F'), ('F', 'E'), ('G', 'D'), ('H', 'C'), ('I', 'B'),
    ('J', 'A'), ('K', 'Z'), ('L', 'Y'), ('M', 'X'), ('N', 'W'), ('O', 'V'), ('P', 'U'), ('Q', 'T'), ('R', 'S'),
    ('S', 'R'), ('T', 'Q'), ('U', 'P'), ('V', 'O'), ('W', 'N'), ('X', 'M'), ('Y', 'L'), ('Z', 'K')
])
def test_decipher_character_j(key, deciphered_character):
    assert decipher_character('J', key) == deciphered_character
    assert decipher_character('j', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'K'), ('B', 'J'), ('C', 'I'), ('D', 'H'), ('E', 'G'), ('F', 'F'), ('G', 'E'), ('H', 'D'), ('I', 'C'),
    ('J', 'B'), ('K', 'A'), ('L', 'Z'), ('M', 'Y'), ('N', 'X'), ('O', 'W'), ('P', 'V'), ('Q', 'U'), ('R', 'T'),
    ('S', 'S'), ('T', 'R'), ('U', 'Q'), ('V', 'P'), ('W', 'O'), ('X', 'N'), ('Y', 'M'), ('Z', 'L')
])
def test_decipher_character_k(key, deciphered_character):
    assert decipher_character('K', key) == deciphered_character
    assert decipher_character('k', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'L'), ('B', 'K'), ('C', 'J'), ('D', 'I'), ('E', 'H'), ('F', 'G'), ('G', 'F'), ('H', 'E'), ('I', 'D'),
    ('J', 'C'), ('K', 'B'), ('L', 'A'), ('M', 'Z'), ('N', 'Y'), ('O', 'X'), ('P', 'W'), ('Q', 'V'), ('R', 'U'),
    ('S', 'T'), ('T', 'S'), ('U', 'R'), ('V', 'Q'), ('W', 'P'), ('X', 'O'), ('Y', 'N'), ('Z', 'M')
])
def test_decipher_character_l(key, deciphered_character):
    assert decipher_character('L', key) == deciphered_character
    assert decipher_character('l', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'M'), ('B', 'L'), ('C', 'K'), ('D', 'J'), ('E', 'I'), ('F', 'H'), ('G', 'G'), ('H', 'F'), ('I', 'E'),
    ('J', 'D'), ('K', 'C'), ('L', 'B'), ('M', 'A'), ('N', 'Z'), ('O', 'Y'), ('P', 'X'), ('Q', 'W'), ('R', 'V'),
    ('S', 'U'), ('T', 'T'), ('U', 'S'), ('V', 'R'), ('W', 'Q'), ('X', 'P'), ('Y', 'O'), ('Z', 'N')
])
def test_decipher_character_m(key, deciphered_character):
    assert decipher_character('M', key) == deciphered_character
    assert decipher_character('m', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'N'), ('B', 'M'), ('C', 'L'), ('D', 'K'), ('E', 'J'), ('F', 'I'), ('G', 'H'), ('H', 'G'), ('I', 'F'),
    ('J', 'E'), ('K', 'D'), ('L', 'C'), ('M', 'B'), ('N', 'A'), ('O', 'Z'), ('P', 'Y'), ('Q', 'X'), ('R', 'W'),
    ('S', 'V'), ('T', 'U'), ('U', 'T'), ('V', 'S'), ('W', 'R'), ('X', 'Q'), ('Y', 'P'), ('Z', 'O')
])
def test_decipher_character_n(key, deciphered_character):
    assert decipher_character('N', key) == deciphered_character
    assert decipher_character('n', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'O'), ('B', 'N'), ('C', 'M'), ('D', 'L'), ('E', 'K'), ('F', 'J'), ('G', 'I'), ('H', 'H'), ('I', 'G'),
    ('J', 'F'), ('K', 'E'), ('L', 'D'), ('M', 'C'), ('N', 'B'), ('O', 'A'), ('P', 'Z'), ('Q', 'Y'), ('R', 'X'),
    ('S', 'W'), ('T', 'V'), ('U', 'U'), ('V', 'T'), ('W', 'S'), ('X', 'R'), ('Y', 'Q'), ('Z', 'P')
])
def test_decipher_character_o(key, deciphered_character):
    assert decipher_character('O', key) == deciphered_character
    assert decipher_character('o', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'P'), ('B', 'O'), ('C', 'N'), ('D', 'M'), ('E', 'L'), ('F', 'K'), ('G', 'J'), ('H', 'I'), ('I', 'H'),
    ('J', 'G'), ('K', 'F'), ('L', 'E'), ('M', 'D'), ('N', 'C'), ('O', 'B'), ('P', 'A'), ('Q', 'Z'), ('R', 'Y'),
    ('S', 'X'), ('T', 'W'), ('U', 'V'), ('V', 'U'), ('W', 'T'), ('X', 'S'), ('Y', 'R'), ('Z', 'Q')
])
def test_decipher_character_p(key, deciphered_character):
    assert decipher_character('P', key) == deciphered_character
    assert decipher_character('p', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'Q'), ('B', 'P'), ('C', 'O'), ('D', 'N'), ('E', 'M'), ('F', 'L'), ('G', 'K'), ('H', 'J'), ('I', 'I'),
    ('J', 'H'), ('K', 'G'), ('L', 'F'), ('M', 'E'), ('N', 'D'), ('O', 'C'), ('P', 'B'), ('Q', 'A'), ('R', 'Z'),
    ('S', 'Y'), ('T', 'X'), ('U', 'W'), ('V', 'V'), ('W', 'U'), ('X', 'T'), ('Y', 'S'), ('Z', 'R')
])
def test_decipher_character_q(key, deciphered_character):
    assert decipher_character('Q', key) == deciphered_character
    assert decipher_character('q', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'R'), ('B', 'Q'), ('C', 'P'), ('D', 'O'), ('E', 'N'), ('F', 'M'), ('G', 'L'), ('H', 'K'), ('I', 'J'),
    ('J', 'I'), ('K', 'H'), ('L', 'G'), ('M', 'F'), ('N', 'E'), ('O', 'D'), ('P', 'C'), ('Q', 'B'), ('R', 'A'),
    ('S', 'Z'), ('T', 'Y'), ('U', 'X'), ('V', 'W'), ('W', 'V'), ('X', 'U'), ('Y', 'T'), ('Z', 'S')
])
def test_decipher_character_r(key, deciphered_character):
    assert decipher_character('R', key) == deciphered_character
    assert decipher_character('r', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'S'), ('B', 'R'), ('C', 'Q'), ('D', 'P'), ('E', 'O'), ('F', 'N'), ('G', 'M'), ('H', 'L'), ('I', 'K'),
    ('J', 'J'), ('K', 'I'), ('L', 'H'), ('M', 'G'), ('N', 'F'), ('O', 'E'), ('P', 'D'), ('Q', 'C'), ('R', 'B'),
    ('S', 'A'), ('T', 'Z'), ('U', 'Y'), ('V', 'X'), ('W', 'W'), ('X', 'V'), ('Y', 'U'), ('Z', 'T')
])
def test_decipher_character_s(key, deciphered_character):
    assert decipher_character('S', key) == deciphered_character
    assert decipher_character('s', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'T'), ('B', 'S'), ('C', 'R'), ('D', 'Q'), ('E', 'P'), ('F', 'O'), ('G', 'N'), ('H', 'M'), ('I', 'L'),
    ('J', 'K'), ('K', 'J'), ('L', 'I'), ('M', 'H'), ('N', 'G'), ('O', 'F'), ('P', 'E'), ('Q', 'D'), ('R', 'C'),
    ('S', 'B'), ('T', 'A'), ('U', 'Z'), ('V', 'Y'), ('W', 'X'), ('X', 'W'), ('Y', 'V'), ('Z', 'U')
])
def test_decipher_character_t(key, deciphered_character):
    assert decipher_character('T', key) == deciphered_character
    assert decipher_character('t', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'U'), ('B', 'T'), ('C', 'S'), ('D', 'R'), ('E', 'Q'), ('F', 'P'), ('G', 'O'), ('H', 'N'), ('I', 'M'),
    ('J', 'L'), ('K', 'K'), ('L', 'J'), ('M', 'I'), ('N', 'H'), ('O', 'G'), ('P', 'F'), ('Q', 'E'), ('R', 'D'),
    ('S', 'C'), ('T', 'B'), ('U', 'A'), ('V', 'Z'), ('W', 'Y'), ('X', 'X'), ('Y', 'W'), ('Z', 'V')
])
def test_decipher_character_u(key, deciphered_character):
    assert decipher_character('U', key) == deciphered_character
    assert decipher_character('u', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'V'), ('B', 'U'), ('C', 'T'), ('D', 'S'), ('E', 'R'), ('F', 'Q'), ('G', 'P'), ('H', 'O'), ('I', 'N'),
    ('J', 'M'), ('K', 'L'), ('L', 'K'), ('M', 'J'), ('N', 'I'), ('O', 'H'), ('P', 'G'), ('Q', 'F'), ('R', 'E'),
    ('S', 'D'), ('T', 'C'), ('U', 'B'), ('V', 'A'), ('W', 'Z'), ('X', 'Y'), ('Y', 'X'), ('Z', 'W')
])
def test_decipher_character_v(key, deciphered_character):
    assert decipher_character('V', key) == deciphered_character
    assert decipher_character('v', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'W'), ('B', 'V'), ('C', 'U'), ('D', 'T'), ('E', 'S'), ('F', 'R'), ('G', 'Q'), ('H', 'P'), ('I', 'O'),
    ('J', 'N'), ('K', 'M'), ('L', 'L'), ('M', 'K'), ('N', 'J'), ('O', 'I'), ('P', 'H'), ('Q', 'G'), ('R', 'F'),
    ('S', 'E'), ('T', 'D'), ('U', 'C'), ('V', 'B'), ('W', 'A'), ('X', 'Z'), ('Y', 'Y'), ('Z', 'X')
])
def test_decipher_character_w(key, deciphered_character):
    assert decipher_character('W', key) == deciphered_character
    assert decipher_character('w', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'X'), ('B', 'W'), ('C', 'V'), ('D', 'U'), ('E', 'T'), ('F', 'S'), ('G', 'R'), ('H', 'Q'), ('I', 'P'),
    ('J', 'O'), ('K', 'N'), ('L', 'M'), ('M', 'L'), ('N', 'K'), ('O', 'J'), ('P', 'I'), ('Q', 'H'), ('R', 'G'),
    ('S', 'F'), ('T', 'E'), ('U', 'D'), ('V', 'C'), ('W', 'B'), ('X', 'A'), ('Y', 'Z'), ('Z', 'Y')
])
def test_decipher_character_x(key, deciphered_character):
    assert decipher_character('X', key) == deciphered_character
    assert decipher_character('x', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'Y'), ('B', 'X'), ('C', 'W'), ('D', 'V'), ('E', 'U'), ('F', 'T'), ('G', 'S'), ('H', 'R'), ('I', 'Q'),
    ('J', 'P'), ('K', 'O'), ('L', 'N'), ('M', 'M'), ('N', 'L'), ('O', 'K'), ('P', 'J'), ('Q', 'I'), ('R', 'H'),
    ('S', 'G'), ('T', 'F'), ('U', 'E'), ('V', 'D'), ('W', 'C'), ('X', 'B'), ('Y', 'A'), ('Z', 'Z')
])
def test_decipher_character_y(key, deciphered_character):
    assert decipher_character('Y', key) == deciphered_character
    assert decipher_character('y', key) == deciphered_character


@pytest.mark.parametrize('key,deciphered_character', [
    ('A', 'Z'), ('B', 'Y'), ('C', 'X'), ('D', 'W'), ('E', 'V'), ('F', 'U'), ('G', 'T'), ('H', 'S'), ('I', 'R'),
    ('J', 'Q'), ('K', 'P'), ('L', 'O'), ('M', 'N'), ('N', 'M'), ('O', 'L'), ('P', 'K'), ('Q', 'J'), ('R', 'I'),
    ('S', 'H'), ('T', 'G'), ('U', 'F'), ('V', 'E'), ('W', 'D'), ('X', 'C'), ('Y', 'B'), ('Z', 'A')
])
def test_decipher_character_z(key, deciphered_character):
    assert decipher_character('Z', key) == deciphered_character
    assert decipher_character('z', key) == deciphered_character


@pytest.mark.parametrize('character', ['1', '.', '"', '?', '!'])
@pytest.mark.parametrize('key', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
def test_deciphering_unknown_character_returns_character(character, key):
    assert decipher_character(character, key) == character


@pytest.mark.parametrize('character', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
@pytest.mark.parametrize('key', ['1', '.', '"', '?', '!'])
def test_deciphering_with_unknown_key_returns_character(character, key):
    assert decipher_character(character, key) == character
