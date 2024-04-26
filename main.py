def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)

    print(get_num_words(file_contents))
    print(get_char_list(file_contents))

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_list(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1

    character_list = []
    for char in char_dict:
        character_list.append({
            "char": char,
            "num": char_dict[char]
        })
    return character_list

def print_report(text, path):
    print(f"--- Report of {path} ---")
    print(f"{get_num_words(text)} words found in the document")
    print()



main()