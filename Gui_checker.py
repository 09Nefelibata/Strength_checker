import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    else:
        remarks += "❌ Password must be at least 8 characters long.\n"

    if re.search("[a-z]", password):
        strength += 1
    else:
        remarks += "❌ Add lowercase letters.\n"

    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks += "❌ Add uppercase letters.\n"

    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks += "❌ Add numbers.\n"

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "❌ Add special characters.\n"

    if strength == 5:
        return "✅ Strong Password!", "green"
    elif strength >= 3:
        return "⚠️ Moderate Password\n" + remarks, "orange"
    else:
        return "❌ Weak Password\n" + remarks, "red"

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    result, color = check_password_strength(password)
    result_label.config(text=result, fg=color)
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#f2f2f2")

title = tk.Label(root, text="🔐 Password Strength Checker", font=("Helvetica", 14, "bold"), bg="#f2f2f2")
title.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=on_check, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#f2f2f2", justify="left", wraplength=350)
result_label.pack(pady=10)

root.mainloop()
