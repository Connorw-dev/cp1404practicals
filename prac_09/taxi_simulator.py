"""Practical 9 - Taxi Simulator program using Taxi and SilverServiceTaxi classes."""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive
>>> """


def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0
    print("Let's drive!")
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)

            # Get taxi choice. Go back to menu if invalid
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice-1]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far? ")))
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill))
        menu_choice = input(MENU).lower()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display list of taxis."""
    [print(f"{i} - {taxi}") for i, taxi in enumerate(taxis, 1)]


if __name__ == '__main__':
    main()
