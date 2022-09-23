"""
CP1404 | prac_02 | temperatures
Program to convert between celsius and fahrenheit.
"""


MENU = """
(C) Convert Celsius to Fahrenheit
(F) Convert Fahrenheit to Celsius
(Q) Quit
>> 
"""


def main():

    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = get_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        choice = input(MENU).upper()
    print("Thank you.")


def get_fahrenheit(celsius):
    """ Convert celsius to fahrenheit """
    return celsius * 9.0 / 5 + 32


def get_celsius(fahrenheit):
    """ Convert fahrenheit to celsius """
    return 5 / 9 * (fahrenheit - 32)


if __name__ == "__main__":
    main()
