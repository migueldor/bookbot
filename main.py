def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def sort_on(items):
    return items["num"]

from stats import word_count
from stats import char_count
from stats import char_count_dict_list

def main(path):
    char_counter = char_count_dict_list( char_count( get_book_text(path) ) )
    char_counter.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count( get_book_text(path) )} total words" )
    print("--------- Character Count -------")
    for char in char_counter:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main("books/frankenstein.txt")

