"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
"""
from prac_06.guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40)]

for guitar in guitars:
    print(guitar)