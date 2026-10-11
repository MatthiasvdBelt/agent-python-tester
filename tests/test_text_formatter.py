from src.text_formatter import TextFormatter


def test_format_title_standard():
    formatter = TextFormatter()
    assert formatter.format_title("hello world") == "Hello world"
    assert formatter.format_title("  welcome to agent testing  ") == "Welcome to agent testing"


def test_format_title_empty():
    formatter = TextFormatter()
    assert formatter.format_title("") == ""


def test_format_slug():
    formatter = TextFormatter()
    assert formatter.format_slug("New Feature: Multi-language Support!") == "new-feature-multi-language-support"


def test_truncate_shorter_or_equal():
    formatter = TextFormatter()
    # Length is strictly less than max_length
    assert formatter.truncate("hello", 10) == "hello"
    # Length is exactly max_length
    assert formatter.truncate("hello", 5) == "hello"
    # Empty string
    assert formatter.truncate("", 5) == ""


def test_truncate_exceeds_max_length():
    formatter = TextFormatter()
    # Default suffix "..." (length 3)
    assert formatter.truncate("hello world", 8) == "hello..."
    assert len(formatter.truncate("hello world", 8)) == 8

    # Custom suffix
    assert formatter.truncate("hello world", 8, suffix="--") == "hello --"
    assert len(formatter.truncate("hello world", 8, suffix="--")) == 8

    # Empty suffix
    assert formatter.truncate("hello world", 5, suffix="") == "hello"
    assert len(formatter.truncate("hello world", 5, suffix="")) == 5


def test_truncate_edge_cases():
    formatter = TextFormatter()
    # Truncate length equals suffix length
    assert formatter.truncate("abcdefg", 3, suffix="...") == "..."
    # Exact length matching with custom suffix
    assert formatter.truncate("abc", 3, suffix="...") == "abc"


def test_truncate_value_error():
    formatter = TextFormatter()
    try:
        formatter.truncate("hello", 2, suffix="...")
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert str(e) == "max_length cannot be shorter than suffix length"

    try:
        formatter.truncate("hello", -1, suffix="")
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert str(e) == "max_length cannot be shorter than suffix length"


