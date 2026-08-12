import random

def main():
    rand = get_random(get_level())
    guess = get_guess()
    result(rand, guess)

def result(rand, guess):
    while True:
        if rand > guess:
            print('Too small!')
            continue
        elif rand < guess:
            print('Too large!')
            continue
        else:
            return print('Just right!')

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
            else:
                continue
        except ValueError:
            continue


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                continue
        except ValueError:
            continue

def get_random(x):
    return random.randint(1,x)

main()
