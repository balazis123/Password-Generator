import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Password display
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            main_frame,
            textvariable=self.password_var,
            font=("Arial", 12),
            justify="center"
        )
        self.password_entry.pack(fill=tk.X, pady=(0, 20))
        self.password_entry.insert(0, "Generated Password")
        self.password_entry.configure(foreground="gray")
        
        # Copy button
        copy_btn = ttk.Button(
            main_frame,
            text="Copy",
            command=self.copy_password
        )
        copy_btn.pack(pady=(0, 20))
        
        # Length slider
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
        self.length_var = tk.IntVar(value=12)
        length_slider = tk.Scale(
            length_frame,
            from_=6,
            to=32,
            orient=tk.HORIZONTAL,
            variable=self.length_var,
            length=200,
            digits=0,
            showvalue=True
        )
        length_slider.pack(side=tk.LEFT, padx=(10, 0))
        ttk.Label(length_frame, textvariable=self.length_var).pack(side=tk.LEFT, padx=(10, 0))
        
        # Checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(
            main_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.uppercase_var
        ).pack(anchor=tk.W, pady=5)
        
        ttk.Checkbutton(
            main_frame,
            text="Lowercase Letters (a-z)",
            variable=self.lowercase_var
        ).pack(anchor=tk.W, pady=5)
        
        ttk.Checkbutton(
            main_frame,
            text="Numbers (0-9)",
            variable=self.numbers_var
        ).pack(anchor=tk.W, pady=5)
        
        ttk.Checkbutton(
            main_frame,
            text="Symbols (!@#$%^&*)",
            variable=self.symbols_var
        ).pack(anchor=tk.W, pady=5)
        
        # Generate button
        generate_btn = ttk.Button(
            main_frame,
            text="GENERATE",
            command=self.generate_password
        )
        generate_btn.pack(pady=20)
        
        # Bind events
        self.password_entry.bind("<FocusIn>", self.on_entry_click)
        self.password_entry.bind("<FocusOut>", self.on_focus_out)
    
    def on_entry_click(self, event):
        if self.password_entry.get() == "Generated password":
            self.password_entry.delete(0, tk.END)
            self.password_entry.configure(foreground="black")
    
    def on_focus_out(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, "Generated password")
            self.password_entry.configure(foreground="gray")
    
    def generate_password(self):
        # Get selected options
        length = self.length_var.get()
        use_uppercase = self.uppercase_var.get()
        use_lowercase = self.lowercase_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()
        
        # Create character pool based on selected options
        chars = ""
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_numbers:
            chars += string.digits
        if use_symbols:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not chars:
            self.password_var.set("Select at least one option")
            return
        
        # Generate password
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Update display
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.configure(foreground="black")
    
    def copy_password(self):
        password = self.password_var.get()
        if password and password != "Generated password":
            pyperclip.copy(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop() 