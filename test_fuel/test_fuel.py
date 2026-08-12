import pytest
from fuel import gauge
from fuel import convert

#test convert(fraction)
def test_fractions():
    assert convert('3/4') == 75

def test_Edgefractions():
    assert convert('1/4') == 25
    assert convert('0/4') == 0

def test_ZaeroError():
    try:
        convert('4/0')
    except ZeroDivisionError:
        assert True
    else:
        assert False

def test_NonDigitError():
    try:
        convert('cat/4')
    except ValueError:
        assert True
    else:
        assert False

def test_XmoreThanY():
    try:
        convert('5/4')
    except ValueError:
        assert True
    else:
        assert False

def test_XorYisNegative():
    try:
        convert('-3/4')
    except ValueError:
        assert True
    else:
        assert False

#test gauge(percentage)
def test_1Percent():
    assert gauge(1) == 'E'

def test_99Percent():
    assert gauge(99) == 'F'

def test_InBetweenPercent():
    assert gauge(48) == '48%'
