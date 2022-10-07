"""
CP1404 Practical
Program to display stats about numbers
"""

NUMBER_COUNT = 5
USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """ Test for username and get stats from inputted numbers"""
    username = input("Username: ")
    if username in USERNAMES:
        print("Access granted")
    else:
        print("Access denied")

    numbers = [int(input("Number: ")) for _ in range(NUMBER_COUNT)]
    print_stats(numbers)


def print_stats(numbers):
    """ Print the stats of a list of numbers"""
    print(f"The first number is: {numbers[0]}")
    print(f"The last number is: {numbers[-1]}")
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
    print(f"The average number is: {sum(numbers) / len(numbers)}")


if __name__ == "__main__":
    main()
