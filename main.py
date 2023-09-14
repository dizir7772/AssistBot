from menu import Menu
from console import *
from screen import Screen
from notes import Notes
from contacts import Contacts
from notereader import Note_reader
from contactreader import Contact_reader
from notesmanager import Notes_manager
from contactsmanager import Contacts_manager
from valuereader import Value_reader
from cleanfolderreader import CleanFolder_reader
from cleanfolder import CleanFolder

# шляхи до файлів
NOTES_FILE = 'notes.bin'
CONTACS_FILE = 'contacts.bin'

# Пункти головного меню
MAIN_MENU = [
    'Контакти',
    'Нотатки',
    'Сортувальник',
    'Вихід'
]

CONTACS_SUB = 0
NOTES_SUB = 1
CLEANFOLDER_SUB = 2
MAIN_MENU_BREAK = 3


# Підпункти
CONTAСTS_MENU = [
    'Додати контакт',
    'Переглянути контакти',
    'Знайти контакт',
    'Назад'
]
CONTACTS_ADD = 0
CONTACTS_SHOW_ALL = 1
CONTACTS_SEARCH = 2
CONTACTS_BREAK = 3

# Підпункти
NOTES_MENU = [
    'Додати нотатки',
    'Переглянути нотатки',
    'Пошук нотатків',
    'Назад'
]
NOTES_ADD = 0
NOTES_SHOW_ALL = 1
NOTES_SEARCH = 2
NOTES_BREAK = 3


# Підпункти
CLEANFOLDER_MENU = [
    'Вказати шлях до папки',
    'Назад'
]
CLEANFOLDER_ADD = 0
CLEANFOLDER_BREAK = 1



hide_cursor()

# екземпляри класів меню
main_menu = Menu(
    Screen('Персональний помічник', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), MAIN_MENU)
contacts_menu = Menu(Screen(
    'Книга контактів', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), CONTAСTS_MENU)
notes_menu = Menu(
    Screen('Нотатки', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), NOTES_MENU)
cleanfolder_menu = Menu(Screen(
    'Сортувальник файлів', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), CLEANFOLDER_MENU)



# екземпляри класів сховища нотаток та контактів
my_notes = Notes(NOTES_FILE)
my_contacts = Contacts(CONTACS_FILE)

# Цикл взаємодії з користувачем
choice = Menu.NONE
while choice != Menu.BREAK:
    choice_contacts = Menu.NONE
    choice_notes = Menu.NONE
    choice_cleanfolder = Menu.NONE

    choice = main_menu.start()
    
    # вибране підменю контакти 
    if choice == CONTACS_SUB:
        while choice_contacts != Menu.BREAK:
            choice_contacts = contacts_menu.start()
            # додати
            if choice_contacts == CONTACTS_ADD:
                # додаємо новий контакт
                contact = Contact_reader().read()
                my_contacts.add(contact)
            # пошук
            elif choice_contacts == CONTACTS_SEARCH:
                key_word = Value_reader(Screen(
                    "Введіть ключове слово для пошуку", "Слово не може бути пустим | Enter - для підтвердження"), None).read()
                Contacts_manager(my_contacts, key_word).interactive()
            # показати всі
            elif choice_contacts == CONTACTS_SHOW_ALL:
                Contacts_manager(my_contacts, None).interactive()
            # назад
            elif choice_contacts == CONTACTS_BREAK:
                break

    # вибране підменю нотатки
    elif choice == NOTES_SUB:
        while choice_notes != Menu.BREAK:
            choice_notes = notes_menu.start()
            # підменю додати
            if choice_notes == NOTES_ADD:
                # створюємо нову нотатку
                note = Note_reader(Screen("Введіть текст нової нотатки",
                                   "Enter - новий рядок. Рядки можете залишати пустими. Допустимий розмір нотатки 8 рядків по 64 букви")).read()
                my_notes.add(note)
            # показати всі
            elif choice_notes == NOTES_SHOW_ALL:
                # менеджер нотаток
                Notes_manager(my_notes, None).interactive()
            # пошук
            elif choice_notes == NOTES_SEARCH:
                tag_word = Value_reader(Screen(
                    "Введіть ключове слово для пошуку", "Слово не може бути пустим | Enter - для підтвердження"), None).read()
                Notes_manager(my_notes, tag_word).interactive()
            # назад
            elif choice_notes == NOTES_BREAK:
                break
            
    # вибране підменю сортувальник        
    elif choice == CLEANFOLDER_SUB:
        while choice_cleanfolder != Menu.BREAK:
            choice_cleanfolder = cleanfolder_menu.start()
            # підменю додати шлях до папки
            if choice_cleanfolder == CLEANFOLDER_ADD:
                CleanFolder_reader().read()
                CleanFolder().interactive()
            # назад
            elif choice_cleanfolder == CLEANFOLDER_BREAK:
                break
        
    elif choice == MAIN_MENU_BREAK:
        break

clear_console()
show_cursor()
