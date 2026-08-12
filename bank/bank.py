greeting = input("Say 'Hello' to get $100: ").strip().lower().replace(",","")
x = greeting.split(" ")[0]

if x == 'hello':
    print("$0")
elif x[0] == 'h':
    print("$20")
else:
    print("$100")
