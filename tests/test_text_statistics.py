import pytest

from textutils import text_statistics


def test_example_from_issue():
    assert text_statistics("You are the most incredible person.") == {
        "word_count": 6,
        "character_count": 35,
        "sentence_count": 1,
        "longest_word": "incredible",
        "average_word_length": 5.0,
    }


def test_multiple_sentences():
    result = text_statistics("Hello world. How are you? Fine!")
    assert result == {
        "word_count": 6,
        "character_count": 31,
        "sentence_count": 3,
        "longest_word": "Hello",  # tie with "world": first one wins
        "average_word_length": 4.33,
    }


def test_no_terminal_punctuation_counts_one_sentence():
    result = text_statistics("Hello world")
    assert result["sentence_count"] == 1
    assert result["word_count"] == 2
    assert result["average_word_length"] == 5.0


def test_repeated_punctuation_is_one_separator():
    result = text_statistics("Wait... what?!")
    assert result["sentence_count"] == 2
    assert result["word_count"] == 2
    assert result["average_word_length"] == 6.5


def test_longest_word_has_no_surrounding_punctuation():
    result = text_statistics("Hi, everyone!")
    assert result["longest_word"] == "everyone"
    assert result["average_word_length"] == 6.0


def test_empty_string():
    assert text_statistics("") == {
        "word_count": 0,
        "character_count": 0,
        "sentence_count": 0,
        "longest_word": "",
        "average_word_length": 0.0,
    }


def test_only_whitespace():
    result = text_statistics("   ")
    assert result["word_count"] == 0
    assert result["character_count"] == 3
    assert result["sentence_count"] == 0
    assert result["longest_word"] == ""
    assert result["average_word_length"] == 0.0


def test_non_string_raises():
    with pytest.raises(TypeError):
        text_statistics(42)