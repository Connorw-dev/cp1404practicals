"""
CP1404/CP5632 - Practical
Program to determine score status.
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(get_result(score))

    random_score = randint(0, 100)
    print(f"Random score: {random_score}")
    print(get_result(random_score))


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score >= 0:
        return "Bad"
    else:
        return "Invalid score"


main()
