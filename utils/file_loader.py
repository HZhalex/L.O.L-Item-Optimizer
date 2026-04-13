from __future__ import annotations

from pathlib import Path


def read_text_file(file_path: str | Path, encoding: str = "utf-8") -> str:
    return Path(file_path).read_text(encoding=encoding)


def list_text_files(folder_path: str | Path) -> list[Path]:
    folder = Path(folder_path)
    if not folder.exists():
        return []
    return sorted([p for p in folder.rglob("*.txt") if p.is_file()])
