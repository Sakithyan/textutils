import pytest

from textutils import character_count, reverse, word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 1),
        ("Hello World", 2),
        ("", 0),
        ("   ", 0),
        ("  Hello World  ", 2),
        ("Hello    World", 2),
        ("Hello\tWorld\nAgain", 3),
        ("open-source is great", 3),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 5),
        ("Hello World", 11),
        ("", 0),
        (" a ", 3),
        ("é!", 2),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", "olleH"),
        ("", ""),
        ("a", "a"),
        ("ab cd", "dc ba"),
        ("radar", "radar"),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


@pytest.mark.parametrize("function", [word_count, character_count, reverse])
@pytest.mark.parametrize("invalid_input", [None, 42, ["a"]])
def test_invalid_input_raises_typeerror(function, invalid_input):
    with pytest.raises(TypeError):
        function(invalid_input)
