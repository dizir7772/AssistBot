from console import *
import readchar as rc
from messagebox import Messagebox
from screen import Screen
from notes import Notes

# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)

""" 
|------------------------------------------|
|                   NOTE INFO              |
|------------------------------------------|
|                                          |
|                                          |
|                                          |
|                                          |
|               Some note text....         |
|               Some note text....         |
|               Some note text....         |
|               Some note text....         |
|                                          |
|                                          |
|                                          |
|                                          |
|------------------------------------------|
|     NEXT/PREV |  DELETE | .....          |
|------------------------------------------|
"""


class Notes_manager:
    """ Клас менеджер нотаток """
    def __init__(self, notes: Notes, tag_word: str) -> None:
        self._notes = notes
        self._screen = Screen(
            'Перегляд нотаток', 'Вліво/Вправо - вибір | DEL - видалити | ESC - назад')
        self._tag_word = tag_word

    def interactive(self):
        """ Інтерактивна взаємодія з користувачем """
        filtered_notes = self._notes.filter(self._tag_word)
        qty = len(filtered_notes)
        current = 0
        while True:
            self._screen.draw()
            if qty == 0:
                self._screen.title = 'Перегляд нотаток'
                Messagebox(
                    self._screen, "Нотатки не знайдені...\nДодайте нові або змініть параметри пошуку").draw()
            else:
                if self._tag_word:
                    self._screen.title = f'Ключове слово : {self._tag_word} | Нотатка : {current+1}/{qty} від {filtered_notes[current].last_change}'
                else:
                    self._screen.title = f'Нотатка : {current+1}/{qty} від : {filtered_notes[current].last_change}'

                Messagebox(self._screen, str(filtered_notes[current])).draw()

            key = rc.readkey()

            if key == rc.key.ESC:
                break
            elif key == rc.key.DELETE:
                if qty:
                    self._notes.delete(filtered_notes[current])
                    filtered_notes = self._notes.filter(self._tag_word)
                    qty = len(filtered_notes)
                    current = current % qty if qty else 0
            elif key == rc.key.LEFT:
                if qty:
                    current = (current - 1) % qty
            elif key == rc.key.RIGHT:
                if qty:
                    current = (current + 1) % qty
