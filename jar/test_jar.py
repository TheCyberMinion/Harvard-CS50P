import pytest
from jar import Jar

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar('testString')

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(4)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar(4)
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
