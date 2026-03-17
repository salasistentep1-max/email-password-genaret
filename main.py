import tkinter as tk
from tkinter import messagebox, ttk
import re
import time
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Email & Password Generator")
        self.master.geometry('400x400')
        self.create_tabs()

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self.master)
        self.generator_tab = ttk.Frame(self.tab_control)
        self.bulk_tab = ttk.Frame(self.tab_control)
        self.validate_tab = ttk.Frame(self.tab_control)
        self.settings_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.generator_tab, text='Generator')
        self.tab_control.add(self.bulk_tab, text='Bulk Generate')
        self.tab_control.add(self.validate_tab, text='Validate')
        self.tab_control.add(self.settings_tab, text='Settings')
        self.tab_control.pack(expand=1, fill='both')

        self.create_generator_tab()
        self.create_bulk_tab()
        self.create_validate_tab()
        self.create_settings_tab()

    def create_generator_tab(self):
        ttk.Label(self.generator_tab, text="Password Length:").pack(pady=5)
        self.length_entry = ttk.Entry(self.generator_tab)
        self.length_entry.pack(pady=5)

        self.show_password = tk.BooleanVar()
        self.show_password_check = ttk.Checkbutton(self.generator_tab, text='Show Password', variable=self.show_password)
        self.show_password_check.pack(pady=5)

        self.generated_password = ttk.Entry(self.generator_tab, width=50)
        self.generated_password.pack(pady=5)

        ttk.Button(self.generator_tab, text='Generate', command=self.generate_password).pack(pady=5)
        ttk.Button(self.generator_tab, text='Copy', command=self.copy_password).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 6:
                raise ValueError("Password length must be at least 6.")
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            if self.show_password.get():
                self.generated_password.config(show='')
            else:
                self.generated_password.config(show='*')
            self.generated_password.delete(0, tk.END)
            self.generated_password.insert(0, password)
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def copy_password(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password.get())
        messagebox.showinfo('Info', 'Password copied to clipboard!')

    def create_bulk_tab(self):
        ttk.Label(self.bulk_tab, text="Number of Passwords:").pack(pady=5)
        self.bulk_count_entry = ttk.Entry(self.bulk_tab)
        self.bulk_count_entry.pack(pady=5)

        ttk.Button(self.bulk_tab, text='Bulk Generate', command=self.bulk_generate).pack(pady=5)

        self.bulk_output = tk.Text(self.bulk_tab, width=50, height=10)
        self.bulk_output.pack(pady=5)

    def bulk_generate(self):
        try:
            count = int(self.bulk_count_entry.get())
            if count < 1:
                raise ValueError("Must generate at least 1 password.")
            self.bulk_output.delete(1.0, tk.END)
            for _ in range(count):
                password = self.generate_random_password(12)
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
                self.bulk_output.insert(tk.END, f'{timestamp}: {password}\n')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def create_validate_tab(self):
        ttk.Label(self.validate_tab, text="Email:").pack(pady=5)
        self.email_entry = ttk.Entry(self.validate_tab)
        self.email_entry.pack(pady=5)

        ttk.Button(self.validate_tab, text='Validate', command=self.validate_email).pack(pady=5)
        self.result_label = ttk.Label(self.validate_tab, text='')
        self.result_label.pack(pady=5)

    def validate_email(self):
        email = self.email_entry.get()
        if self.is_valid_email(email):
            self.result_label.config(text='Valid Email', foreground='green')
        else:
            self.result_label.config(text='Invalid Email', foreground='red')

    def is_valid_email(self, email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

    def create_settings_tab(self):
        ttk.Label(self.settings_tab, text="Settings Placeholder").pack(pady=5)
        # Add more settings functionality here

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()