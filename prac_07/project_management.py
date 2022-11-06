""" CP1404 Practical
Program to load and save a data file and use a list of Project objects.
Estimated time: 30m
Actual time:
"""
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> """


def main():
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects()
        elif choice == "s":
            save_projects(projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        choice = input(MENU).lower()
    return


def load_projects():
    projects = []
    projects_file = input("Projects filename: ")
    with open(projects_file) as in_file:
        # Consume CSV header
        in_file.readline()

        for line in in_file:
            parts = line.strip().split('\t')  # TAB delimiter
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(parts[0], start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(projects):
    projects_file = input("Projects filename: ")
    with open(projects_file, "w") as out_file:
        for project in projects:
            print(project.name, project.start_date, project.priority,
                  project.cost_estimate, project.completion_percentage, sep="\t", file=out_file)


def display_projects(projects):
    completed_projects = [project for project in projects if project.completion_percentage == 100]
    incomplete_projects = list(set(projects) - set(completed_projects))
    print("Incomplete projects:")
    [print(project, end="\n") for project in incomplete_projects]
    print("Completed projects:")
    [print(project, end="\n") for project in completed_projects]


def filter_projects(projects):

def update_project(projects):
    [print(i, project) for i, project in enumerate(projects)]
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    if new_percentage:
        projects[choice].completion_percentage = new_percentage
    if new_priority:
        projects[choice].priority = new_priority


def add_project(projects):
    print("Let's add a new project")
    projects.append(Project(input("Name: "),
                            input("Start date (dd/mm/yy): "),
                            int(input("Priority: ")),
                            float(input("Cost estimate: $")),
                            int(input("Percent complete: "))))


if __name__ == "__main__":
    main()