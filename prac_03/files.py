"""
CP1404/CP5632 - Practical
Experiment with reading files
"""

# Program 1
name = input("Name: ")
with open("names.txt", "w") as name_file:
    print(name, file=name_file)

# Program 2
with open("names.txt", "r") as name_file:
    name = name_file.read().strip()
print(f"Your name is {name}")

# Program 3
with open("numbers.txt", "r") as numbers_file:
    lines = numbers_file.readlines()
result = int(lines[0]) + int(lines[1])
print(f"Sum of first two numbers: {result:,}")

# Program 4
with open("numbers.txt", "r") as numbers_file:
    sum = 0
    for line in numbers_file:
        sum += int(line.strip())
print(f"Sum of all numbers: {sum:,}")
