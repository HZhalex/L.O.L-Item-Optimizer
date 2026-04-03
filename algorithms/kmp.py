from __future__ import annotations


def _build_lps(pattern: str) -> list[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def search(pattern: str, text: str) -> list[int]:
    """Return all start indices where pattern appears in text (KMP)."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = _build_lps(pattern)
    matches: list[int] = []

    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return matches
