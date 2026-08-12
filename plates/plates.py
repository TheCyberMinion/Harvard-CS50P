def get_number():
    number = ask_number()
    if not (2 <= len(number) <= 6):
        return False
    return check_until_letters(number)

def ask_number():
    return str(input("Number Plate: ")).strip()

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

def main():
    while True:
        if get_number():
            print("Valid")
            break
        else:
            print("Invalid")
            break

main()

