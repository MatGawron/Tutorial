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
def __initGrid(self):
    self.grid = [[self.EMPTY for x in range(3)] for x in range(3)]

    def save(self):
        """
    Save the game progress into a file
    :return:
        """
        with open('game_prg.txt', 'a') as f:
            pass


class View(ttk.Frame):
    window = ttk.Tk()
# setting window tittle
    window.title("Kółko i krzyżyk")
# setting default window size
    window.geometry("300x300")

    def __init__(self, grid=np.ones((3, 3)) * np.nan, GUI=None):
        self.grid = grid
        self.GUI = GUI

    def __init(self, parent):
        super().__init__(parent)

    window.mainloop()