from console import *
import readchar as rc
from messagebox import Messagebox
from screen import Screen
from contact import Contact
from contacts import Contacts
from contactreader import Contact_reader
from validator import Validator
from valuereader import Value_reader

""" 
|------------------------------------------|
|              CONTACT INFO                |
|------------------------------------------|
|                                          |
|                                          |
|                                          |
|          Field : information             |
|          Field : information             |
|          Field : information             |
|          Field : information             |
|          Field : information             |
|          Field : information             |
|                                          |
|                                          |
|                                          |
|                                          |
|------------------------------------------|
| NEXT/PREV | DEL - DELETE | ENTER - EDIT  |
|------------------------------------------|
"""


class Contacts_manager:
    """ Клас що описує сутність - менеджер контактів  """
    def __init__(self, constacts: Contacts, key_word: str | None) -> None:
        self._contacts = constacts
        self._key_word = key_word
        self._screen = Screen(
            'Перегляд контактів', 'Вліво/Вправо - вибір | ENTER - редагувати | DEL - видалити | ESC - назад')

    def interactive(self):
        """ Інтеракивний режим взаємодії з корстувачем """
        filtered_contacts = self._contacts.filter(self._key_word)
        qty = len(filtered_contacts)
        current = 0
        while True:
            self._screen.draw()
            if qty == 0:
                self._screen.title = 'Перегляд контактів'
                Messagebox(
                    self._screen, "Контакти не знайдені...\nДодайте нові або змініть параметри пошуку").draw()
            else:
                if self._key_word:
                    self._screen.title = f'Ключове слово : {self._key_word} | Контакт : {current+1}/{qty} | Доданий : {filtered_contacts[current].create_date}'
                else:
                    self._screen.title = f'Контакт : {current+1}/{qty} додано {filtered_contacts[current].create_date}'

                Messagebox(
                    self._screen, str(filtered_contacts[current])).draw()

            # обробка клавіш
            key = rc.readkey()
            if key == rc.key.ESC:
                break

            elif key == rc.key.DELETE and qty:
                self._contacts.delete(filtered_contacts[current])
                filtered_contacts = self._contacts.filter(self._key_word)
                qty = len(filtered_contacts)
                current = current % qty if qty else 0

            elif key == rc.key.LEFT and qty:
                current = (current - 1) % qty

            elif key == rc.key.RIGHT and qty:
                current = (current + 1) % qty

            elif key == rc.key.ENTER and qty:
                current_contact = filtered_contacts[current]
                
                # редагуємо ім'я 
                scr = Screen(
                    f'Редагування поля "Ім`я", старе значення : {current_contact.name}', 'Щоб не змінювати - залиште поле пустим')
                name = Value_reader(scr, Validator(
                    r"^(|([a-zA-Zа-яА-ЯіїєґІЇЄҐ0-9 ,.]{3,24}))$")).read()
                current_contact.name = name if name else current_contact.name

                # редагуємо адресу
                old_value = current_contact.address if current_contact.address else '-'
                scr = Screen(
                    f'Редагування поля "Адреса", старе значення : {old_value}', 'Щоб не змінювати - залиште поле пустим')
                address = Value_reader(
                    scr, Validator(Contact_reader.ADDRESS_PATTERN)).read()
                current_contact.address = address if address else current_contact.address

                # редагуємо список телефонів
                for i in range(Contact.MAX_PHONES):
                    old_value = '-' if current_contact.phones[i] is None else current_contact.phones[i]
                    scr = Screen(
                        f'Редагування поля "Телефон №{i+1}", старе значення : {old_value}', 'Щоб не змінювати - залиште поле пустим')
                    phone = Value_reader(
                        scr, Validator(Contact_reader.PHONE_PATTERN)).read()
                    current_contact.phones[i] = phone if phone else current_contact.phones[i]

                # Редагуємо список імейлів
                for i in range(Contact.MAX_EMAILS):
                    old_value = '-' if current_contact.email[i] is None else current_contact.email[i]
                    scr = Screen(
                        f'Редагування поля "Email №{i+1}", старе значення : {old_value}', 'Щоб не змінювати - залиште поле пустим')
                    email = Value_reader(
                        scr, Validator(Contact_reader.MAIL_PATTERN)).read()
                    current_contact.email[i] = email if email else current_contact.email[i]
                
                # редагуємо дату народження
                old_value = '-' if current_contact.birthday is None else current_contact.birthday
                scr = Screen(
                    f'Редагування поля "День народження", старе значення : {old_value}', 'Щоб не змінювати - залиште поле пустим')
                birthday = Value_reader(
                    scr, Validator(Contact_reader.DATE_PATTERN)).read()
                current_contact.birthday = birthday if birthday else current_contact.birthday

                # зберігаємо зміни
                self._contacts.save()