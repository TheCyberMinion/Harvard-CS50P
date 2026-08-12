import sys
import inflect
from datetime import date, datetime

def main():
    currentDate = date.today()
    dob = getDobAndValidate(currentDate, (input('Date Of Birth: ').strip()))
    minutes = getMinutes(currentDate, dob)
    print(f'{printMinutes(minutes).capitalize()} minutes')

def getDobAndValidate(currentDate, x):
    try:
        dob = datetime.strptime(x, "%Y-%m-%d").date()
    except ValueError:
        sys.exit('Invalid Date')

    if (dob > currentDate):
        sys.exit('Invalid Date')
    else:
        return dob

def getMinutes(currentDate, dob):
    return (currentDate - dob).days * 24 * 60

def printMinutes(minutes):
    getWords = inflect.engine()
    return getWords.number_to_words(minutes, andword= "")

if __name__ == "__main__":
    main()
