import re
import tkinter as tk

class Model:
    Empty = 0
    Gracz1 = 1
    Gracz2 = 2

    def __init__(self):
        super(Model, self).__init__()
        self.grid = None
        self.turn = self.PLAYER1




        self.__initGrid()
        pass







    def __initGrid(self):
        self.grid = [[self.EMPTY for x in range(3)] for x in range(3)]
        pass