import tkinter as tk
from tkinter import ttk

# English to Japanese dictionary
translations = {
    "hello": "こんにちは",
    "world": "世界",
    "python": "パイソン",
    "translator": "翻訳者",
    "example": "例",
    "program": "プログラム",
    "computer": "コンピュータ",
    "language": "言語",
    "code": "コード",
    "window": "ウィンドウ",
    "file": "ファイル",
    "network": "ネットワーク",
    "internet": "インターネット",
    # Add more translations as needed
}

def translate_text():
    english_word = english_entry.get().lower()
    if english_word in translations:
        japanese_label.config(text=translations[english_word])
    else:
        japanese_label.config(text="Translation not found")

# Create main window
root = tk.Tk()
root.title("English to Japanese Translator")

# Create frames
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
output_frame = ttk.Frame(root, padding="10")
output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input widgets
english_label = ttk.Label(input_frame, text="English Text:")
english_label.grid(row=0, column=0, sticky=tk.W)
english_entry = ttk.Entry(input_frame, width=50)
english_entry.grid(row=0, column=1)

# Output widgets
japanese_label = ttk.Label(output_frame, text="", wraplength=300, justify=tk.LEFT, anchor='nw', font=('Arial Unicode MS', 12))
japanese_label.grid(row=0, column=0, sticky=tk.W)

# Translate button
translate_button = ttk.Button(input_frame, text="Translate", command=translate_text)
translate_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
