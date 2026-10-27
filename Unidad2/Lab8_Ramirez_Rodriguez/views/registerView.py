import os
import tkinter as tk
from tkinter import messagebox

class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        self.ventana.title("REGISTER USER")
        self.ventana.geometry("1080x720")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.resizable(False, False)

        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(
            self.ventana,
            text="CREATE ACCOUNT",
            font=("Calibri", 20, "bold"),
            bg="#FFFFFF",
            fg="#000000"
        )
        self.titulo.pack(pady=18)

        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Full name:",
            bg="#FFFFFF",
            font=("Calibri", 12)
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=30,
            font=("Calibri", 12)
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Email:",
            bg="#FFFFFF",
            font=("Calibri", 12)
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=30,
            font=("Calibri", 12)
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Password:",
            bg="#FFFFFF",
            font=("Calibri", 12)
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=30,
            show="*",
            font=("Calibri", 12)
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirm password:",
            bg="#FFFFFF",
            font=("Calibri", 12)
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=30,
            show="*",
            font=("Calibri", 12)
        )
        self.entry_confirmar.pack(pady=4)

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Register user",
            width=22,
            bg="#FFFFFF",
            fg="white",
            font=("Calibri", 12, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancel",
            width=25,
            bg="#000000",
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()