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
    # for char in chars:
    for letter in letters:
        for char in chars:
            if char == letter:
                if char not in char_dict:
                    char_dict[char] = 0
                    char_dict[char] += 1
                else:
                    char_dict[char] += 1
    return char_dict
    