from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("300x600")
root.resizable(0, 0)
title = Callu-Calc
root.title(title)

user_input = Entry(root, textvariable=input_t, font=('arial', 18, 'bold'), width=50, bd=0)
user_input.pack(side="top", ipady=15, fill="both", expand=True)
user_input.focus()
input_t.set("Enter input in the format: x(operation)y")
user_input.icursor(len(input_t.get()))

