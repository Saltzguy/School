def get_words():
    more_words = "y"
    list_of_words = []
    while more_words[0].lower() == "y":
        list_of_words.append(input("Please input a word ->"))
        more_words = input("Do you want to input more words (yes or no) -> ")
    print_max_size(list_of_words)


def print_max_size(lst):
    print(str(max(map(len, lst))))


get_words()
