import os
import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("1080x720")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)

        self.titulo = tk.Label(
            root,
            text="LOGIN",
            font=("Calibri", 24, "bold"),
            bg="#FFFFFF",
            fg="#000000"
        )
        self.titulo.pack(pady=20)

        self.lbl_email = tk.Label(
            root,
            text="Email:",
            font=("Calibri", 12),
            bg="#FFFFFF"
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            root,
            width=35,
            font=("Calibri", 12)
        )
        self.entry_email.pack(pady=5)

        self.lbl_password = tk.Label(
            root,
            text="Password:",
            font=("Calibri", 12),
            bg="#FFFFFF"
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            root,
            width=35,
            font=("Calibri", 12),
            show="*"
        )
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(
            root,
            text="Enter",
            width=20,
            bg="#000000",
            fg="white",
            font=("Calibri", 12, "bold"),
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        self.btn_register = tk.Button(
            root,
            text="Create account",
            width=20,
            bg="#000000",
            fg="white",
            font=("Calibri", 11),
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)