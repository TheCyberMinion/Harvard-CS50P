def main():
    x = str(input("Tyep this ':)' or ':(' to see magic: "))
    convert(x)

def convert(x):
    print(x.replace(":)","🙂").replace(":(","🙁"))

main()
