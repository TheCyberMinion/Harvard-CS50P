import pytest
from twttr import shorten

def test_Lowercase():
    assert shorten('twitter') == 'twttr'
def test_Uppercase():
    assert shorten('TWITTER') == 'TWTTR'
def test_WithNumber():
    assert shorten('tw12itter123') == 'tw12ttr123'
def test_EmptyStr():
    assert shorten('') == ''
def test_MixedCase():
    assert shorten('twiTTER') == 'twTTR'
def test_OnlyVowels():
    assert shorten('aeiou') == ''
def test_AllOnlyVowelsWithNumbers():
    assert shorten('aeiour567') == 'r567'
def test_SpecialChar():
    assert shorten('twitte!!!r') == 'twtt!!!r'
def test_MixedWithNumber():
    assert shorten('twit12te3r') == 'twt12t3r'
