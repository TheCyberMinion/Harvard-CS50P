import random

def main():
    level = get_level()
    counter = make_problems(level)
    print(f'Score: {counter}')

#get level until a positive number comes thorugh 1/2/3 and then returns it
def get_level():
    while True:
        try:
            n = int(input())
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                continue
        except ValueError:
            continue
#generate random numbers based on level
def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
        return number
    elif level == 2:
        number = random.randint(10, 99)
        return number
    else:
        number = random.randint(100, 999)
        return number

#make problem by combining numbers
def make_problems(level):
    correct_counter = 0
    for _ in range(10): #runs it 10 times for 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        correct_counter = correct_counter + get_answers(x,y)
    return correct_counter

def get_answers(x,y):
    i = 1
    while i <= 3:
        try:
            guess = int(input(f'{x} + {y} = '))
            if guess != (x+y):
                print('EEE')
                i = i + 1
                continue
            else:
                return 1
        except ValueError:
            i = i + 1
            continue
    else:
        print(f'{x} + {y} = {x+y}')
        return 0

if __name__ == "__main__":
    main()
