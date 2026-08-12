def make_list():
    items = {}
    while True:
        try:
            item = str(input().strip().upper())
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1
        except EOFError:
            break
    return items

def print_list():
    item_list = make_list()
    for _ in sorted(item_list):
        print(f"{item_list[_]} {_}")

def main():
    print_list()

main()
