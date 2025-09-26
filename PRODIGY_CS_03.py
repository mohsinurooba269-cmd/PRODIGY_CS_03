import tkinter as tk
import re

def check_password_strength():
    password = entry.get()
    feedback = []
    strength = 0

    # Check length
    if len(password) < 8:
        feedback.append("❌ Password must be at least 8 characters long.")
    else:
        feedback.append("✅ Length is good.")
        strength += 1

    # Check lowercase
    if re.search(r"[a-z]", password):
        feedback.append("✅ Contains lowercase letters.")
        strength += 1
    else:
        feedback.append("❌ Add lowercase letters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        feedback.append("✅ Contains uppercase letters.")
        strength += 1
    else:
        feedback.append("❌ Add uppercase letters.")

    # Check digits
    if re.search(r"[0-9]", password):
        feedback.append("✅ Contains numbers.")
        strength += 1
    else:
        feedback.append("❌ Add numbers.")

    # Check special characters
    if re.search(r"[@$!%*?&]", password):
        feedback.append("✅ Contains special characters.")
        strength += 1
    else:
        feedback.append("❌ Add special characters like @, $, !, %.")

    # Strength result
    if strength <= 2:
        result = "🔴 Weak Password"
        color = "red"
    elif strength in (3, 4):
        result = "🟡 Medium Password"
        color = "orange"
    else:
        result = "🟢 Strong Password"
        color = "green"

    lbl_result.config(text=result, fg=color)
    txt_feedback.config(state="normal")
    txt_feedback.delete(1.0, tk.END)
    txt_feedback.insert(tk.END, "\n".join(feedback))
    txt_feedback.config(state="disabled")

def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
        btn_toggle.config(text="Show Password")
    else:
        entry.config(show="")
        btn_toggle.config(text="Hide Password")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x380")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

btn_toggle = tk.Button(root, text="Show Password", command=toggle_password, font=("Arial", 10))
btn_toggle.pack(pady=2)

btn = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12))
btn.pack(pady=10)

lbl_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
lbl_result.pack(pady=5)

txt_feedback = tk.Text(root, width=40, height=10, state="disabled", wrap="word")
txt_feedback.pack(pady=5)

root.mainloop()
