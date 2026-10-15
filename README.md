# textutils

textutils ist eine kleine, eigenständige Python-Bibliothek mit fünf String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Sie hat keine Benutzeroberfläche und keine Datenhaltung und kommt ausschließlich mit der Standardbibliothek aus.

## Tech-Stack

- Python 3 (Standardbibliothek, keine Laufzeitabhängigkeiten)
- pytest (Tests)
- ruff (Linting und Formatierung)

## Installation

```bash
pip install -e .
```

Für Tests und Linting zusätzlich die Entwicklungsabhängigkeiten installieren:

```bash
pip install -e ".[dev]"
```

## Ausführen und Tests

Es gibt keinen Server und kein CLI. Die Bibliothek wird importiert:

```bash
python -c "import textutils"
```

Tests ausführen:

```bash
pytest
```

Linting:

```bash
ruff check .
```

## Öffentliche Funktionen

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words

slugify(text: str) -> str
truncate(text: str, max_len: int) -> str
word_count(text: str) -> int
is_palindrome(text: str) -> bool
reverse_words(text: str) -> str
```

Hinweis: Die Funktionen sind derzeit nur als Gerüst angelegt und werfen `NotImplementedError`, bis ihre Implementierung ergänzt wird.

## Funktionsumfang

- `slugify`: Text in einen URL-tauglichen Slug umwandeln
- `truncate`: Text auf eine maximale Länge kürzen (mit `...`)
- `word_count`: Anzahl der Wörter zählen
- `is_palindrome`: Prüfen, ob ein Text ein Palindrom ist
- `reverse_words`: Reihenfolge der Wörter umkehren
