import re
import sys

def main():
    print(convert(input("Hours: ")), end = "")

def convert(s):
    if matches := re.search(r'^(?:([1][0-2]?|[2-9])(?::([0-5][0-9]))? (AM|PM)) to (?:([1][0-2]?|[2-9])(?::([0-5][0-9]))? (AM|PM))$', s.strip()):
        return f'{convert_Time(matches.group(1),matches.group(2),matches.group(3))} to {convert_Time(matches.group(4),matches.group(5),matches.group(6))}'
    else:
        raise Value

def convert_Time(a,b,c):
    a = int(a)
    if b is None:
        b = 0
    else:
        b = int(b)
    if c == 'PM':
        if a == 12:
            return f'{a:02d}:{b:02d}'
        else:
            a = a + 12
            return f'{a:02d}:{b:02d}'
    else:
        if a == 12:
            return f'00:{b:02d}'
        else:
            return f'{a:02d}:{b:02d}'

if __name__ == "__main__":
    main()
