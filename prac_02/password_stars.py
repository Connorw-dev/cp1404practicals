"""
CP1404 Practical 2
Program to do something
"""


def main():
    """ Function docstring"""
    min_length = 5
    password = get_password(min_length)
    print("*" * len(password))


def get_password(min_length):
    password = input("Create a password: ")
    while len(password) < min_length:
        print(f"Password must be > {min_length} characters")
        password = input("Create a password: ")
    return password


if __name__ == "__main__":
    main()
