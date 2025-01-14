def main():
    file_path = "books/frankenstein.txt"
    file_contents = book_text(file_path)
    num_words = count_words(file_contents)
    num_letters_dict = count_letters(file_contents)
    num_letters_list = convert_to_list(num_letters_dict)
    num_letters_list.sort(reverse=True, key=sort_on_count)
    
    print(f"--- Begin report of {file_path} ---")
    print_report(num_words, num_letters_list)
    print("--- End report ---")

def book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}

    for char in text:
        if char.isalpha():
            letters[char.lower()] = letters.get(char.lower(), 0) + 1
    return letters

def print_report(num_words, num_letters):
    print(f"{num_words} words found in the document\n")
    
    for letter in num_letters:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    
def sort_on_count(num_letters):
    return num_letters["count"]

def convert_to_list(num_letters):
    return [{"letter": letter, "count": count} for letter, count in num_letters.items()]

main()
