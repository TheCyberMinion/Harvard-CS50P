import pytest
import os
from project import getFilePath, getContentFromFile, scoreEmail

def test_getFilePath():

    # checks if it takes argument with quotes edge case
    argList = ['main.py', r'"phish-triage\test_project.py"']
    assert getFilePath(argList) == r'phish-triage\test_project.py'

    # checks if it takes argument with no quotes
    argList = ['main.py', r'phish-triage\test_project.py']
    assert getFilePath(argList) == r'phish-triage\test_project.py'

    # checks if it exists with more than needed args
    argList = ['main.py', r'"phish-triage\test_project.py"', 'arg3']
    with pytest.raises(SystemExit):
        getFilePath(argList)

    # checks if it exists with less than needed args
    argList = ['main.py']
    with pytest.raises(SystemExit):
        getFilePath(argList)

def test_getContentFromFile():

    # make a .txt file just to test this function
    with open('testExample.txt', 'w') as file:
        file.write('this is just an example for test cases')

    # passing correct file path and getting bytes back
    assert getContentFromFile(r'testExample.txt') == b"this is just an example for test cases"

    # passing wrong or does not exist file path
    with pytest.raises(SystemExit):
        getContentFromFile(r'testExample.md')

    # passing wrong or does not exist file path
    with pytest.raises(SystemExit):
        getContentFromFile(r'')

    # delete the temp text file that got created to test this function
    os.remove('testExample.txt')

def test_scoreEmail():

    # passing the perfect email file
    assert scoreEmail(False, 'REJECT', 50, 50) == 100

    # passing imperfect email file
    assert scoreEmail(True, 'REJECT', 50, 25) == 75

    # testing urls both 0,0
    assert scoreEmail(False, 'REJECT', 0, 0) == 50
