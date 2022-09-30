"""
CP1404 | prac_02 | gopher_pop_simulator
Program to simulate a gopher population
"""

import random


def main():
    print("Welcome to the Gopher Population Simulator!")
    gopher_pop = int(input("Starting population: "))
    for year in range(1, 10 + 1):
        print()
        print(f"Year {year}")
        gopher_pop = update_gopher_pop(gopher_pop, (0.05, 0.15), (0.10, 0.20))


def update_gopher_pop(population, deathrate_min_max: tuple, birthrate_min_max: tuple):
    """Updates and prints the gopher population with deaths and births"""
    deaths = int(population * random.uniform(*deathrate_min_max))
    births = int(population * random.uniform(*birthrate_min_max))
    population -= deaths
    population += births
    print(f"{births} gophers were born. {deaths} gophers died.")
    print(f"Population: {population}")
    return population


if __name__ == "__main__":
    main()
