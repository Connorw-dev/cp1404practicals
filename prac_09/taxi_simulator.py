"""Practical 9 - Taxi Simulator program using Taxi and SilverServiceTaxi classes."""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_to_drive = int(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill))
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display list of taxis."""
    [print(f"{i} - {taxi}") for i, taxi in enumerate(taxis)]


if __name__ == '__main__':
    main()
