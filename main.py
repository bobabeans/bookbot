import sys
from stats import word_count
from stats import char_count
from stats import sort_dicts
from stats import formatted

def main():
    total_words = word_count("./books/frankenstein.txt")
    print(f"Found {total_words} total words")

    char_stats = char_count("./books/frankenstein.txt")
    print(char_stats)

    output = sort_dicts("./books/frankenstein.txt")
    print(output)

    formatted("./books/frankenstein.txt")
    
main()
