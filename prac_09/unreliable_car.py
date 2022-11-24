"""CP1404 Practical 9 - Unreliable Car"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return string representation of UnreliableCar."""
        return f"{super().__str__()}, {self.reliability}% reliability"

    def drive(self, distance):
        """Drive like parent Car but with a chance of not driving at all."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
