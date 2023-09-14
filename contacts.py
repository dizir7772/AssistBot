from contact import Contact
import pickle
import os


class Contacts:
    """ Клас що опису сутність - сховище контактів """
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._contacts = []
        self.load()

    def load(self):
        """ ВІдновлює стан з файлу"""
        if os.path.exists(self._filename):
            with open(self._filename, 'rb') as file:
                try:
                    obj = pickle.load(file)
                    self.__dict__ = obj.__dict__
                except:
                    pass

    def save(self):
        """ Записує стан у файл """
        with open(self._filename, 'wb') as file:
            pickle.dump(self, file)

    def add(self, contact: Contact):
        """ Додає контакт в сховище """
        self._contacts.append(contact)
        self._contacts = sorted(self._contacts, key=lambda x: x.name, reverse=True)
        self.save()

    def delete(self, contact: Contact):
        """ Видаляє контакт """
        try:
            self._contacts.remove(contact)
            self.save()
        except:
            pass

    @property
    def content(self):
        return self._contacts

    def filter(self, value):
        """ Фільтрує контакти по заданому ключу """
        if value is None:
            return self.content

        filtered = []
        for contact in self._contacts:
            if value in contact:
                filtered.append(contact)

        return filtered
