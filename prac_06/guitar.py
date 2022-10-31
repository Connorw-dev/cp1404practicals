"""CP1404/CP5632 Practical - Guitar class"""
import datetime

VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Return formatted string when printing object """
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """ Return age of guitar"""
        return datetime.date.today().year - self.year

    def is_vintage(self):
        """ return true if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
