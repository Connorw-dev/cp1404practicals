"""
CP1404 Practical 2
Program to convert multiple temperatures from text file
"""

from prac_02.temperatures import get_celsius
from random import random


def main():
    create_random_text(15, -200, 200)
    with open("temps_input.txt", "r") as temps_input_file:
        fahr_temps = [float(temp) for temp in temps_input_file.readlines()]
    with open("temps_output.txt", "w") as temps_output_file:
        temps_output_file.writelines([f"{get_celsius(fahr_temp)}\n"
                                      for fahr_temp in fahr_temps])


def create_random_text(count, min_value, max_value):
    """
    Create a random temps_input.txt file
    :param count: how many random temps?
    :param min_value: minimum temp value
    :param max_value: maximum temp value
    :return:
    """
    with open("temps_input.txt", "w") as temps_file:
        for _ in range(count):
            temps_file.write(f"{random() * (max_value - min_value) + min_value}\n")


if __name__ == "__main__":
    main()
