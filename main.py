import sys
from stats import get_book_text, get_chars_dict, chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = num_book_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = chars_dict_to_sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")            

def num_book_words(file_contents):
    words = (file_contents.split())
    num_words = len(words)
    return num_words

main()