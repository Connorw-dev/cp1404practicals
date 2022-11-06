""" CP1404 Practical
Program to load and save a data file and use a list of Project objects.
Estimated time: 30m
Actual time:
"""

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


if __name__ == "__main__":
    main()