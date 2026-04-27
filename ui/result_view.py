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


def format_compare_summary(results: list[dict[str, float | int | str]]) -> str:
	if not results:
		return "No comparison result"

	parts = []
	for row in sorted(results, key=lambda item: float(item["elapsed_ms"])):
		parts.append(
			f"{row['algorithm']}: {int(row['matches'])} matches, "
			f"{float(row['elapsed_ms']):.3f} ms, ~{float(row['similarity']):.2f}%"
		)

	return "Compare | " + " | ".join(parts)


def format_corpus_top_summary(results: list[dict[str, float | int | str]], top_n: int = 5) -> str:
	if not results:
		return "No corpus ranking result"

	top = results[:top_n]
	parts = []
	for idx, row in enumerate(top, start=1):
		file_name = str(row["file_name"])
		parts.append(
			f"Top {idx}: {file_name} ~{float(row['similarity']):.2f}% "
			f"({int(row['matches'])} matches, {float(row['elapsed_ms']):.3f} ms)"
		)

	return "Corpus Ranking | " + " | ".join(parts)