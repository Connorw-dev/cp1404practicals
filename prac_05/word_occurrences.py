"""
CP1404/CP5632 Practical
Word occurrences in a string
"""


def main():
    words = input("String: ").split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    max_word_length = max([len(word) for word in word_to_count])
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{max_word_length}} : {count}")


if __name__ == "__main__":
    main()
