""" CP1404 Practical
Program to load and save a data file and use a list of Project objects.
Estimated time: 30m
Actual time: 1h 30m
"""
from project import Project
from datetime import datetime
from operator import attrgetter

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> """
PROJECTS_FILE = "projects.txt"


def main():
    """ Menu-driven UI to load, save and use a list of Project objects"""
    projects = load_projects(PROJECTS_FILE)
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "l":
            projects_file = input("Projects filename: ")
            projects = load_projects(projects_file)
        elif choice == "s":
            projects_file = input("Projects filename: ")
            save_projects(projects, projects_file)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        choice = input(MENU).lower()
    save_projects(projects, PROJECTS_FILE)
    print("Thank you for using custom-built project management software.")


def load_projects(projects_file):
    """ Load projects from a file into memory with the correct variable types"""
    projects = []
    with open(projects_file) as in_file:
        # Consume CSV header
        in_file.readline()

        for line in in_file:
            parts = line.strip().split('\t')  # TAB delimiter
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(parts[0], start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(projects, projects_file):
    """ Save list of objects into a file"""
    with open(projects_file, "w") as out_file:
        for project in projects:
            print(project.name, project.start_date, project.priority,
                  project.cost_estimate, project.completion_percentage, sep="\t", file=out_file)


def display_projects(projects):
    """ Display a list of incomplete and completed projects"""
    completed_projects = sorted([project for project in projects if project.completion_percentage == 100])
    incomplete_projects = sorted(list(set(projects) - set(completed_projects)))
    print("Incomplete projects:")
    [print(f"  {project}", end="\n") for project in incomplete_projects]
    print("Completed projects:")
    [print(f"  {project}", end="\n") for project in completed_projects]


def filter_projects(projects):
    """ Display projects with start dates after a specified date"""
    chosen_date = datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= chosen_date]
    filtered_projects.sort(key=attrgetter('start_date'))
    [print(project) for project in filtered_projects]


def update_project(projects):
    """ Update a Project's percentage and priority"""
    [print(i, project) for i, project in enumerate(projects)]
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        projects[choice].completion_percentage = int(new_percentage)
    if new_priority:
        projects[choice].priority = int(new_priority)


def add_project(projects):
    """ Add a new project to memory"""
    print("Let's add a new project")
    projects.append(Project(input("Name: "),
                            datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date(),
                            int(input("Priority: ")),
                            float(input("Cost estimate: $")),
                            int(input("Percent complete: "))))


if __name__ == "__main__":
    main()
