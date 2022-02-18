
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

global board
board = [[" " for x in range(3)] for y in range(3)]

class View(ttk.Frame):
    root = ttk.Tk()
    # setting window tittle
    root.title("Kółko i krzyżyk")
    # setting default window size
    root.geometry("318x348")
    root.configure(bg="light yellow")

    def display_checked(self):
        pass

# Create label
    label = Label(root, text="gracz1: X gracz2: O")
    label.grid(row=0)

# Create Buttons
    b1 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b1, 0, 0))
    b2 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b2, 0, 1))
    b3 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b3, 0, 2))
    b4 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b4, 1, 0))
    b5 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b5, 1, 1))
    b6 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b6, 1, 2))
    b7 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b7, 2, 0))
    b8 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b8, 2, 1))
    b9 = Button(root, text="", height=4, width=8, bg="black", activebackground="white", fg="white", font="Times 15 bold",
                command=lambda: changeVal(b9, 2, 2))
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)
    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=4, column=2)

    root.mainloop()









