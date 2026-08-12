accepted_money =  [25, 10, 5]
balance = 50

def ask_money():
    money_given = int(input("Put Money: "))
    if money_given in accepted_money:
        return money_given
    else:
        return 0

while balance > 0:
    m_given = ask_money()
    balance = balance - m_given
    print(f"Amount Due: {balance}")
else:
    print("Change Owed: "+ str(abs(balance)))
