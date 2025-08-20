def count_words(file_content):
    # split creates a list which elements are counted by len
    num_words = len(file_content.split())
    return num_words

    # or: return len(file_content.split())


def count_char(file_content):
    lower_string = file_content.lower()
    characters = {}
    for char in lower_string:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def sort_on(count):
    return count["num"]


def sort_list(char_dict):
    list_of_dict = []
    for char in char_dict:
        count = char_dict[char]
        new_dict = {"char": char, "num": count}
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)

    return list_of_dict
