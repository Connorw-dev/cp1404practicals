"""
CP1404/CP5632 - Practical
Program to determine score status.
"""

score = float(input("Enter score: "))

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
elif score >= 0:
    print("Bad")
else:
    print("Invalid score")
