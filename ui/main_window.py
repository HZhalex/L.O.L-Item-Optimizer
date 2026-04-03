from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from algorithms import (
	boyer_moore_search,
	brute_force_search,
	kmp_search,
	rabin_karp_search,
)
from ui.result_view import format_result_summary
from utils.file_loader import read_text_file
from utils.text_normalizer import normalize_text
from utils.timer import Timer


class MainWindow:
	def __init__(self) -> None:
		self.root = tk.Tk()
		self.root.title("Plagiarism Detection - String Matching")
		self.root.geometry("1000x700")

		self.text_content = ""

		self.pattern_var = tk.StringVar()
		self.algorithm_var = tk.StringVar(value="kmp")
		self.result_var = tk.StringVar(value="No analysis yet")

		self.text_widget: tk.Text | None = None

	def setup_ui(self) -> None:
		top = ttk.Frame(self.root, padding=10)
		top.pack(fill=tk.X)

		ttk.Button(top, text="Upload Text File", command=self._on_upload).pack(side=tk.LEFT)
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

		self.text_widget = tk.Text(self.root, wrap=tk.WORD, font=("Consolas", 11))
		self.text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
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

	def _on_run(self) -> None:
		if not self.text_content:
			messagebox.showwarning("Missing text", "Please upload a text file first.")
			return

		pattern = normalize_text(self.pattern_var.get())
		if not pattern:
			messagebox.showwarning("Missing pattern", "Please enter a pattern to search.")
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

		self._highlight_matches(matches, len(pattern))
		self.result_var.set(format_result_summary(algorithm, len(matches), elapsed_ms, len(pattern), len(text)))

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