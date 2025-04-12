from stats import word_count
from stats import char_count
from stats import sorted_char_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        book_text = file.read()
    return book_text



def main():
    # char_count = char_count(get_book_text(sys.argv[1]))

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        
        book_text = get_book_text(sys.argv[1])
        print("----------- Word Count ----------")
        print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")

        char_count_result = char_count(get_book_text(sys.argv[1]))
        for char_dict in sorted_char_count(char_count_result):

            char = char_dict["char"]
            count = char_dict["count"]

            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")


main()

