from stats import count_char, count_words


def get_book_text(path):
    with open(path) as file:
        file_content = file.read()
    return file_content


def main():
    file_content = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_content)
    num_char = count_char(file_content)
    # print(f"{num_words} words found in the document")
    print(num_char)


main()
