import operator

equ = str(input("Maths Time(x + y): ")).strip().lower()
x,y,z = equ.split(" ")
x = float(x)
z = float(z)

"""
#old approach works but does not look good

if y == '+':
    print(float(x) + float(z))
elif y == '-':
    print(float(x) - float(z))
elif y == '*':
    print(float(x) * float(z))
elif y == '/':
    print(float(x) / float(z))
"""

operations = {

    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
}

print(operations.get(y, lambda x,z: "Unknown" )(x,z))




