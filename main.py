def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)

    print(count_words(file_contents))
    print(count_characters(file_contents))

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

main()