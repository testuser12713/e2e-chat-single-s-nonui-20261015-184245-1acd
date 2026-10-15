"""Slug generation for free text."""

import re
import unicodedata

_NON_ALNUM_RUN = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return a URL-friendly slug built from the alphanumeric words of ``text``."""
    # NFKD splits accented letters into base letter + combining mark; encoding
    # to ASCII then drops the marks (and any character without an ASCII form).
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    lowered = folded.lower()
    hyphenated = _NON_ALNUM_RUN.sub("-", lowered)
    return hyphenated.strip("-")
