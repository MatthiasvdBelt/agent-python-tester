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
