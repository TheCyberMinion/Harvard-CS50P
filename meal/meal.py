def main():
    get_time = input("What time(##:##): ")
    x = convert(get_time)
    if (7.0 <= x <= 8.0):
        print("breakfast time")
    elif (12.0 <= x <= 13.0):
        print("lunch time")
    elif (18.0 <= x <= 19.0):
        print("dinner time")
    else:
        pass

def convert(time):
    firstHalf , secondHalf = time.strip().split(":")
    firstHalf , secondHalf = float(firstHalf), float(secondHalf)/60
    return firstHalf + secondHalf

if __name__ == "__main__":
    main()
