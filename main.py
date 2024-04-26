def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)

    print(count_words(file_contents))

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)    

main()