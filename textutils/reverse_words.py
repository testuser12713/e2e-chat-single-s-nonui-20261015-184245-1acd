"""Word order reversal."""


def reverse_words(text: str) -> str:
    """Return ``text`` with the order of its whitespace-separated words reversed."""
    return " ".join(reversed(text.split()))
