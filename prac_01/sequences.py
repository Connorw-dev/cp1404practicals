MENUS = """
(4) Show the even numbers from x to y
(1) Show the odd numbers from x to y
(2) Show the squares from x to y
(e) Exit the program"""

print(MENUS)

menu_choice = input("> ")
while menu_choice.lower() != "e":
    x = int(input("x: "))
    y = int(input("y: "))

    if menu_choice == "1":
        x += x % 2
        print(', '.join([f"{i} " for i in range(x, y+1, 2)]))

    elif menu_choice == "2":
        x += not x % 2
        print(', '.join([f"{i} " for i in range(x, y + 1, 2)]))

    elif menu_choice == "3":
        print(', '.join([f"{i} " for i in range(x, y + 1) if (i ** 0.5).is_integer()]))

    print(MENUS)
    menu_choice = input("> ")