"""Text truncation with an ellipsis."""


def truncate(text: str, max_len: int) -> str:
    """Return ``text`` shortened to at most ``max_len`` characters, ending in '...' when cut."""
    if max_len < 0:
        raise ValueError("max_len must not be negative")
    if len(text) <= max_len:
        return text
    if max_len < 3:
        # No room for the ellipsis: cut hard to the limit.
        return text[:max_len]
    return text[: max_len - 3] + "..."
