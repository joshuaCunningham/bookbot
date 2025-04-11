from stats import word_count
from stats import char_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        book_text = file.read()
    return book_text

char_count = char_count(get_book_text('books/frankenstein.txt'))

def main():
    print(f"{word_count(get_book_text('books/frankenstein.txt'))} words found in the document")
    print(char_count)

main()