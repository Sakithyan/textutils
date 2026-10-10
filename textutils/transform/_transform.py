def word_count(text):
    """Count the words in a string.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    int
        Number of whitespace-separated words.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return len(text.split())


def character_count(text):
    """Count the characters in a string, spaces included.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    int
        Number of characters.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return len(text)


def reverse(text):
    """Reverse a string.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    str
        The text with its characters in reverse order.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return text[::-1]
