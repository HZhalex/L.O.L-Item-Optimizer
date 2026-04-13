from __future__ import annotations

BASE = 256
MOD = 1_000_000_007


def search(pattern: str, text: str) -> list[int]:
    """Return all start indices where pattern appears in text (Rabin-Karp)."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    m = len(pattern)
    n = len(text)
    high_base = pow(BASE, m - 1, MOD)

    p_hash = 0
    t_hash = 0

    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD

    matches: list[int] = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i : i + m] == pattern:
            matches.append(i)

        if i < n - m:
            t_hash = (t_hash - ord(text[i]) * high_base) % MOD
            t_hash = (t_hash * BASE + ord(text[i + m])) % MOD

    return matches
