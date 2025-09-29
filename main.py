import sys
from stats import word_count
from stats import char_count
from stats import sort_dicts
from stats import formatted

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    formatted(f"{sys.argv[1]}")
    
main()
