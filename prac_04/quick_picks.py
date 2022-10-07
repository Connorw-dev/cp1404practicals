"""
CP1404 Practical
Program to display quick pick lines
"""
import random

LINE_TEMPLATE = "{0:2} {1:2} {2:2} {3:2} {4:2} {5:2}"
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """ Print n lines, each with 6 unique random numbers from 1-45"""
    quick_pick_count = int(input("Number of quick picks: "))

    for _ in range(quick_pick_count):
        quick_picks = []
        while len(quick_picks) < NUMBERS_PER_LINE:
            random_num = random.randint(MIN_NUMBER, MAX_NUMBER)
            if random_num not in quick_picks:
                quick_picks.append(random_num)
        quick_picks.sort()
        print(LINE_TEMPLATE.format(*quick_picks))


if __name__ == "__main__":
    main()
