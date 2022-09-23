"""
CP1404 | prac_02 | score
Program to determine grade from inputted score and random score.
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    random_score = randint(0, 100)
    print(f"Random score: {random_score}")
    print(get_result(random_score))


def get_result(score):
    """ Return grade based on score """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score >= 0:
        return "Bad"
    else:
        return "Invalid score"


if __name__ == "__main__":
    main()
