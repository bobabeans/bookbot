from stats import word_count
from stats import char_count

def main():
    total_words = word_count("./books/frankenstein.txt")
    print(f"Found {total_words} total words")

    char_stats = char_count("./books/frankenstein.txt")
    print(char_stats)
    
main()
