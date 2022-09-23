"""
CP1404 | prac_02 | more_scores
Program to grade multiple random scores
"""

from prac_02.score import get_result
from random import randint


def main():
    # Get random scores and their grades
    num_of_scores = int(input("Number of scores: "))
    scores = [randint(0, 100) for _ in range(num_of_scores)]
    grades = [get_result(score) for score in scores]

    # Write to output file
    with open("score_result.txt", "w") as result_file:
        for idx, score in enumerate(scores):
            result_file.write(f"{score} is {grades[idx]}\n")


if __name__ == "__main__":
    main()
