import pytest
from plates import is_valid

def test_NumberInEnd():
    assert is_valid('CS50') == True

def test_NumberInEndBut0():
    assert is_valid('CS05') == False

def test_CharacterAfterNumeber():
    assert is_valid('CS50P') == False

def test_DecimalNumber():
    assert is_valid('PI3.14') == False

def single_Letter():
    assert is_valid('H') == False

def test_MoreThan6():
    assert is_valid('OUTATIME') == False

def test_StartWithNumnber():
    assert is_valid('1ABC') == False

def test_SecondLetterIsNumber():
    assert is_valid('A123') == False
