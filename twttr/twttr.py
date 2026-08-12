file_name = str(input("File Name: ")).strip()
vowels = ['A','E','I','O','U']

file_name_new = []

def shorten(file_name):
    for _ in file_name:
        if _.upper() in vowels:
            pass
        else:
            file_name_new.append(_)

shorten(file_name)
print("".join(file_name_new))







