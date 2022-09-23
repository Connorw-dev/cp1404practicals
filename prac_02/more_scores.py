"""
CP1404 | prac_02 | more_scores
Program to grade multiple random scores
"""

from prac_02.score import get_result
from random import randint


def main():
    num_of_scores = int(input("Number of scores: "))
    scores = [randint(0, 100) for _ in range(num_of_scores)]
    results = [get_result(score) for score in scores]
    with open("score_result.txt", "w") as result_file:
        for idx, score in enumerate(scores):
            result_file.write(f"{score} is {results[idx]}\n")


if __name__ == "__main__":
    main()
