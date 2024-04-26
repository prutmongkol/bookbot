def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    print(count_words(file_contents))

def count_words(text):
    words = text.split()
    return len(words)    

main()