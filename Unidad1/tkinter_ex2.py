import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application TKINTER TEST")
root.geometry("480x960")
root.minsize(480, 120)

ttk.Label(root, text="TEST TEXT").pack(padx=20, pady=20)

root.mainloop()