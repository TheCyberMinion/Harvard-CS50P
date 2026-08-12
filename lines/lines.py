import sys

# x is file name ex. file.py
def count_lines(x):
    filterdFile = []
    try:
        with open(x) as file:
            for _ in file:
                line = _.strip()
                if line == '' or line == ' ':
                    pass
                elif line[0] == '#':
                    pass
                else:
                    filterdFile.append(line)
    except FileNotFoundError:
        sys.exit('File does not exist')
    return len(filterdFile)

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
    if fileNameBroken[n-1] == 'y'and fileNameBroken[n-2] == 'p' and fileNameBroken[n-3] == '.' and n > 3:
        lengthFile = count_lines(fileName)
        print(lengthFile)
    else:
        sys.exit('Not a Python file')
