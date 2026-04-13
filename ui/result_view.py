from __future__ import annotations


def format_result_summary(
	algorithm: str,
	match_count: int,
	elapsed_ms: float,
	pattern_len: int,
	text_len: int,
) -> str:
	similarity = (match_count * pattern_len / max(1, text_len)) * 100
	return (
		f"Algorithm={algorithm} | Matches={match_count} | "
		f"Elapsed={elapsed_ms:.3f} ms | Similarity~{similarity:.2f}%"
	)