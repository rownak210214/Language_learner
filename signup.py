import tkinter as tk
from tkinter import messagebox

def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

def signup():
    def register_user():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        save_user(username, password)
        messagebox.showinfo("Success", "Signup successful! You can now login.")
        root.destroy()

    root = tk.Tk()
    root.title("Signup")
    root.geometry("300x150")

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    signup_button = tk.Button(root, text="Sign Up", command=register_user)
    signup_button.pack()

    root.mainloop()

if _name_ == "_main_":
    signup()
