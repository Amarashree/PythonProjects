# creating a main file, with create UI in Object Oriented programming form\
import tkinter as tk
from tkinter import messagebox

class BasicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Tkinter App")
        self.root.geometry("400x300")
        self.root.configure(bg="#f4f4f4")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self.root, text="Welcome to Tkinter!", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333"
        )
        self.label.pack(pady=20)

        self.text_field = tk.Entry(self.root, font=("Arial", 14), width=25, bg="#007bff", fg="white",)
        self.text_field.pack(pady=10)

        self.submit_button = tk.Button(
            self.root,
            text="Submit",
            font=("Arial", 12),
            bg="#007bff",
            fg="white",
            command=self.submit_action
        )
        self.submit_button.pack(pady=10)

        self.quit_button = tk.Button(
            self.root,
            text="Quit",
            font=("Arial", 12),
            bg="#dc3545",
            fg="white",
            command=self.root.quit
        )
        self.quit_button.pack(pady=10)

    def submit_action(self):
        user_input = self.text_field.get()
        if user_input.strip():
            messagebox.showinfo("Input Received", f"You entered: {user_input}")
        else:
            messagebox.showwarning("No Input", "Please enter something!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicApp(root)
    root.mainloop()