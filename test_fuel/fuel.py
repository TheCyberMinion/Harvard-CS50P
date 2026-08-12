def convert(fraction):
        fraction = fraction.strip()
        x, y = fraction.split("/")
        if x.isdigit() and y.isdigit():
               x, y = float(x), float(y)
               if x < 0 or y < 0:
                      raise ValueError
               else:
                      if y == 0:
                         raise ZeroDivisionError
                      else:
                             if x > y :
                                    raise ValueError
                             else:
                                    return int(round((x/y) * 100))
        else:
               raise ValueError

def gauge(percentage):
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return (f"{percentage}%")

print(convert('3/4'))
