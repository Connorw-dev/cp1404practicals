"""
CP1404/CP5632 - Practical
Experiment with reading files
"""

NAME_FILE = "names.txt"
NUMBERS_FILE = "numbers.txt"

name = input("Name: ")

with open(NAME_FILE, "w") as name_file:
    print(name, file=name_file)

with open(NAME_FILE, "r") as name_file:
    print(f"Your name is {name_file.read()}")

with open(NUMBERS_FILE, "r") as numbers_file:
    lines = numbers_file.readlines()

    result = int(lines[0].strip()) + int(lines[1].strip())
    print(f"Sum of first two numbers: {result:,}")

with open(NUMBERS_FILE, "r") as numbers_file:
    sum = 0
    for line in numbers_file:
        sum += int(line.strip())
    print(f"Sum of all numbers: {sum:,}")
