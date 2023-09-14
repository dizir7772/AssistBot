from console import *
import readchar as rc
import colorama
import screen

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

""" 
|------------------------------------------|
|                 MENU NAME                |
|------------------------------------------|
|                                          |
|                                          |
|                  MENU ITEM               |
|                  MENU ITEM               |
|                  MENU ITEM               |
|                  MENU ITEM               |
|                  MENU ITEM               |
|                                          |
|                                          |
|------------------------------------------|
|                  STATUS                  |
|------------------------------------------|
"""


class Menu:
    """ Клас що описує сутність - меню """
    BREAK = -1
    NONE = -2

    def __init__(self, screen: screen.Screen,  menu_items: list[str]) -> None:
        self._items = menu_items
        self._curr_active = 0
        self._screen = screen

    def draw(self):
        """ Виводить на консоль стан меню """
        self._screen.draw()
        con_h, con_w = get_console_size()
        start_row = gap(con_h, len(self._items))
        for index, item in enumerate(self._items):
            move_cursor(start_row+index, gap(con_w, len(item)))
            if index != self._curr_active:
                print(f'{Fore.YELLOW}{item}')
            else:
                print(f'{Fore.BLACK}{Back.YELLOW}{item}')

    def start(self):
        """ Взяємодіє з користувачем та повертаї індекс вибраного пункту меню """
        while True:
            self.draw()
            key = rc.readkey()

            if key == rc.key.ESC:
                return Menu.BREAK
            elif key == rc.key.UP:
                self._curr_active = (self._curr_active - 1) % len(self._items)
            elif key == rc.key.DOWN:
                self._curr_active = (self._curr_active + 1) % len(self._items)
            elif key == rc.key.ENTER:
                return self._curr_active
