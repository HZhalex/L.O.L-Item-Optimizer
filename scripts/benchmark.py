from __future__ import annotations

import csv
from pathlib import Path

from algorithms import boyer_moore, brute_force, kmp, rabin_karp
from utils.file_loader import list_text_files, read_text_file
from utils.text_normalizer import normalize_text
from utils.timer import Timer


ALGORITHMS = {
    "brute_force": brute_force.search,
    "kmp": kmp.search,
    "rabin_karp": rabin_karp.search,
    "boyer_moore": boyer_moore.search,
}


def run_benchmark(pattern: str, corpus_dir: str, output_csv: str) -> None:
    files = list_text_files(corpus_dir)
    rows: list[dict[str, str | int | float]] = []

    for file_path in files:
        text = normalize_text(read_text_file(file_path))
        for name, search_fn in ALGORITHMS.items():
            timer = Timer()
            timer.start()
            matches = search_fn(pattern, text)
            elapsed = timer.stop()
            similarity = (len(matches) * len(pattern) / max(1, len(text))) * 100

            rows.append(
                {
                    "file": file_path.name,
                    "algorithm": name,
                    "matches": len(matches),
                    "elapsed_ms": round(elapsed, 4),
                    "similarity_percent": round(similarity, 4),
                }
            )

    out = Path(output_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file", "algorithm", "matches", "elapsed_ms", "similarity_percent"],
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run_benchmark(pattern="sample pattern", corpus_dir="data/corpus", output_csv="report/benchmark.csv")
