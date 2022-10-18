"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_TO_HEX = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7",
                 "AntiqueWhite1": "#ffefdb",
                 "AntiqueWhite2": "#eedfcc"}

COLOUR_TO_HEX = {k.lower(): v for k, v in COLOUR_TO_HEX.items()}  # convert keys to lower

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
