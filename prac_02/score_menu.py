"""
CP1404 | prac_02 | score_menu
Program to process inputted score with a menu
"""

from prac_02.score import get_result

MENU = """ 
(1) Enter score
(2) Print result
(3) Print Stars
(4) Quit
>>> 
"""


def main():
    choice = input(MENU)
    score = -1
    while choice != "4":
        if choice == "1":
            score = get_score()
        elif choice == "2":
            print_result(score)
        elif choice == "3":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = input(MENU)


def get_score():
    """ Get valid score """
    score = float(input("Enter score: "))
    while not 0 <= score <= 100:
        print("Score must be between 0 and 100")
        score = float(input("Enter score: "))
    return score


def print_result(score):
    """ Print grade based on score """
    print(get_result(score))


def print_stars(score):
    """ Print number of *'s equal to score """
    if score != -1:
        print("*" * int(score))
    else:
        print("Invalid score")


if __name__ == "__main__":
    main()
