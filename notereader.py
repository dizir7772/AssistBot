from note import Note
from screen import Screen
from console import *

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

""" 
|------------------------------------------|
|             CREATE  NEW NOTE             |
|------------------------------------------|
|                                          |
|  -> Some text....                        |
|  -> Some text.....                       |
|  -> Some text....                        |
|  -> Some text.....                       |
|  -> Some text....                        |
|  -> Some text.....                       |
|  -> Some text....                        |
|  -> Some text.....                       |
|                                          |
|------------------------------------------|
|              INSTRUCTIONS                |
|------------------------------------------|
"""


class Note_reader:
    """ Отримує від користувача дані для нотатки та повертає екземпляр """
    def __init__(self, screen: Screen) -> None:
        self._screen = screen

    def read(self) -> Note:
        """ Читає та повертає інформацію від користувача """
        self._screen.draw()
        col_start = gap(self._screen.w, Note.MAX_COLUMNS)
        row_start = gap(self._screen.h, Note.MAX_ROWS)

        for i in range(Note.MAX_ROWS):
            move_cursor(row_start+i, col_start)
            print(Fore.YELLOW+'|'+'.'*(Note.MAX_COLUMNS-2)+'|', end='')

        lines = []
        show_cursor()
        for i in range(Note.MAX_ROWS):
            move_cursor(row_start+i, col_start+1)
            line = input()[:Note.MAX_COLUMNS].replace('\t','')
            lines.append(line)
        hide_cursor()
        return Note(lines)
