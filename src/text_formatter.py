"""
Text Formatter and Multilingual Helper Service.
"""
import re


class TextFormatter:
    """
    Service for formatting, sanitizing, and preparing text strings.
    """

    def __init__(self, default_language: str = "en"):
        self.default_language = default_language.lower()

    def format_title(self, text: str) -> str:
        """Capitalize first character of text, stripping trailing whitespace."""
        if not text:
            return ""
        clean_text = text.strip()
        return clean_text[:1].upper() + clean_text[1:]

    def format_slug(self, text: str) -> str:
        """Convert string to a clean URL-friendly kebab-case slug."""
        if not text:
            return ""
        slug = re.sub(r"[^\w\s-]", "", text).strip().lower()
        return re.sub(r"[-\s]+", "-", slug)
