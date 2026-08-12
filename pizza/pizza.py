import sys
import csv
from tabulate import tabulate

def print_file(x):
    try:
        with open(x) as file:
            reader = csv.reader(file)
            formatterFile = list(reader)
            headers = formatterFile[0] #the first line is headers
            rows = formatterFile[1:] # the rest
    except FileNotFoundError:
        sys.exit('File does not exist')
    return print(tabulate(rows, headers=headers, tablefmt='grid'))


if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
else:
    fileNameBroken = []
    fileName = (sys.argv[1]).strip()
    for _ in fileName:
        fileNameBroken.append(_)
    n = len(fileNameBroken)
    if fileNameBroken[n-1] == 'v'and fileNameBroken[n-2] == 's' and fileNameBroken[n-3] == 'c' and fileNameBroken[n-4] == '.' and n > 4:
        print_file(fileName)
    else:
        sys.exit('Not a CSV file')
