filename = input("File directory")

with open(filename, "r") as file:
    for line in file.readlines():
        if line[0] == "#":
            print(line)