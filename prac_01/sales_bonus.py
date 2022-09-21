"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales:
    if sales < 1000:
        bonus = 0.1 * sales
    else:
        bonus = 0.15 * sales
    print(f"Bonus: ${bonus}")
    sales = float(input("Enter sales: $"))
