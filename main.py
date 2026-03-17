import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Email and Password Generator")

        # Create tabs
        self.tab_control = tk.Notebook(master)

        self.generator_tab = tk.Frame(self.tab_control)
        self.bulk_tab = tk.Frame(self.tab_control)
        self.validate_tab = tk.Frame(self.tab_control)

        self.tab_control.add(self.generator_tab, text='Generator')
        self.tab_control.add(self.bulk_tab, text='Bulk Generate')
        self.tab_control.add(self.validate_tab, text='Validate')

        self.tab_control.pack(expand=1, fill='both')

        self.create_generator_tab()
        self.create_bulk_tab()
        self.create_validate_tab()

    def create_generator_tab(self):
        tk.Label(self.generator_tab, text="Generate a Random Password:").pack(pady=10)
        self.password_display = tk.Entry(self.generator_tab, width=30)
        self.password_display.pack(pady=5)
        tk.Button(self.generator_tab, text="Generate Password", command=self.generate_password).pack(pady=5)

    def generate_password(self):
        length = 12  # Choose desired password length
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

    def create_bulk_tab(self):
        tk.Label(self.bulk_tab, text='Bulk Generate Passwords:').pack(pady=10)
        self.bulk_display = tk.Text(self.bulk_tab, height=10, width=40)
        self.bulk_display.pack(pady=5)
        tk.Button(self.bulk_tab, text='Bulk Generate', command=self.bulk_generate).pack(pady=5)

    def bulk_generate(self):
        self.bulk_display.delete(1.0, tk.END)
        for _ in range(5):  # Generate 5 passwords as an example
            self.bulk_display.insert(tk.END, self.generate_password_text() + '\n')

    def generate_password_text(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))

    def create_validate_tab(self):
        tk.Label(self.validate_tab, text='Validate Passwords:').pack(pady=10)
        tk.Label(self.validate_tab, text='Enter Password:').pack(pady=5)
        self.validate_entry = tk.Entry(self.validate_tab, width=30)
        self.validate_entry.pack(pady=5)
        tk.Button(self.validate_tab, text='Validate', command=self.validate_password).pack(pady=5)

    def validate_password(self):
        password = self.validate_entry.get()
        if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
            messagebox.showinfo("Validation", "Password is valid!")
        else:
            messagebox.showerror("Validation", "Password must be at least 8 characters long, contain one digit and one uppercase letter.")

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()