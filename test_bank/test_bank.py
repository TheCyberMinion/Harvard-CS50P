import pytest
from bank import value

def test_Small():
    assert value('hello') == 0
def test_Large():
    assert value('HELLO') == 0
def test_MIX():
    assert value('HeO') == 20
def test_Number():
    assert value('1') == 100
def test_HnumberLetter():
    assert value('h1') == 20
def test_NoHNumberLetter():
    assert value('g78') == 100
