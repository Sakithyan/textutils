import pytest

from textutils import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "Hello"),
        ("hello world", "Hello World"),
        ("HELLO WORLD", "Hello World"),
        ("", ""),
        ("  hello   world  ", "  Hello   World  "),
        ("élan vital", "Élan Vital"),
        ("it's a test", "It's A Test"),
        ("3rd place", "3rd Place"),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


@pytest.mark.parametrize("invalid_input", [None, 42, ["a"]])
def test_capitalize_words_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        capitalize_words(invalid_input)