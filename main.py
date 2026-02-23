# Main program for the assignment.
#Imports teh custom modules for formatting and statistics, 
# and uses datetime from the standard library.

from datetime import datetime  # built-in library module with the second import style: from module import function
import text_utils  # import style 1: import module_name
import stats_utils 

def main():
    raw_text = "   hello    from   python   programming!  \nThis is module 5.   "

    cleaned = text_utils.clean_text(raw_text)
    titled = text_utils.title_case(cleaned)

    print("Text Utility Project")
    print("Timestamp:", datetime.now())
    print()

    print("Original text:")
    print(raw_text)
    print()

    print("Cleaned text:")
    print(cleaned)
    print()

    print("Title cased text:")
    print(titled)
    print()

    print("Preview (first 30 chars):", text_utils.preview(titled))
    print("Word count:", stats_utils.word_count(cleaned))
    print("Character count:", stats_utils.char_count(cleaned))
    print("Line count:", stats_utils.line_count(raw_text))

if __name__ == "__main__":
    main()