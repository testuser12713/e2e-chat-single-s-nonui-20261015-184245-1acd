"""Palindrome detection."""


def is_palindrome(text: str) -> bool:
    """Return True if ``text`` reads the same forwards and backwards, ignoring case and punctuation."""
    cleaned = [char.casefold() for char in text if char.isalnum()]
    return cleaned == cleaned[::-1]
