import tkinter as tk
from tkinter import ttk

def check_password():
    password = entry_pass.get()

    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.islower() for char in password):
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(not char.isalnum() for char in password):
        strength += 1


    progress["value"] = strength * 20

    if strength <= 2:
        result_label.config(text="WEAK PASSWORD", fg="red")

    elif strength == 3 or strength == 4:
        result_label.config(text="MEDIUM PASSWORD", fg="orange")

    else:
        result_label.config(text="STRONG PASSWORD", fg="green")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#f1f2f6")
root.resizable(False, False)

tk.Label(root, text="Password Strength Checker",
         font=("Arial", 14, "bold"),
         bg="#f1f2f6",
         fg="#2f3542").pack(pady=10)

tk.Label(root, text="Enter Password",
         bg="#d1d5e4").pack()

entry_pass = tk.Entry(root, width=30, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Check Strength",
          command=check_password,
          bg="#1e90ff",
          fg="white",
          width=15).pack(pady=10)

progress = ttk.Progressbar(root, length=250, maximum=100)
progress.pack(pady=10)

result_label = tk.Label(root, text="",
                        bg="#f1f2f6",
                        font=("Arial", 11, "bold"))
result_label.pack(pady=10)

root.mainloop()
