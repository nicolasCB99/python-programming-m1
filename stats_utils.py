# This module will computed the word/character/line counts
# so that the main.py can use them once connected

def word_count(text: str) -> int:
    
    # Counts the words in the text
    if not text.strip():
        return 0
    return len(text.split())

def char_count(text: str) -> int:
    
    # Count the characters in the text, which includs the spaces
    return len(text)

def line_count(text: str) -> int:

    #Count the lines in the text
    return len(text.splitlines()) if text else 0