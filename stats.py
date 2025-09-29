def get_book_text(filepath):
    with open(filepath) as f:
        content = file_contents = f.read()
        return content

def word_count(book):
    content = get_book_text(book)
    words = content.split()
    count = 0
    for word in words:
        count += 1
    return count

def char_count(book):
    content = get_book_text(book)
    content = content.lower()
    char_dict = {}
    chars = list(content)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z']

    for letter in letters:
        for char in chars:
            if char == letter:
                if char not in char_dict:
                    char_dict[char] = 0
                    char_dict[char] += 1
                else:
                    char_dict[char] += 1
    return char_dict

def sort_dicts(book):
    word_count = get_book_text(book)
    char_dict = char_count(book)
    sorted_output = []
    for char in char_dict:
        amount = char_dict[char]       
        sorted_output.append({"char": char, "num": amount})
    sorted_output.sort(reverse=True, key=sort_on)
    return sorted_output

def formatted(book):
    words = word_count(book)
    sorted_dicts = sort_dicts(book)
    print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {book}...\n"
        f"----------- Word Count ----------\n"
        f"Found {words} total words\n"
        f"--------- Character Count -------"
    )
    for d in sorted_dicts:
        print(f"{d["char"]}: {d["num"]}")

# helpers
def sort_on(items):
    return items["num"]