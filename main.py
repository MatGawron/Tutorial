import re
import tkinter as tk
from tkinter import ttk

class Model:

    Empty = 0
    Gracz_1 = 1
    Gracz_2 = 2

    def __init__(self, Plansza):
        self.Plansza = Plansza

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
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')
##




