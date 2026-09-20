def word_count(text):
   """Count the number of words in the given text.
    Args:
        text: The input string.
    Returns:
        The number of words in the text.
    """
   return len(text.split())

def character_count(text):
   """Count the number of characters in the given text.
    Args:
        text: The input string.
    Returns:
        The number of characters in the text.
    """
   return len(text)

def reverse(text):
   """Reverse the given text.
    Args:
        text: The input string.
    Returns:
        The reversed string.
    """
   return text[::-1]