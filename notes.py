from note import Note
import os
import pickle


class Notes:
    """ Клас що описує сутність - сховище нотаток """
    def __init__(self, filename: str) -> None:
        self._notes = []
        self._filename = filename
        self.load()
    
    def load(self):
        """ відновлює стан з файлу """
        if os.path.exists(self._filename):
            with open(self._filename, 'rb') as file:
                try:
                    obj = pickle.load(file)
                    self._notes = obj._notes
                except:
                    pass

    def save(self):
        """ Записує стан у файл """
        with open(self._filename, 'wb') as file:
            pickle.dump(self, file)

    def add(self, _note: Note):
        """ Додає нову нотатку у сховище """
        symbols = set((ch for line in _note.content for ch in line))
        if len(symbols) > 0:
            self._notes.insert(0,_note)
            self._notes = sorted(self._notes, key=lambda x: x._last_change, reverse=True)
        self.save()

    def delete(self, _note: Note):
        """ Видаляє нотатку """
        try:
            self._notes.remove(_note)
            self.save()
        except:
            pass

    @property
    def content(self):
        return self._notes

    def filter(self, value):
        """ Проводить фільтрування по заданому ключу """
        if value is None:
            return self.content

        filtered = []
        for note in self._notes:
            for tag in note.tags:
                if value.upper() in tag.upper():
                    filtered.append(note)
        return filtered
