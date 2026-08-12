def shorten(text):
    vowels = ['A','E','I','O','U']
    file_name_new = []
    for _ in text:
        if _.upper() not in vowels:
            file_name_new.append(_)
    return ("".join(file_name_new))
