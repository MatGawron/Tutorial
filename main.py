import re
from tkinter import ttk


class Model:

    Empty = 0
    Gracz_1 = 1
    Gracz_2 = 2

    def __init__(self, plansza):
        self.plansza = plansza

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """   dffd
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

        def save(self):
            """
        Save the game progress into a file
        :return:
        """
            with open('game_prg.txt', 'a') as f:
                f.write(self.game_prg + '\n')


class View(ttk.Frame):
    def __init(self, parent):
        super().__init__(parent)
