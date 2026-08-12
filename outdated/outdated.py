month_list = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def get_date_values():
    while True:
        user_date = str(input("Date: ")).strip()
        try:
            x,y,z = user_date.split("/")
            if int(x) > 0 and int(x) <= 12:
                if int(y) > 0 and int(y) <= 31:
                    return x,y,z
                else:
                    continue
            else:
                continue
        except ValueError:
            try:
                firstHalf,z = user_date.split(",")
                x,y = firstHalf.split(" ")
                if x in month_list:
                    if int(y) > 0 and int(y) <= 31:
                        return x,y,z
                    else:
                        continue
                else:
                    continue
            except ValueError:
                continue

def final_month_value(month):
    if month.isdigit():
        return month
    else:
        return str(month_list[month])

def print_output():
    month,date,year = get_date_values()
    month = final_month_value(month.lower().title())
    month = int(month.strip())
    year = int(year.strip())
    date = int(date.strip())
    return print(f"{year}-{month:02}-{date:02}")

def main():
    print_output()

main()
