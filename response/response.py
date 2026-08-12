import validators

def validate():
    UserEmail = input('Email: ').strip()
    if validators.email(UserEmail):
        return 'Valid'
    else:
        return 'Invalid'
def main():
    print(validate())

main()

