import pytest
from um import count


def test_OnlyUM():
    assert count('um') == 1

def test_UMwITHMark():
    assert count('um?') == 1

def test_RandomUm():
    assert count('um mum rum umum mu mum um um') == 3

def text_Line():
    assert count('Um, thanks for the album.') == 1

def test_UMWITHDOT():
    assert count('Um, thanks, um...') == 2
