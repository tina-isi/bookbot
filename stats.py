def count_words(file_content):
    # split creates a list which elements are counted by len
    num_words = len(file_content.split())
    return num_words

    # or: return len(file_content.split())


def count_char(file_content):
    lower_string = file_content.lower()
