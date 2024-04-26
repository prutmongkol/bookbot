def main():
    file_path = "books/frankenstein.txt"

    print_report(file_path)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_list(text):
    char_dict = {}
    for char in text:
        if not char.isalpha():
            continue
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
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(dict):
    return dict["num"]

def print_report(path):
    text = get_book_text(path)
    
    print(f"--- Report of {path} ---")
    print(f"{get_num_words(text)} words found in the document")
    print()

    for char in get_char_list(text):
        print(f"Character '{char["char"]}' was found {char["num"]} times")

    print("--- End of report ---")
    

main()