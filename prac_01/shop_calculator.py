"""
CP1404/CP5632 - Practical
Program to calculate total price of n items.
Discount applied to items priced over an amount.
"""

total_price = 0

# Make sure there's a valid input
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))


for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    if item_price > 100:
        item_price *= 0.9
    total_price += item_price
print(f"Total price for {number_of_items} items is ${total_price}")
