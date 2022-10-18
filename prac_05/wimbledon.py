"""
CP1404/CP5632 Practical
Get country and champion stats from Wimbledon
"""

CSV_FILE = "wimbledon.csv"


def main():
    """ Extract and print champions and countries from CSV file """
    csv_lines = load_csv()
    display_stats(*get_stats(csv_lines))
    

def display_stats(champion_wins_dict, countries):
    """ Display the champion wins and winning countries"""

    print("Wimbledon Champions:")
    for champion, wins in champion_wins_dict.items():
        print(f"{champion} {wins}")
    print()
    unique_countries = sorted(set(countries))
    print(f"These {len(unique_countries)} countries have won Wimbledon:")
    print(f"{', '.join(unique_countries)}")


def load_csv():
    """ Load the data of a CSV into memory """
    with open(CSV_FILE, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
    return lines


def get_stats(lines):
    """ Get champions and their countries from lines of CSV.
    Returns dict of champions and wins, and list of countries"""
    countries = []
    champion_to_wins = {}
    for line in lines:
        elements = line.split(',')
        countries.append(elements[1])

        champion = elements[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1

    return champion_to_wins, countries


if __name__ == "__main__":
    main()
