"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_stats(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            data.append(parts)
    return data


def print_stats(data):
    """ Print the stats of classes from data"""
    for class_info in data:
        print(f"{class_info[0]} is taught by {class_info[1]} and has {class_info[2]} students")


main()
