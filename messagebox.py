from console import *
import colorama
from screen import Screen

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

""" 
|------------------------------------------|
|                  SOME TEXT               |
|------------------------------------------|
|                                          |
|                                          |
|                                          |
|                                          |
|               Some text....              |
|               Some text....              |
|                                          |
|                                          |
|                                          |
|                                          |
|------------------------------------------|
|                  STATUS                  |
|------------------------------------------|
"""




class Messagebox:
    """ Просто виводить текст на екран """
    def __init__(self, screen: Screen, msg: str) -> None:
        self._screen = screen
        self._msg = msg

    def draw(self):
        self._screen.draw()
        strings = self._msg.split('\n')
        max_str_len = max((len(s) for s in strings))
        str_qty = len(strings)

        row_start = gap(self._screen.h, str_qty)
        col_start = gap(self._screen.w, max_str_len)

        for i in range(str_qty):
            move_cursor(row_start+i, col_start)
            print(Fore.YELLOW+strings[i], end='')
