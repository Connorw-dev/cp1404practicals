""" CP1404 Practical 9 - Test UnreliableCar class """
from unreliable_car import UnreliableCar

my_car = UnreliableCar("Car 1", 100, 50)
my_car.drive(40)
print(my_car)
my_car.drive(100)
print(my_car)
