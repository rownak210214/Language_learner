import tkinter as tk
from tkinter import messagebox
import random

class LanguageLearningAppEnglish(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Learning App - English")
        self.geometry("400x200")

        self.label_word = tk.Label(self, text="")
        self.label_word.pack(pady=10)

        self.entry_translation = tk.Entry(self)
        self.entry_translation.pack(pady=5)

        self.check_button = tk.Button(self, text="Check", command=self.check_translation)
        self.check_button.pack(pady=5)

        self.next_button = tk.Button(self, text="Next", command=self.next_word)
        self.next_button.pack(pady=5)

        self.vocabulary = {
            "apple": "apple",
            "banana": "banana",
            "orange": "orange",
            "grape": "grape"
        }

        self.current_word = ""
        self.next_word()

    def next_word(self):
        self.current_word = random.choice(list(self.vocabulary.keys()))
        self.label_word.config(text=self.current_word)

    def check_translation(self):
        translation = self.entry_translation.get().strip()
        if translation == self.vocabulary[self.current_word]:
            messagebox.showinfo("Correct", "Your translation is correct!")
        else:
            messagebox.showerror("Incorrect", "Your translation is incorrect. Try again.")


if __name__ == "__main__":
    app = LanguageLearningAppEnglish()
    app.mainloop()
