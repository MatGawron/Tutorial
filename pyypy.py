import re
import tkinter as tk

#
class Model:

    EMPTY = 0
    Gracz_1 = 1
    Gracz_2 = 2

    def __init__(self):

        super(Model, self).__init__()
        self.grid = None
        self.turn = self.Gracz_1
        self.__initGrid()
        pass

# pusta plansza do gry
    def __initGrid(self):
        self.grid = [[self.EMPTY for x in range(3)] for x in range(3)]
        pass

    def __intNowaGra(self, NowaGra):
        self.NowaGra =self.grid