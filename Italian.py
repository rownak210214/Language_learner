import tkinter as tk
from tkinter import ttk

# English to Italian dictionary
translations = {
    "hello": "ciao",
    "world": "mondo",
    "python": "Python",
    "translator": "traduttore",
    "example": "esempio",
    "program": "programma",
    "computer": "computer",
    "language": "linguaggio",
    "code": "codice",
    "window": "finestra",
    "file": "file",
    "network": "rete",
    "internet": "internet",
    # Add more translations as needed
}

def translate_text():
    english_word = english_entry.get().lower()
    if english_word in translations:
        italian_label.config(text=translations[english_word])
    else:
        italian_label.config(text="Translation not found")

# Create main window
root = tk.Tk()
root.title("English to Italian Translator")

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
italian_label = ttk.Label(output_frame, text="", wraplength=300, justify=tk.LEFT, anchor='nw', font=('Arial Unicode MS', 12))
italian_label.grid(row=0, column=0, sticky=tk.W)

# Translate button
translate_button = ttk.Button(input_frame, text="Translate", command=translate_text)
translate_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
