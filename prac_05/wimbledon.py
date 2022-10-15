"""
CP1404/CP5632 Practical
Get country and champion stats from Wimbledon
"""

CSV_FILE = "wimbledon.csv"


def main():
    champion_wins_dict = {}
    countries = []
    with open(CSV_FILE, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]

    for line in lines:
        elements = line.split(',')

        countries.append(elements[1])
        champion = elements[2]

        if champion in champion_wins_dict:
            champion_wins_dict[champion] += 1
        else:
            champion_wins_dict[champion] = 1

    print("Wimbledon Champions:")
    for champion, wins in champion_wins_dict.items():
        print(f"{champion} {wins}")
    print()

    unique_countries = sorted(set(countries))
    print(f"These {len(unique_countries)} countries have won Wimbledon:")
    print(f"{', '.join(unique_countries)}")


if __name__ == "__main__":
    main()
