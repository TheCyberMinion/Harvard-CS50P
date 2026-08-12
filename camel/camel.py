word = str(input("Varibale Name: ")).strip()
result = []

for letter in word:
    if letter.isupper() and result:
        result.append(" ")
    result.append(letter)

length = len(result)

print("".join(result).lower().replace(" ","_"))
