from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MatchResult:
    algorithm: str
    file_name: str
    pattern: str
    match_positions: list[int]
    elapsed_ms: float

    @property
    def match_count(self) -> int:
        return len(self.match_positions)
