"""
CP1404/CP5632 - Practical
Program to interact with the user using a menu.
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")
print(MENU)

choice = input("Choice: ").upper()

while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("Invalid input")

    print(MENU)
    choice = input("Choice: ").upper()

print("Finished.")
