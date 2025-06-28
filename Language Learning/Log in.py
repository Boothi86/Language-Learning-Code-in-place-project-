# import tkinter as tk
# from tkinter import messagebox
# import subprocess
# import re
# import os
#
# # === Path to Modules ===
# HIRAGANA_FILE = "Hiragna.py"
# WORDS_FILE = "Basic Words.py"
# QUIZ_FILE = "Quiz.py"
#
# class IchigoApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Ichigo Learning App")
#         self.frame = tk.Frame(master)
#         self.frame.pack(pady=20)
#
#         self.show_welcome_screen()
#
#     def clear_frame(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()
#
#     def show_welcome_screen(self):
#         self.clear_frame()
#         tk.Label(self.frame, text="🍓 Welcome to Ichigo Learning App 🍓", font=("Helvetica", 18)).pack(pady=10)
#         tk.Button(self.frame, text="Sign In", width=20, command=self.show_signin).pack(pady=5)
#         tk.Button(self.frame, text="Sign Up", width=20, command=self.show_signup).pack(pady=5)
#
#     def show_signin(self):
#         self.clear_frame()
#         tk.Label(self.frame, text="Sign In", font=("Helvetica", 16)).pack(pady=10)
#
#         tk.Label(self.frame, text="Name").pack()
#         self.signin_name = tk.Entry(self.frame)
#         self.signin_name.pack()
#
#         tk.Label(self.frame, text="5-digit Player ID").pack()
#         self.signin_id = tk.Entry(self.frame)
#         self.signin_id.pack()
#
#         tk.Button(self.frame, text="Login", command=self.login_user).pack(pady=10)
#         tk.Button(self.frame, text="Back", command=self.show_welcome_screen).pack()
#
#     def login_user(self):
#         name = self.signin_name.get().strip()
#         pid = self.signin_id.get().strip()
#
#         if not (name and pid.isdigit() and len(pid) == 5):
#             messagebox.showerror("Error", "Please enter valid name and 5-digit Player ID.")
#             return
#
#         self.username = name
#         self.show_main_menu()
#
#     def show_signup(self):
#         self.clear_frame()
#         tk.Label(self.frame, text="Sign Up", font=("Helvetica", 16)).pack(pady=10)
#
#         tk.Label(self.frame, text="Name").pack()
#         self.signup_name = tk.Entry(self.frame)
#         self.signup_name.pack()
#
#         tk.Label(self.frame, text="Age").pack()
#         self.signup_age = tk.Entry(self.frame)
#         self.signup_age.pack()
#
#         tk.Label(self.frame, text="Email").pack()
#         self.signup_email = tk.Entry(self.frame)
#         self.signup_email.pack()
#
#         tk.Button(self.frame, text="Register", command=self.register_user).pack(pady=10)
#         tk.Button(self.frame, text="Back", command=self.show_welcome_screen).pack()
#
#     def register_user(self):
#         name = self.signup_name.get().strip()
#         age = self.signup_age.get().strip()
#         email = self.signup_email.get().strip()
#
#         if not name or not age.isdigit() or not self.validate_email(email):
#             messagebox.showerror("Error", "Please enter valid name, age and email.")
#             return
#
#         self.username = name
#         messagebox.showinfo("Success", f"Welcome {name}! Your Player ID is 12345 (for demo)")
#         self.show_main_menu()
#
#     def validate_email(self, email):
#         return re.match(r"[^@]+@[^@]+\.[^@]+", email)
#
#     def show_main_menu(self):
#         self.clear_frame()
#         tk.Label(self.frame, text=f"Welcome, {self.username}!", font=("Helvetica", 18)).pack(pady=10)
#         tk.Label(self.frame, text="Choose a section to begin:", font=("Helvetica", 14)).pack(pady=5)
#
#         tk.Button(self.frame, text="Hiragana", width=20, command=lambda: self.run_file(HIRAGANA_PATH)).pack(pady=5)
#         tk.Button(self.frame, text="Basic Words", width=20, command=lambda: self.run_file(WORDS_PATH)).pack(pady=5)
#         tk.Button(self.frame, text="Quiz", width=20, command=lambda: self.run_file(QUIZ_PATH)).pack(pady=5)
#         tk.Button(self.frame, text="Logout", command=self.show_welcome_screen).pack(pady=10)
#
#     def run_file(self, filepath):
#         if not os.path.exists(filepath):
#             messagebox.showerror("File Not Found", f"Cannot find file:\n{filepath}")
#             return
#         subprocess.Popen(["python3", filepath])
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = IchigoApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
import subprocess
import re
import os

# === Relative File Names (should be in the same folder as this script) ===
HIRAGANA_FILE = "Hiragna.py"
WORDS_FILE = "Basic Words.py"
QUIZ_FILE = "Quiz.py"

class IchigoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ichigo Learning App")
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        self.show_welcome_screen()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_frame()
        tk.Label(self.frame, text="🍓 Welcome to Ichigo Learning App 🍓", font=("Helvetica", 18)).pack(pady=10)
        tk.Button(self.frame, text="Sign In", width=20, command=self.show_signin).pack(pady=5)
        tk.Button(self.frame, text="Sign Up", width=20, command=self.show_signup).pack(pady=5)

    def show_signin(self):
        self.clear_frame()
        tk.Label(self.frame, text="Sign In", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.frame, text="Name").pack()
        self.signin_name = tk.Entry(self.frame)
        self.signin_name.pack()

        tk.Label(self.frame, text="5-digit Player ID").pack()
        self.signin_id = tk.Entry(self.frame)
        self.signin_id.pack()

        tk.Button(self.frame, text="Login", command=self.login_user).pack(pady=10)
        tk.Button(self.frame, text="Back", command=self.show_welcome_screen).pack()

    def login_user(self):
        name = self.signin_name.get().strip()
        pid = self.signin_id.get().strip()

        if not (name and pid.isdigit() and len(pid) == 5):
            messagebox.showerror("Error", "Please enter valid name and 5-digit Player ID.")
            return

        self.username = name
        self.show_main_menu()

    def show_signup(self):
        self.clear_frame()
        tk.Label(self.frame, text="Sign Up", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.frame, text="Name").pack()
        self.signup_name = tk.Entry(self.frame)
        self.signup_name.pack()

        tk.Label(self.frame, text="Age").pack()
        self.signup_age = tk.Entry(self.frame)
        self.signup_age.pack()

        tk.Label(self.frame, text="Email").pack()
        self.signup_email = tk.Entry(self.frame)
        self.signup_email.pack()

        tk.Button(self.frame, text="Register", command=self.register_user).pack(pady=10)
        tk.Button(self.frame, text="Back", command=self.show_welcome_screen).pack()

    def register_user(self):
        name = self.signup_name.get().strip()
        age = self.signup_age.get().strip()
        email = self.signup_email.get().strip()

        if not name or not age.isdigit() or not self.validate_email(email):
            messagebox.showerror("Error", "Please enter valid name, age and email.")
            return

        self.username = name
        messagebox.showinfo("Success", f"Welcome {name}! Your Player ID is 12345 (for demo)")
        self.show_main_menu()

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def show_main_menu(self):
        self.clear_frame()
        tk.Label(self.frame, text=f"Welcome, {self.username}!", font=("Helvetica", 18)).pack(pady=10)
        tk.Label(self.frame, text="Choose a section to begin:", font=("Helvetica", 14)).pack(pady=5)

        tk.Button(self.frame, text="Hiragana", width=20, command=lambda: self.run_file(HIRAGANA_FILE)).pack(pady=5)
        tk.Button(self.frame, text="Basic Words", width=20, command=lambda: self.run_file(WORDS_FILE)).pack(pady=5)
        tk.Button(self.frame, text="Quiz", width=20, command=lambda: self.run_file(QUIZ_FILE)).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.show_welcome_screen).pack(pady=10)

    def run_file(self, filename):
        # Resolve full path
        full_path = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(full_path):
            messagebox.showerror("File Not Found", f"Cannot find file:\n{filename}")
            return
        # Run using system default Python (assumes .py files are GUI apps too)
        subprocess.Popen(["python3", full_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = IchigoApp(root)
    root.mainloop()
