
#import re
import tkinter as ttk
from tkinter import *


class Model:
    click = True
    count = 0
    Empty = 0
    Gracz_1 = 1
    Gracz_2 = 2

    def __init__(self, plansza):
        self.plansza = plansza

class View(ttk.Frame):
    root = ttk.Tk()
    # setting window tittle
    root.title("Kółko i krzyżyk")
    # setting default window size
    root.minsize(300, 300)
    root.maxsize(300, 300)
    root.configure(bg="light yellow")

    def display_checked(self):
        pass

# Create label
    label = Label(root, text="gracz1: X                                                                    gracz2: O")
    label.grid(row=0)

# Create Buttons
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=1, column=1)
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=1, column=2)
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=1, column=3)

    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=2, column=1)
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=2, column=2)
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=2, column=3)

    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=3, column=1)
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=3, column=2)
    Button(root, text=" ", width=10, height=4, command=display_checked).grid(row=3, column=3)

    root.mainloop()









