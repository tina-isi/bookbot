from stats import count_char, count_words, sort_list


def get_book_text(path):
    with open(path) as file:
        file_content = file.read()
    return file_content


def print_report(path):
    file_content = get_book_text(path)
    introduction(path)
    print_count_words(file_content)
    print_count_char(file_content)


def introduction(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")


def print_count_words(file_content):
    num_words = count_words(file_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


def print_count_char(file_content):
    num_char = count_char(file_content)
    list_of_dict = sort_list(num_char)
    print("--------- Character Count -------")
    for baby_dict in list_of_dict:
        if baby_dict["char"].isalpha():
            print(f'{baby_dict["char"]}: {baby_dict["num"]}')

    # {
    # 'char': ' ',
    # 'num': 70480
    # }
