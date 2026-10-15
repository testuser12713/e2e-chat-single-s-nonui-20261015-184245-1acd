"""Package-level checks: the package imports and exposes the five public functions."""

import inspect

import textutils
from textutils import is_palindrome, reverse_words, slugify, truncate, word_count


def test_package_imports() -> None:
    assert textutils is not None


def test_public_functions_have_expected_signatures() -> None:
    expected = {
        slugify: ["text"],
        truncate: ["text", "max_len"],
        word_count: ["text"],
        is_palindrome: ["text"],
        reverse_words: ["text"],
    }
    for func, params in expected.items():
        assert callable(func)
        assert list(inspect.signature(func).parameters) == params
        assert inspect.signature(func).return_annotation is not inspect.Signature.empty
