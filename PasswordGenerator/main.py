import tkinter as tk
from tkinter import messagebox
import string
import secrets


root = tk.Tk()
root.title(" My Password Ganerator")
root.geometry("500x600")

password_entry = tk.Entry(
    root,
    font=("Arial", 15),
    width=30,
    justify="center"
)
password_entry.pack(pady=20)

length_Label = tk.Label(
    root,
    text="Choose your password length",
    font=("Ariel",14)
)
length_Label.pack(pady=10)



password_length = tk.IntVar(value=12)

length_selector = tk.Spinbox(
    root,
    from_=4,
    to=64,
    textvariable=password_length,
    width=10
)

length_selector.pack(pady=10)

uppercase = tk.BooleanVar(value=True)
lowercase = tk.BooleanVar(value=True)
numbers = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)

uppercase_check = tk.Checkbutton(
    root,
    text="uppercase letters(ABC)",
    variable=uppercase
)
uppercase_check.pack()

lowercase_check = tk.Checkbutton(
    root,
    text="lowercase Letters (abc)",
    variable=lowercase
)

lowercase_check.pack()

numbers_check = tk.Checkbutton(
    root,
    text="numbers (123)",
    variable=numbers
)

numbers_check.pack()

symbols_check = tk.Checkbutton(
    root,
    text="Special Characters (!@#)",
    variable=symbols
)

symbols_check.pack()

def generate_password():
    characters = ""
    
    if uppercase.get():
        characters += string.ascii_uppercase

    if lowercase.get():
        characters += string.ascii_lowercase

    if numbers.get():
        characters += string.digits

    if symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning(
            "Warning",
            "Please select at least one character option."
        )
        return

    length = password_length.get()
    password = ""
    for i in range(length):
        password += secrets.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password
)

generate_button.pack(pady=20)

root.mainloop()

