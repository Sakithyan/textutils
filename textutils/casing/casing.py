import re


def capitalize_words(text):
    """
    Capitalize the first letter of each word in the given text.
    Args:
        text: The input string.
    Returns:
        The string with each word capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return re.sub(r"\S+", lambda match: match.group().capitalize(), text)
