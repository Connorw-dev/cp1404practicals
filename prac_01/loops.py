"""
CP1404/CP5632 - Practical
Program to print with for loops
"""

for i in range(1, 20 + 1, 2):
    print(i, end=' ')
print()

for i in range(0, 100 + 1, 10):
    print(i, end=' ')
print()

for i in range(20, 1 - 1, -1):
    print(i, end=' ')
print()

print('*' * int(input("Number of stars: ")))

for i in range(1, int(input("Number of stars: ")) + 1):
    print("*" * i)
