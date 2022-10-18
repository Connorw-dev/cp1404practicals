"""
CP1404/CP5632 Practical
Get country and champion stats from Wimbledon
"""

CSV_FILE = "wimbledon.csv"


def main():
    """ Extract and print champions and countries from CSV file """
    csv_lines = load_csv()
    champion_wins_dict, countries = get_stats(csv_lines)
    display_champions(champion_wins_dict)
    print()
    display_countries(countries)


def display_countries(countries):
    """ Display the countries that have won a wimbledon, sorted."""
    unique_countries = sorted(set(countries))
    print(f"These {len(unique_countries)} countries have won Wimbledon:")
    print(f"{', '.join(unique_countries)}")


def display_champions(champion_wins_dict):
    """ Display each champion and their win count"""
    print("Wimbledon Champions:")
    for champion, wins in champion_wins_dict.items():
        print(f"{champion} {wins}")


def load_csv():
    """ Load the data of a CSV into memory """
    with open(CSV_FILE, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
    return lines


def get_stats(lines):
    """ Get champions and their countries from lines of CSV.
    Returns dict of champions and wins, and list of countries"""
    countries = []
    champion_wins_dict = {}
    for line in lines:
        elements = line.split(',')
        countries.append(elements[1])

        champion = elements[2]
        if champion in champion_wins_dict:
            champion_wins_dict[champion] += 1
        else:
            champion_wins_dict[champion] = 1

    return champion_wins_dict, countries


if __name__ == "__main__":
    main()
