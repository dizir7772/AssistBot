from validator import Validator
from screen import Screen
from console import *

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)


""" 
|------------------------------------------|
|              ENTER SOMETHING             |
|------------------------------------------|
|                                          |
|                                          |
|                                          |
|                                          |
|                                          |
|  -> Entered text....                     |
|                                          |
|                                          |
|                                          |
|                                          |
|                                          |
|------------------------------------------|
|                  STATUS                  |
|------------------------------------------|
"""


class Value_reader:
    """ Отримує дані від користувача та перевіряє їх з допомогою вказаного валідатора """
    def __init__(self, _screen: Screen, _validator: Validator = None) -> None:
        self._screen = _screen
        self._validator = _validator

    def read(self):
        """ Читає та повертає дані від коритсувача """
        success = False
        show_cursor()
        while not success:
            self._screen.draw()
            row_start = gap(self._screen.h, 1)
            col_start = gap(self._screen.w, 64)
            move_cursor(row_start, col_start)
            print(Fore.YELLOW+'->', end='')
            value = input()

            if (self._validator is None and len(value)>0):
                break
            if(self._validator is not None and self._validator(value)):
                break
        hide_cursor()
        return value if len(value)>0 else None
