def is_valid(text):
    while True:
        if get_number(text):
            return True
        else:
            return False

def get_number(text):
    number = text
    if not (2 <= len(number) <= 6):
        return False
    return check_until_letters(number)

def check_until_letters(number):
    if not number.isalnum():
        return False
    if not number[0].isalpha():
        return False
    if not number[1].isalpha():
        return False
    for _ in range(2, len(number)):
        if number[_].isalpha():
            continue
        else:
            return check_form_numbers(number, _)
    return True

def check_form_numbers(number, x):
    if number[x] == '0':
        return False
    for _ in range((x + 1), len(number)):
        if not number[_].isdigit():
            return False
    return True

print(is_valid('12ABC'))

