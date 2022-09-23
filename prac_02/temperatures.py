"""
CP1404 Practical 2
Program to convert between celsius and fahrenheit.
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
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
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_fahrenheit(celsius):
    """
    Convert celsius to fahrenheit
    :param celsius: degrees C
    :return: degrees F
    """
    return celsius * 9.0 / 5 + 32


def get_celsius(fahrenheit):
    """
    Convert fahrenheit to celsius
    :param fahrenheit: degrees F
    :return: degrees C
    """
    return 5 / 9 * (fahrenheit - 32)


if __name__ == "__main__":
    main()
