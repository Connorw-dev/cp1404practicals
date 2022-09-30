"""
CP1404/CP5632 - Practical
Experiment with reading files
"""
FILE_NAME = "names.txt"

name = input("Name: ")

with open(FILE_NAME, "w") as out_file:
    print(name, file=out_file)

with open(FILE_NAME, "r") as name_file:
    print(f"Your name is {name_file.read()}")

