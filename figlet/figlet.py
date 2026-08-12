import sys
import random
import pyfiglet
from pyfiglet import Figlet

def get_it_done():
    x = len(sys.argv)
    if (x > 3):
        sys.exit('Invalid usage')
    else:
        if (x == 1):
            input = get_text()
            F_font = get_font()
            figlet = Figlet(font=F_font)
            return print(figlet.renderText(input))
        elif (x == 2):
            if sys.argv[1] == '0':
                input = get_text()
                F_font = get_font()
                figlet = Figlet(font=F_font)
                return print(figlet.renderText(input))
            else:
                sys.exit('Invalid usage')
        else:
            if (sys.argv[1] == '-f' or sys.argv[1] == '-font'):
                input = get_text()
                F_font = sys.argv[2]
                try:
                    figlet = Figlet(font=F_font)
                    return print(figlet.renderText(input))
                except pyfiglet.FontNotFound:
                    sys.exit('Invalid usage')
            else:
                sys.exit('Invalid usage')

def get_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    return random.choice(fonts)

def get_text():
    return input("Input: ").strip()

def main():
    get_it_done()

main()
