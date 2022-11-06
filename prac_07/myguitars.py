"""CP1404/CP5632 Practical - Guitars reader"""
from prac_06.guitar import Guitar

GUITARS_FILE = "guitars.csv"


def main():
    guitars = []
    with open(GUITARS_FILE) as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            parts[1] = int(parts[1])  # Convert year to int
            parts[2] = float(parts[2])  # Convert price to float
            guitar = Guitar(*parts)
            print(guitar)
            guitars.append(guitar)
    guitars.sort()


if __name__ == "__main__":
    main()