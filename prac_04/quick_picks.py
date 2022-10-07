"""
CP1404 Practical
Program to display quick pick lines
"""
import random

LINE_TEMPLATE = "{0:2} {1:2} {2:2} {3:2} {4:2} {5:2}"


def main():
    quick_pick_count = int(input("Number of quick picks: "))

    for _ in range(quick_pick_count):
        quick_picks = []
        while len(quick_picks) < 6:
            random_num = random.randint(1, 45)
            if random_num not in quick_picks:
                quick_picks.append(random_num)
        quick_picks.sort()
        print(LINE_TEMPLATE.format(*quick_picks))


if __name__ == "__main__":
    main()
