import emoji

def get_input():
    return str(input()).strip().lower()

def user_split(user_text):
    words = []
    while True:
        while ":" in user_text:
            a,b = user_text.split(":", 1)
            words.append(a.strip())
            user_text = b
        words.append(user_text.strip())
        return words

def convert_emoji(text):
    words = user_split(text)
    final_words = []
    for _ in words:
        replacement = emoji.emojize(f":{_}:")
        if ':' in replacement:
            final_words.append(_)
        else:
            final_words.append(replacement)
    return final_words

def final_output():
    text = get_input()
    final_words = convert_emoji(text)
    return print("".join(final_words))

def main():
   # final_output()
   text = get_input()
   print(emoji.emojize(text, language="alias"))

main()


