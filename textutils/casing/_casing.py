import re


def capitalize_words(text):
    """Capitalize the first letter of each word in a string.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    str
        The text with each word capitalized and spacing preserved.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return re.sub(r"\S+", lambda match: match.group().capitalize(), text)
