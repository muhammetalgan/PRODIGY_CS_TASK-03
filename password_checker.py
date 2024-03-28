import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    score = 0
    errors = []
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        errors.append("Password must be at least 8 characters long.")
        suggestions.append("Consider using a longer password.")

    if re.search(r"\d", password):
        score += 1
    else:
        errors.append("Password must contain at least one digit.")
        suggestions.append("Consider adding numbers to your password.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        errors.append("Password must contain at least one uppercase letter.")
        suggestions.append("Consider using uppercase letters in your password.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        errors.append("Password must contain at least one lowercase letter.")
        suggestions.append("Consider using lowercase letters in your password.")

    if re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password):
        score += 1
    else:
        errors.append("Password must contain at least one special character.")
        suggestions.append("Consider adding special characters to your password.")

    return score, errors, suggestions

def check_password():
    password = entry_password.get()
    score, errors, suggestions = check_password_strength(password)

    if score == 5:
        messagebox.showinfo("Strong Password", "Your password is strong!")
    else:
        suggestion_text.set("\n".join(suggestions))
        score_text.set(f"Password Strength Score: {score}/5")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")

root.geometry("400x300")  # Set window size

label_instructions = tk.Label(root, text="Enter your password:", font=("Helvetica", 12))
label_instructions.pack(pady=10)

entry_password = tk.Entry(root, show="*", font=("Helvetica", 12))
entry_password.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password, font=("Helvetica", 12))
check_button.pack(pady=10)

suggestion_frame = tk.Frame(root, bd=1, relief=tk.SOLID)
suggestion_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

suggestion_label = tk.Label(suggestion_frame, text="Suggestions:", font=("Helvetica", 12))
suggestion_label.pack(pady=5)

suggestion_text = tk.StringVar()
suggestion_text_label = tk.Label(suggestion_frame, textvariable=suggestion_text, font=("Helvetica", 10), wraplength=350)
suggestion_text_label.pack(fill=tk.BOTH, expand=True)

score_text = tk.StringVar()
score_label = tk.Label(root, textvariable=score_text, font=("Helvetica", 12))
score_label.pack(pady=10)

root.mainloop()
