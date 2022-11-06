"""
CP1404/CP5632 Practical
Project class
"""


class Project:
    """Represent information about a Project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}," \
               f" priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"