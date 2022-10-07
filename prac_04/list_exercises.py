"""
CP1404 Practical
Program to display stats about numbers
"""

NUMBER_COUNT = 5


def main():
    numbers = [int(input("Number: ")) for _ in range(NUMBER_COUNT)]
    print(f"The first number is: {numbers[0]}")
    print(f"The last number is: {numbers[-1]}")
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
    print(f"The average number is: {sum(numbers)/len(numbers)}")


if __name__ == "__main__":
    main()
