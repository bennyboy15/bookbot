def main():
    with open("github.com/USERNAME/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        return file_contents
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    new_dict = {}
    for char in text:
        new_char = char.lower()
        if new_char in new_dict:
            new_dict[new_char] += 1
        else:
            new_dict[new_char] = 1
    return new_dict
    
def sort_on(dict):
    return dict["num"]
    
def report(word_count, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    
    for thing in sorted_list:
        if thing["char"].isalpha() and thing["char"] != " ":
            print(f"The '{thing["char"]}' character was found {thing["num"]} times")
    print("--- End report ---")

if __name__ == "__main__":
    file_contents = main()
    print(count_words(file_contents))
    count_chars_dict = count_chars(file_contents)
    print(count_chars_dict)
    report(count_words(file_contents), count_chars_dict)