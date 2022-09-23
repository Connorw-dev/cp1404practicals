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
"""


def main():
    choice = get_choice()
    score = -1
    while choice != "4":
        if choice == "1":
            score = float(input("Enter score: "))
            while not 0 <= score <= 100:
                print("Score must be between 0 and 100")
                score = float(input("Enter score: "))
        elif choice == "2":
            print(get_result(score))
        elif choice == "3":
            if score != -1:
                print("*" * int(score))
            else:
                print("Invalid score")
        choice = get_choice()


def get_choice():
    """ Print the menu and get user input """

    print(MENU)
    return input(">> ")


if __name__ == "__main__":
    main()
