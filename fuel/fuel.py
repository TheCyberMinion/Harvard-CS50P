def get_reading():
    while True:
        fraction = str(input("Give me fraction: ")).strip()
        try:
            x, y = fraction.split("/")
            try:
                if x.isdigit() and y.isdigit():
                    x, y = float(x), float(y)
                    try:
                        if x <= y and x >= 0 and y > 0:
                            try:
                                return x/y
                            except ZeroDivisionError:
                                continue
                    except ValueError:
                        continue
            except ValueError:
                continue
        except ValueError:
            continue

def gauge():
        output = int(round(get_reading() * 100))
        if output <= 1:
            print("E")
        elif output >= 99:
            print("F")
        else:
            print(f"{output}%")

def main():
    gauge()

main()
