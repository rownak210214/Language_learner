import tkinter as tk
from tkinter import ttk

# English to Bangla dictionary
translations = {
    "hello": "হ্যালো",
    "world": "বিশ্ব",
    "python": "পাইথন",
    "translator": "অনুবাদক",
    "example": "উদাহরণ",
    "program": "প্রোগ্রাম",
    "computer": "কম্পিউটার",
    "language": "ভাষা",
    "code": "কোড",
    "window": "উইন্ডো",
    "file": "ফাইল",
    "network": "নেটওয়ার্ক",
    "internet": "ইন্টারনেট",
    "browser": "ব্রাউজার",
    "website": "ওয়েবসাইট",
    "database": "ডাটাবেস",
    "server": "সার্ভার",
    "client": "ক্লায়েন্ট",
    "programmer": "প্রোগ্রামার",
    "development": "উন্নতি",
    "application": "অ্যাপ্লিকেশন",
    "interface": "ইন্টারফেস",
    "input": "ইনপুট",
    "output": "আউটপুট",
    "function": "ফাংশন",
    "variable": "ভ্যারিয়েবল",
    "loop": "লুপ",
    "condition": "শর্ত",
    "statement": "বিবৃতি",
    "syntax": "সিনট্যাক্স",
    "compiler": "কম্পাইলার",
    "debugging": "ডিবাগিং",
    "algorithm": "এলগোরিদম",
    "bug": "বাগ",
    "error": "ত্রুটি",
    "memory": "মেমরি",
    "keyboard": "কীবোর্ড",
    "mouse": "মাউস",
    "click": "ক্লিক",
    "drag": "ড্র্যাগ",
    "drop": "ড্রপ",
}

def translate_text():
    english_word = english_entry.get().lower()
    if english_word in translations:
        bangla_label.config(text=translations[english_word])
    else:
        bangla_label.config(text="Translation not found")

# Create main window
root = tk.Tk()
root.title("English to Bangla Translator")

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
bangla_label = ttk.Label(output_frame, text="", wraplength=300, justify=tk.LEFT, anchor='nw', font=('Arial Unicode MS', 12))
bangla_label.grid(row=0, column=0, sticky=tk.W)

# Translate button
translate_button = ttk.Button(input_frame, text="Translate", command=translate_text)
translate_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
