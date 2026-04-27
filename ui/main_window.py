from __future__ import annotations

import csv
import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from algorithms import (
	boyer_moore_search,
	brute_force_search,
	kmp_search,
	rabin_karp_search,
)
from ui.result_view import format_compare_summary, format_corpus_top_summary, format_result_summary
from utils.file_loader import list_text_files, read_text_file
from utils.text_normalizer import normalize_text
from utils.timer import Timer


MISSING_PATTERN_TITLE = "Missing pattern"
MISSING_PATTERN_MSG = "Please enter a pattern to search."


class MainWindow:
	def __init__(self) -> None:
		self.root = tk.Tk()
		self.root.title("Plagiarism Detection - String Matching")
		self.root.geometry("1000x700")

		self.text_content = ""
		self.corpus_files: list[str] = []
		self.manual_corpus_files: list[str] = []
		self.folder_corpus_files: list[str] = []

		self.pattern_var = tk.StringVar()
		self.algorithm_var = tk.StringVar(value="kmp")
		self.result_var = tk.StringVar(value="No analysis yet")
		self.last_run_result: dict[str, float | int | str] | None = None
		self.last_compare_results: list[dict[str, float | int | str]] = []
		self.last_corpus_results: list[dict[str, float | int | str]] = []
		self.corpus_folder: str | None = None

		self.text_widget: tk.Text | None = None

	def _merge_corpus_files(self) -> list[str]:
		# Keep selection order while removing duplicate paths.
		seen: set[str] = set()
		merged: list[str] = []
		for file_path in [*self.manual_corpus_files, *self.folder_corpus_files]:
			key = str(Path(file_path).resolve())
			if key in seen:
				continue
			seen.add(key)
			merged.append(file_path)
		return merged

	def _refresh_corpus_selection(self) -> None:
		self.corpus_files = self._merge_corpus_files()
		self.result_var.set(
			"Corpus selected | "
			f"manual: {len(self.manual_corpus_files)} | "
			f"folder: {len(self.folder_corpus_files)} | "
			f"total unique: {len(self.corpus_files)}"
		)

	def setup_ui(self) -> None:
		top = ttk.Frame(self.root, padding=10)
		top.pack(fill=tk.X)

		ttk.Button(top, text="Upload Text File", command=self._on_upload).pack(side=tk.LEFT)
		ttk.Button(top, text="Select Corpus Files", command=self._on_select_corpus).pack(side=tk.LEFT, padx=(8, 0))
		ttk.Button(top, text="Select Corpus Folder", command=self._on_select_corpus_folder).pack(side=tk.LEFT, padx=(8, 0))
		ttk.Label(top, text="Pattern:").pack(side=tk.LEFT, padx=(12, 4))
		ttk.Entry(top, textvariable=self.pattern_var, width=30).pack(side=tk.LEFT)

		algo_box = ttk.Combobox(
			top,
			textvariable=self.algorithm_var,
			values=["brute_force", "kmp", "rabin_karp", "boyer_moore"],
			width=14,
			state="readonly",
		)
		algo_box.pack(side=tk.LEFT, padx=8)

		ttk.Button(top, text="Run Analysis", command=self._on_run).pack(side=tk.LEFT)
		ttk.Button(top, text="Compare Algorithms", command=self._on_compare).pack(side=tk.LEFT, padx=(8, 0))
		ttk.Button(top, text="Rank Corpus", command=self._on_rank_corpus).pack(side=tk.LEFT, padx=(8, 0))
		ttk.Button(top, text="Export Result", command=self._on_export).pack(side=tk.LEFT, padx=(8, 0))

		text_frame = ttk.Frame(self.root)
		text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

		y_scroll = ttk.Scrollbar(text_frame, orient=tk.VERTICAL)
		x_scroll = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL)

		self.text_widget = tk.Text(
			text_frame,
			wrap=tk.NONE,
			font=("Consolas", 11),
			yscrollcommand=y_scroll.set,
			xscrollcommand=x_scroll.set,
		)
		y_scroll.config(command=self.text_widget.yview)
		x_scroll.config(command=self.text_widget.xview)

		self.text_widget.grid(row=0, column=0, sticky="nsew")
		y_scroll.grid(row=0, column=1, sticky="ns")
		x_scroll.grid(row=1, column=0, sticky="ew")
		text_frame.rowconfigure(0, weight=1)
		text_frame.columnconfigure(0, weight=1)

		self.text_widget.tag_config("match", background="#FFE08A")

		ttk.Label(self.root, textvariable=self.result_var, anchor="w").pack(fill=tk.X, padx=10, pady=(0, 10))

	def _on_upload(self) -> None:
		file_path = filedialog.askopenfilename(
			title="Select text file",
			filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
		)
		if not file_path:
			return

		try:
			self.text_content = read_text_file(file_path)
			if self.text_widget:
				self.text_widget.delete("1.0", tk.END)
				self.text_widget.insert(tk.END, self.text_content)
			self.result_var.set(f"Loaded: {file_path}")
		except Exception as exc:
			messagebox.showerror("Read error", str(exc))

	def _on_select_corpus(self) -> None:
		file_paths = filedialog.askopenfilenames(
			title="Select corpus files",
			filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
		)
		if not file_paths:
			return

		self.manual_corpus_files = list(file_paths)
		self._refresh_corpus_selection()

	def _on_select_corpus_folder(self) -> None:
		folder_path = filedialog.askdirectory(title="Select corpus folder")
		if not folder_path:
			return

		try:
			text_files = list_text_files(folder_path)
		except Exception as exc:
			messagebox.showerror("Corpus read error", str(exc))
			return

		if not text_files:
			messagebox.showwarning("Empty corpus", "No .txt files found in selected folder.")
			return

		self.corpus_folder = folder_path
		self.folder_corpus_files = [str(path) for path in text_files]
		self._refresh_corpus_selection()

	def _on_run(self) -> None:
		if not self.text_content:
			messagebox.showwarning("Missing text", "Please upload a text file first.")
			return

		pattern = normalize_text(self.pattern_var.get())
		if not pattern:
			messagebox.showwarning(MISSING_PATTERN_TITLE, MISSING_PATTERN_MSG)
			return

		text = normalize_text(self.text_content)
		algorithm = self.algorithm_var.get()

		search_map = {
			"brute_force": brute_force_search,
			"kmp": kmp_search,
			"rabin_karp": rabin_karp_search,
			"boyer_moore": boyer_moore_search,
		}

		timer = Timer()
		timer.start()
		matches = search_map[algorithm](pattern, text)
		elapsed_ms = timer.stop()
		similarity = (len(matches) * len(pattern) / max(1, len(text))) * 100

		self._highlight_matches(matches, len(pattern))
		self.last_run_result = {
			"algorithm": algorithm,
			"matches": len(matches),
			"elapsed_ms": elapsed_ms,
			"similarity": similarity,
			"pattern": pattern,
			"text_len": len(text),
		}
		self.last_compare_results = []
		self.last_corpus_results = []
		self.result_var.set(format_result_summary(algorithm, len(matches), elapsed_ms, len(pattern), len(text)))

	def _on_compare(self) -> None:
		if not self.text_content:
			messagebox.showwarning("Missing text", "Please upload a text file first.")
			return

		pattern = normalize_text(self.pattern_var.get())
		if not pattern:
			messagebox.showwarning(MISSING_PATTERN_TITLE, MISSING_PATTERN_MSG)
			return

		text = normalize_text(self.text_content)
		results: list[dict[str, float | int | str]] = []

		search_map = {
			"brute_force": brute_force_search,
			"kmp": kmp_search,
			"rabin_karp": rabin_karp_search,
			"boyer_moore": boyer_moore_search,
		}

		for name, search_fn in search_map.items():
			timer = Timer()
			timer.start()
			matches = search_fn(pattern, text)
			elapsed_ms = timer.stop()
			similarity = (len(matches) * len(pattern) / max(1, len(text))) * 100
			results.append(
				{
					"algorithm": name,
					"matches": len(matches),
					"elapsed_ms": elapsed_ms,
					"similarity": similarity,
				}
			)

		selected = self.algorithm_var.get()
		selected_row = next((r for r in results if r["algorithm"] == selected), None)
		if selected_row is not None:
			self._highlight_matches(search_map[selected](pattern, text), len(pattern))

		self.last_compare_results = results
		self.last_run_result = None
		self.last_corpus_results = []
		self.result_var.set(format_compare_summary(results))

	def _on_rank_corpus(self) -> None:
		if not self.corpus_files:
			messagebox.showwarning("Missing corpus", "Please select corpus files first.")
			return

		pattern = normalize_text(self.pattern_var.get())
		if not pattern:
			messagebox.showwarning(MISSING_PATTERN_TITLE, MISSING_PATTERN_MSG)
			return

		algorithm = self.algorithm_var.get()
		search_map = {
			"brute_force": brute_force_search,
			"kmp": kmp_search,
			"rabin_karp": rabin_karp_search,
			"boyer_moore": boyer_moore_search,
		}
		search_fn = search_map[algorithm]

		results: list[dict[str, float | int | str]] = []
		for corpus_path in self.corpus_files:
			try:
				text = normalize_text(read_text_file(corpus_path))
			except Exception:
				continue

			timer = Timer()
			timer.start()
			matches = search_fn(pattern, text)
			elapsed_ms = timer.stop()
			similarity = (len(matches) * len(pattern) / max(1, len(text))) * 100
			similarity = min(100.0, similarity)

			results.append(
				{
					"algorithm": algorithm,
					"file_path": corpus_path,
					"file_name": Path(corpus_path).name,
					"matches": len(matches),
					"elapsed_ms": elapsed_ms,
					"similarity": similarity,
				}
			)

		if not results:
			messagebox.showwarning("No result", "Could not analyze selected corpus files.")
			return

		results.sort(key=lambda item: (-float(item["similarity"]), -int(item["matches"]), float(item["elapsed_ms"])))

		top = results[0]
		try:
			top_text_raw = read_text_file(str(top["file_path"]))
			top_text = normalize_text(top_text_raw)
			top_matches = search_fn(pattern, top_text)
			if self.text_widget:
				self.text_widget.delete("1.0", tk.END)
				self.text_widget.insert(tk.END, top_text_raw)
			self._highlight_matches(top_matches, len(pattern))
		except Exception:
			pass

		self.last_corpus_results = results
		self.last_compare_results = []
		self.last_run_result = None
		self.result_var.set(format_corpus_top_summary(results, top_n=5))

	def _on_export(self) -> None:
		if not self.last_run_result and not self.last_compare_results and not self.last_corpus_results:
			messagebox.showwarning("No result", "Please run analysis or compare algorithms first.")
			return

		file_path = filedialog.asksaveasfilename(
			title="Export result",
			defaultextension=".csv",
			filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json")],
		)
		if not file_path:
			return

		try:
			if file_path.lower().endswith(".json"):
				self._export_json(file_path)
			else:
				self._export_csv(file_path)
			self.result_var.set(f"Exported: {file_path}")
		except Exception as exc:
			messagebox.showerror("Export error", str(exc))

	def _export_csv(self, file_path: str) -> None:
		if self.last_corpus_results:
			rows = self.last_corpus_results
			fieldnames = ["algorithm", "file_name", "matches", "elapsed_ms", "similarity", "file_path"]
		elif self.last_compare_results:
			rows = self.last_compare_results
			fieldnames = ["algorithm", "matches", "elapsed_ms", "similarity"]
		else:
			rows = [self.last_run_result] if self.last_run_result else []
			fieldnames = ["algorithm", "matches", "elapsed_ms", "similarity"]

		with open(file_path, "w", newline="", encoding="utf-8") as output:
			writer = csv.DictWriter(output, fieldnames=fieldnames)
			writer.writeheader()
			for row in rows:
				payload: dict[str, str | int | float] = {
					"algorithm": str(row.get("algorithm", "")),
					"matches": int(row.get("matches", 0)),
					"elapsed_ms": f"{float(row.get('elapsed_ms', 0.0)):.3f}",
					"similarity": f"{float(row.get('similarity', 0.0)):.2f}",
				}
				if "file_name" in fieldnames:
					payload["file_name"] = str(row.get("file_name", ""))
					payload["file_path"] = str(row.get("file_path", ""))
				writer.writerow(payload)

	def _export_json(self, file_path: str) -> None:
		payload: dict[str, object]
		if self.last_corpus_results:
			payload = {"mode": "corpus_ranking", "results": self.last_corpus_results}
		elif self.last_compare_results:
			payload = {"mode": "compare", "results": self.last_compare_results}
		else:
			payload = {"mode": "single", "result": self.last_run_result}

		with open(file_path, "w", encoding="utf-8") as output:
			json.dump(payload, output, ensure_ascii=False, indent=2)

	def _highlight_matches(self, matches: list[int], pattern_len: int) -> None:
		if not self.text_widget:
			return
		self.text_widget.tag_remove("match", "1.0", tk.END)

		for pos in matches:
			start = f"1.0+{pos}c"
			end = f"1.0+{pos + pattern_len}c"
			self.text_widget.tag_add("match", start, end)

	def run(self) -> None:
		self.setup_ui()
		self.root.mainloop()