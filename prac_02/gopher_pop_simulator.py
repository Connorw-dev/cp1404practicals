"""
CP1404 Practical 2
Program to simulate a gopher population
"""
from random import uniform


def main():
    print("Welcome to the Gopher Population Simulator!")
    gopher_pop = int(input("Starting population: "))
    for year in range(1, 10 + 1):
        print()
        deaths = int(gopher_pop * uniform(0.05, 0.25))
        births = int(gopher_pop * uniform(0.10, 0.20))
        gopher_pop -= deaths
        gopher_pop += births
        print(f"Year {year}")
        print(f"{births} gophers were born. {deaths} gophers died.")
        print(f"Population: {gopher_pop}")


if __name__ == "__main__":
    main()
