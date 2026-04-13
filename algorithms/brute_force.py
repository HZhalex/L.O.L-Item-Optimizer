from __future__ import annotations


def search(pattern: str, text: str) -> list[int]:
    """Return all start indices where pattern appears in text (Naive)."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    matches: list[int] = []
    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            matches.append(i)

    return matches
