import numpy as np
import re
import tkinter as ttk


class Model:

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
        with open('game_prg.txt', 'a') as f:
            pass


class View(ttk.Frame):
    root = ttk.Tk()
# setting window tittle
    root.title("Kółko i krzyżyk")
# setting default window size
    root.minsize(300, 300)
    root.maxsize(300, 300)
    root.configure(bg="light yellow")

    def __init__grid(self, grid=np.ones((3, 3)) * np.nan, gui=None):
        self.grid = grid
        self.gui = gui

    def __init(self, parent):
        super().__init__(parent)

    root.mainloop()