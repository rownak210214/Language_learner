import tkinter as tk
from tkinter import messagebox
import random

class LanguageLearningApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Learning App")
        self.geometry("400x300")

        # Vocabulary dictionary for English to Spanish
        self.vocabulary = {
            "apple": "manzana",
            "banana": "plátano",
            "orange": "naranja",
            "grape": "uva"
        }

        self.current_word = ""
        self.score = 0
        self.create_widgets()
        self.next_word()

    def create_widgets(self):
        self.label_word = tk.Label(self, text="")
        self.label_word.pack(pady=10)

        self.entry_translation = tk.Entry(self)
        self.entry_translation.pack(pady=5)

        self.check_button = tk.Button(self, text="Check", command=self.check_translation)
        self.check_button.pack(pady=5)

        self.next_button = tk.Button(self, text="Next", command=self.next_word)
        self.next_button.pack(pady=5)

        self.label_score = tk.Label(self, text=f"Score: {self.score}")
        self.label_score.pack(pady=5)

    def next_word(self):
        self.current_word = random.choice(list(self.vocabulary.keys()))
        self.label_word.config(text=self.current_word)

    def check_translation(self):
        translation = self.entry_translation.get().strip()
        if translation.lower() == self.vocabulary[self.current_word]:
            messagebox.showinfo("Correct", "Your translation is correct!")
            self.score += 1
        else:
            messagebox.showerror("Incorrect", "Your translation is incorrect. Try again.")

        # Update score label
        self.label_score.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    app = LanguageLearningApp()
    app.mainloop()
