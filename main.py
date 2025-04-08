def get_book_text(path_to_file):
    with open(path_to_file) as file:
        book_text = file.read()
    return book_text

def main():
    print(f"{word_count(get_book_text("books/frankenstein.txt"))} words found in the document")


def word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

main()