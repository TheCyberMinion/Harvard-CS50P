def value(text):
    greeting = text.strip().lower().replace(",","")
    x = greeting.split(" ")[0]
    if x == 'hello':
        return 0
    elif x[0] == 'h':
        return 20
    else:
        return 100
