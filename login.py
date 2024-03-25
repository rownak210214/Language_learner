import tkinter as tk
from tkinter import messagebox

def load_users():
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users.append((username, password))
    except FileNotFoundError:
        pass
    return users

def login():
    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        users = load_users()
        for user in users:
            if user[0] == username and user[1] == password:
                messagebox.showinfo("Success", "Login successful!")
                root.destroy()
                return

        messagebox.showerror("Error", "Invalid username or password")

    root = tk.Tk()
    root.title("Login")
    root.geometry("300x150")

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Login", command=check_credentials)
    login_button.pack()

    root.mainloop()

if _name_ == "_main_":
    login()
    