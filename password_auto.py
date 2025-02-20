import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_number = number_var.get()
        use_special = special_var.get()

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if use_uppercase else ''
        numbers = string.digits if use_number else ''
        special = string.punctuation if use_special else ''

        all_chars = lower + upper + numbers + special

        if not all_chars:
            messagebox.showerror("Error", "You must select at least one character type!")
            return
        
        password = ''.join(random.choice(all_chars) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

tk.Label(root, text="Password Length:", font=label_font, bg="#f0f0f0").pack(pady=5)
length_entry = tk.Entry(root, font=entry_font, width=10, justify='center')
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
number_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font=label_font, bg="#f0f0f0").pack(anchor='w', padx=80)
tk.Checkbutton(root, text="Include Numbers", variable=number_var, font=label_font, bg="#f0f0f0").pack(anchor='w', padx=80)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=label_font, bg="#f0f0f0").pack(anchor='w', padx=80)

tk.Button(root, text="Generate Password", font=button_font, bg="#4CAF50", fg="white", command=generate_password, padx=10, pady=5).pack(pady=10)


password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=entry_font, state='readonly', width=30, justify='center')
password_entry.pack(pady=5)

root.mainloop()