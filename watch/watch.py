import re
import sys

def main():
    print(parse(input("HTML: ")))

 # I did the large one bcz i wanted to practise regex and it
 # helped me short was pretty simple gonna submit the large one
 # since that is what i am more proud of but short one was preety easy
 # which i made with help of regex official documentations
 # but the long one is pure lecture

def parse(s):
    if matches := re.search(r"^<iframe (?:width=\"(?:[0-9]{1,3})\")? ?(?:height=\"(?:[0-9]{1,3})\")? ?(?:src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\") ?(?:title=\"[A-Za-z0-9 ]+\" frameborder=\"[0-9]+\" allow=\"[a-zA-Z0-9 ]+; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen>)? ?>?</iframe>$", s.strip()):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
