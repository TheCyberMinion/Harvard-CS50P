import csv
import sys

def file_name_checker_CSV(x):
    fileNameBroken = []
    fileName = x.strip()
    for _ in fileName:
        fileNameBroken.append(_)
    n = len(fileNameBroken)
    if fileNameBroken[n-1] == 'v'and fileNameBroken[n-2] == 's' and fileNameBroken[n-3] == 'c' and fileNameBroken[n-4] == '.' and n > 4:
        return True
    else:
        sys.exit('Not a CSV file')

def file_convert(x,y):
    try:
        with open(x) as file:
            reader = csv.DictReader(file)
            with open(y, 'w') as file2:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(file2, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    lastName, firstName = row['name'].strip().split(", ")
                    writer.writerow(
                        {
                            'first': firstName,
                            'last' : lastName,
                            'house' : row['house']
                        }
                    )
    except FileNotFoundError:
        sys.exit('File does not exist')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
else:
    if file_name_checker_CSV(sys.argv[1]) and file_name_checker_CSV(sys.argv[2]):
        file_convert(sys.argv[1],sys.argv[2])
    else:
        sys.exit('Not a CSV file')
