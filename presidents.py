#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Offline browser for the project's historical U.S. presidents dataset."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk

DATA = Path(__file__).resolve().parent / "presidents.json"

def load_presidents(path: Path = DATA) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expected a list of presidents")
    required = {"president", "number", "party", "took_office", "left_office", "history"}
    for index, item in enumerate(data):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Invalid president record at index {index}")
    return data

def description(item: dict) -> str:
    return (
        f"{item['number']}. {item['president']}\n"
        f"Party: {item['party']}\n"
        f"Term: {item['took_office']} to {item['left_office']}\n"
        f"Born: {item.get('birth_year', 'unknown')} | Died: {item.get('death_year', 'unknown')}\n\n"
        f"{item['history']}"
    )

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="Print the bundled names")
    args = parser.parse_args()
    presidents = load_presidents()
    if args.list:
        for item in presidents:
            print(f"{item['number']}. {item['president']}")
        return
    root = tk.Tk()
    root.title("U.S. Presidents — Historical Dataset")
    root.geometry("950x620")
    frame = ttk.Frame(root, padding=14)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Historical snapshot: data may not include recent presidencies").pack(anchor="w")
    content = ttk.Frame(frame)
    content.pack(fill="both", expand=True, pady=10)
    names = tk.Listbox(content, width=32, exportselection=False)
    names.pack(side="left", fill="y")
    portrait = ttk.Label(content)
    portrait.pack(side="right", padx=8)
    details = tk.Text(content, wrap="word", padx=12, pady=12)
    details.pack(side="left", fill="both", expand=True)
    for item in presidents:
        names.insert("end", f"{item['number']}. {item['president']}")
    def select(_event=None) -> None:
        selection = names.curselection()
        if not selection:
            return
        filename = Path(presidents[selection[0]]["picture"]).stem + "-ui.png"
        path = Path(__file__).resolve().parent / "pictures" / filename
        portrait.image = tk.PhotoImage(file=str(path)) if path.is_file() else None
        portrait.configure(image=portrait.image or "")
        details.config(state="normal")
        details.delete("1.0", "end")
        details.insert("1.0", description(presidents[selection[0]]))
        details.config(state="disabled")
    names.bind("<<ListboxSelect>>", select)
    if presidents:
        names.selection_set(0)
        select()
    root.mainloop()

if __name__ == "__main__":
    main()
