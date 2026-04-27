from __future__ import annotations


def _build_lps(pattern: str) -> list[int]:
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def search(pattern: str, text: str) -> list[int]:
    """Return all start indices where pattern appears in text (KMP)."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = _build_lps(pattern)
    matches: list[int] = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j - 1]

    return matches


def kmp_search(pattern: str, text: str) -> list[int]:
    """Backward-compatible alias for legacy imports."""
    return search(pattern, text)
