menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

bill = 0

def get_bill(item):
    global bill
    if item in menu:
        bill += float(menu[item])
        print(f"Total: ${bill:.2f}")
    else:
        pass

while True:
    try:
        item = str(input("Item: ")).strip().lower().title()
        get_bill(item)
    except EOFError:
        print()
        break
