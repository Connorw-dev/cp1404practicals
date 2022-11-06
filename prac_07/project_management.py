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
            update_project(project)
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

if __name__ == "__main__":
    main()