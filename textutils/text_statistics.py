"""Compute basic statistics about a text."""

import re
import string


def text_statistics(text):
    """
    Compute basic statistics about a text.

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    dict
        A dictionary with the following keys:

        - ``word_count`` (int): number of words.
        - ``character_count`` (int): number of characters, including
          spaces and punctuation.
        - ``sentence_count`` (int): number of sentences, split on
          ``.``, ``!`` and ``?``.
        - ``longest_word`` (str): the longest word, without surrounding
          punctuation. The first one wins in case of a tie.
        - ``average_word_length`` (float): average number of characters
          per word, rounded to 2 decimals.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Notes
    -----
    Words are the whitespace-separated tokens of ``text``. The average
    word length is computed on these tokens, so attached punctuation
    counts toward their length.

    Examples
    --------
    >>> stats = text_statistics("You are the most incredible person.")
    >>> stats["word_count"]
    6
    >>> stats["character_count"]
    35
    >>> stats["sentence_count"]
    1
    >>> stats["longest_word"]
    'incredible'
    >>> stats["average_word_length"]
    5.0
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()
    word_count = len(words)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]

    if word_count == 0:
        longest_word = ""
        average_word_length = 0.0
    else:
        longest = max(words, key=lambda w: len(w.strip(string.punctuation)))
        longest_word = longest.strip(string.punctuation)
        average_word_length = round(
            sum(len(w) for w in words) / word_count, 2
        )

    return {
        "word_count": word_count,
        "character_count": len(text),
        "sentence_count": len(sentences),
        "longest_word": longest_word,
        "average_word_length": average_word_length,
    }