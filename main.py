"""CP1404 Theeradon Somsri practical3"""
'''password check'''

def main():
    """Start Program."""
    password = input("Enter a password")

    if check_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    return password == "12345678"


main()