"""Practical 9 -  Band class"""
from prac_09.musician import Musician

class Band:
    """Represent a Band object."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band instance."""
        return f"{self.name}: {', '.join([str(musician) for musician in self.musicians])}"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)


    def play(self):
        """All musicians play instrument on seperate lines. Ignore the None"""
        return '\n'.join([musician.play() for musician in self.musicians if musician.play() is not None])