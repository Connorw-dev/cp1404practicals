"""CP1404/CP5632 Practical - Programming Language"""


class ProgrammingLanguage:
    """ Represent a programming language """

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Return True/False if programming language is dynamically typed"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
