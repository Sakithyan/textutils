"""Compute basic statistics about a text."""

import re
import string


def text_statistics(text):
    """Compute basic statistics about a text.

    A word is a whitespace-separated token containing at least one letter
    or digit, so tokens such as "..." are not counted.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    dict
        Dictionary with the keys:

        - ``word_count``: number of words.
        - ``character_count``: number of characters, spaces included.
        - ``sentence_count``: number of sentences (split on ``.``, ``!``, ``?``).
        - ``longest_word``: longest word without surrounding punctuation
          (first one in case of a tie, empty if no words).
        - ``average_word_length``: mean length of the whitespace-separated
          tokens, rounded to 2 decimals (0.0 if no words).

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = [w for w in text.split() if any(c.isalnum() for c in w)]
    word_count = len(words)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]

    if word_count == 0:
        longest_word = ""
        average_word_length = 0.0
    else:
        longest = max(words, key=lambda w: len(w.strip(string.punctuation)))
        longest_word = longest.strip(string.punctuation)
        average_word_length = round(sum(len(w) for w in words) / word_count, 2)

    return {
        "word_count": word_count,
        "character_count": len(text),
        "sentence_count": len(sentences),
        "longest_word": longest_word,
        "average_word_length": average_word_length,
    }
