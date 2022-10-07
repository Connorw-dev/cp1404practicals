"""
CP1404 Practical
Program to
"""
import random

TEMPLATE = "{0:2} {1:2} {2:2} {3:2} {4:2}"
def main():
    quick_pick_count = int(input("Number of quick picks: "))
    quick_picks = []
    while len(quick_picks) < 6:
        random_num = random.randint(1, 45)
        if random_num not in quick_picks:
            quick_picks.append(random_num)
    quick_picks.sort()
    print((" ".join(quick_picks)))
    print(TEMPLATE.format(*quick_picks))


if __name__ == "__main__":
    main()