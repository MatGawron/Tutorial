
#import re
import tkinter as ttk
from tkinter import *
#import tkinter.messagebox


class Model:
    click = True
    count = 0
    Empty = 0
    Gracz_1 = 1
    Gracz_2 = 2

    def __init__(self, plansza):
        self.plansza = plansza

    @property
# pusta plansza do gry
    def grid(self):
        return self.grid

    @grid.setter
    def grid(self, value):
        self.grid.set_name = [[self.Empty for x in range(3)] for x in range(3)]

    def save(self):
        """
    Save the game progress into a file
    :return:
        """
        filepath = "game_prg.txt"
        f = open(filepath, "w")
        f.write("Dane")
        f.close()
        pass


class View(ttk.Frame):
    root = ttk.Tk()
    # setting window tittle
    root.title("Kółko i krzyżyk")
    # setting default window size
    root.minsize(300, 300)
    root.maxsize(300, 300)
    root.configure(bg="light yellow")

    def display_checked(self, blue_var=None, red_var=None, yellow_var=None, green_var=None):
        '''check if the checkbuttons have been toggled, and display
        a value of '1' if they are checked, '0' if not checked'''
        red = red_var.get()
        yellow = yellow_var.get()
        green = green_var.get()
        blue = blue_var.get()

        print("red: {}\nyellow:{}\ngreen: {}\nblue: {}".format(
            red, yellow, green, blue))

    # Create label
    label = Label(root, text="gracz1: x                                                                     gracz2:o ")
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









