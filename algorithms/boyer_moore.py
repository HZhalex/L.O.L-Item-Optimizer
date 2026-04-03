from __future__ import annotations


def _build_bad_char(pattern: str) -> dict[str, int]:
    table: dict[str, int] = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table


def search(pattern: str, text: str) -> list[int]:
    """Return all start indices where pattern appears in text (Boyer-Moore bad-char rule)."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    m = len(pattern)
    n = len(text)
    bad_char = _build_bad_char(pattern)
    matches: list[int] = []

    shift = 0
    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            matches.append(shift)
            shift += m - bad_char.get(text[shift + m], -1) if shift + m < n else 1
        else:
            mismatch = text[shift + j]
            shift += max(1, j - bad_char.get(mismatch, -1))

    return matches
