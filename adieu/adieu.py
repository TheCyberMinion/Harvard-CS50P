import inflect

def main():
    names = make_list()
    p = inflect.engine()
    print()
    print("Adieu, adieu, to", p.join(names))

def make_list():
    names = []
    while True:
        try:
            names.append(get_text())
        except EOFError:
            return names

def get_text():
    return input('Name: ').strip().lower().title()

main()
