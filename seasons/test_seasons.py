import pytest
from datetime import date, datetime
from seasons import getDobAndValidate, getMinutes, printMinutes

def test_getDobAndValidate():
    assert getDobAndValidate(date.today(), '2003-02-02') == date(2003, 2, 2)
    with pytest.raises(SystemExit):
        getDobAndValidate(date.today(), '2030-02-02')
    with pytest.raises(SystemExit):
        getDobAndValidate(date.today(), '02-02-2003')

def test_getMinutes():
     assert getMinutes(date(2003, 2, 2), date(2002, 2, 2)) == 525600

def test_printMinutes():
     assert printMinutes(525600) == 'five hundred twenty-five thousand, six hundred'
