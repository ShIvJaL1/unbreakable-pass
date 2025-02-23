import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    char_set = ""
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        messagebox.showerror("Error", "Please select at least one character set!")
        return

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Widgets
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")  # Default length

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

# Run Application
root.mainloop()
