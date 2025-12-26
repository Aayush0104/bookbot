def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_chars_dict(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        new_dict = {"char": char, "num": count}
        chars_list.append(new_dict)
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list
