"""CP1404/CP5632 Practical - Guitar class"""
import datetime


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
        """ return true if age of guitar >= 50"""
        return self.get_age() >= 50
