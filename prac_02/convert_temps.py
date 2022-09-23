"""
CP1404 | prac_02 | convert_temps
Program to convert multiple temperatures from text file
"""

from prac_02.temperatures import get_celsius
from random import uniform


def main():
    create_random_text(15, -200, 200)
    with open("temps_input.txt", "r") as temps_input_file:
        fahr_temps = [float(temp) for temp in temps_input_file.readlines()]
    with open("temps_output.txt", "w") as temps_output_file:
        temps_output_file.writelines([f"{get_celsius(fahr_temp)}\n"
                                      for fahr_temp in fahr_temps])


def create_random_text(count, min_value, max_value):
    """ Create temps_input.txt with random floats """
    with open("temps_input.txt", "w") as temps_file:
        for _ in range(count):
            temps_file.write(f"{uniform(min_value, max_value)}\n")


if __name__ == "__main__":
    main()
