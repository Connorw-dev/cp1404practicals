"""
CP1404/CP5632 Practical - Client code to test the Guitar class.
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(guitar)
print(f"Age: {guitar.get_age()}, Vintage? {guitar.is_vintage()}")
