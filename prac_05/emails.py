"""
CP1404/CP5632 Practical
Emails in dictionaries
"""


def main():
    """ Get email and name from user and store in a dictionary"""
    email_dict = {}

    email = input("Email: ")
    while email:
        name = get_name(email)
        name_correct_input = input(f"Is your name {name}? (Y/n) ").lower()
        if name_correct_input and name_correct_input != "y":
            name = input("Name: ")
        email_dict[email] = name
        email = input("Email: ")

    for email, name in email_dict.items():
        print(f"{name} ({email})")


def get_name(email):
    """ Extract name from email address """
    email_prefix = email.split('@')[0]
    words = email_prefix.split('.')
    return ' '.join([word.title() for word in words])


if __name__ == "__main__":
    main()
