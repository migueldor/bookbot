def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

from stats import word_count
from stats import char_count
def main():
    print( f"Found {word_count( get_book_text("books/frankenstein.txt") )} total words" )
    print( char_count( get_book_text("books/frankenstein.txt") ) )
main()

