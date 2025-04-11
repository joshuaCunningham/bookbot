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

def sorted_char_count(char_count):
    
    #create a list to hold our dictionaries
    char_list = []

    # convert dictionary to list of dictionaries
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    # sort the list of dictionaries by count (highest to lowest)
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

