"""Practical 10 - Program to print summary of a wikipedia page"""
import wikipedia


def main():
    """Print title, URL and summary of a wikipedia page based on user input"""
    search_term = input("Enter search term: ")
    while search_term != "":
        try:
            page = wikipedia.page(search_term, auto_suggest=False)
            print(page.title)
            print(page.url)
            print(page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        search_term = input("Enter search term: ")


if __name__ == '__main__':
    main()
