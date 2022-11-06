"""
CP1404/CP5632 Practical
Project class
"""


class Project:
    """Represent information about a Project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Return less than method for Project"""
        return self.priority < other.priority

    def is_complete(self):
        """ Determines if project is completed"""
        return self.completion_percentage == 100
