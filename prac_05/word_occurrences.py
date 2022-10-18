"""
CP1404/CP5632 Practical
Word occurrences in a string
"""


def main():
    words = input("String: ").split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    max_word_length = max([len(word) for word in word_dict])
    for word, count in sorted(word_dict.items()):
        print(f"{word:{max_word_length}} : {count}")


if __name__ == "__main__":
    main()
