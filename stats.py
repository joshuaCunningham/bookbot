def word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def char_count(book_text):
    words = book_text.lower()
    # words.lower()
    char_count = {}

    for char in words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count