from stats import word_count
from stats import char_count
from stats import sorted_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        book_text = file.read()
    return book_text

char_count = char_count(get_book_text('books/frankenstein.txt'))

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text('books/frankenstein.txt'))} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_char_count(char_count):

        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")


    print("============= END ===============")


main()

