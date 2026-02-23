# This module focuses on the cleaning and formatting strings
# so that the main.py can use them once connected

def clean_text(text: str) -> str:

    # Removes the extra whitespace and trim the ends
    return " ".join(text.split())

def title_case(text: str) -> str:

    # Returns the text in title case, meaning each word capitalized
    return text.title()

def preview(text: str, n: int = 30) -> str:

    # Returns a short preview of the text, the default is 30 characters
    return text[:n]