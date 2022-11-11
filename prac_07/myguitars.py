"""CP1404/CP5632 Practical - Guitars reader"""
from prac_06.guitar import Guitar

GUITARS_FILE = "guitars.csv"


def main():
    """ Print sorted list of guitars from CSV file. Add new guitars, then save"""
    guitars = load_guitars(GUITARS_FILE)
    guitars.sort()
    [print(guitar) for guitar in guitars]
    guitars += get_guitars()
    guitars.sort()
    [print(guitar) for guitar in guitars]
    save_guitars(GUITARS_FILE, guitars)


def load_guitars(guitar_file):
    """ Load guitars from CSV file into list, making sure variables are of the correct type"""
    guitars = []
    with open(guitar_file) as in_file:
        for line in in_file:
            parts: list = line.strip().split(',')
            parts[1] = int(parts[1])  # Convert year to int
            parts[2] = float(parts[2])  # Convert price to float
            guitars.append(Guitar(*parts))
    return guitars


def save_guitars(guitar_file, guitars):
    """ Save guitars list into a csv file"""
    with open(guitar_file, 'w') as out_file:
        for guitar in guitars:
            print(guitar.name, guitar.year, guitar.cost, sep=',', file=out_file)


def get_guitars():
    """ Interact with user to get a list of guitars"""
    guitars = []
    print()
    print("Adding new guitars")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    return guitars


if __name__ == "__main__":
    main()
