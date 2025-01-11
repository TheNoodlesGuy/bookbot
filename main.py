def main():
    book_path = "books/frankenstein.txt"
    word_count = get_word_count(book_path)
    character_count = get_character_count(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    sorted_dict = get_sorted_dict(character_count)
    for item in sorted_dict:
        print(f"The '{item['character']}' character was found {item['occurences']} times")

    
def get_word_count(path):
    with open(path) as f:
        book_text = f.read()
    split_text = book_text.split()
    return len(split_text)

def get_character_count(path):
    with open(path) as f:
        book_text = f.read()
    character_dict = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def get_sorted_dict(dict):
    sorted = []
    for key in dict:
        temp_string = f"{key}"
        if temp_string.isalpha():
           temp_dict = {"character":key, "occurences":dict[key]}
           sorted.append(temp_dict)
    sorted.sort(reverse=True,key=sort_on)
    return sorted

def sort_on(dict):
    return dict["occurences"]

main()