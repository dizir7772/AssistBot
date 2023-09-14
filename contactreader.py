from contact import Contact
from valuereader import Value_reader
from validator import Validator
from screen import Screen

""" 
|------------------------------------------|
|             CREATE NEW CONTACT           |
|------------------------------------------|
|                                          |
|                                          |
|                                          |
|                                          |
|        -> Some text in the field         |
|                                          |
|                                          |
|                                          |
|                                          |
|------------------------------------------|
|              INSTRUCTIONS                |
|------------------------------------------|
"""


class Contact_reader:
    """ Клас що отримує в користувача дані контакту та перевіряє їх правильність """
    NAME_PATTERN = r"^[a-zA-Zа-яА-ЯіїєґІЇЄҐ0-9 ,.]{3,24}$"
    ADDRESS_PATTERN = r"(|(^[a-zA-Zа-яА-ЯіїєґІЇЄҐ0-9 ,.\/]{3,24}))$"
    PHONE_PATTERN = r'^(|(\d{3}-\d{3}-\d{2}-\d{2}))$'
    MAIL_PATTERN = r"^(|([\w.-]+@[\w.-]+))$"
    DATE_PATTERN = r"^(|((0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}))$"

    def __init__(self) -> None:
        pass

    def read(self) -> Contact:
        """ Отримує дані, перевіряє та повертає екземпляр """
        name = Value_reader(
            Screen("Введіть ім'я контакту",
                   "Ім'я має бути не менше 3 літер і не більше 24 | Enter - для підтвердження"),
            Validator(Contact_reader.NAME_PATTERN)
        ).read()

        address = Value_reader(
            Screen("Введіть адресу контакту",
                   "Адреса має бути від 3 до 32 літер | Можете залишити рядок пустим | Enter - для підтвердження"),
            Validator(Contact_reader.ADDRESS_PATTERN)
        ).read()

        phones = []
        for i in range(Contact.MAX_PHONES):
            phone = Value_reader(
                Screen(
                    f"Введіть номер телефону №{i+1}", "Номер має бути в форматі [xxx-xxx-xx-xx] | Можете залишити рядок пустим | Enter - для підтвердження"),
                Validator(Contact_reader.PHONE_PATTERN)
            ).read()
            phones.append(phone)

        emails = []
        for i in range(Contact.MAX_EMAILS):
            email = Value_reader(
                Screen(
                    f"Введіть email №{i+1}", "Email має бути в форматі [xxxx@xxxx.xxx] | Можете залишити рядок пустим | Enter - для підтвердження"),
                Validator(Contact_reader.MAIL_PATTERN)
            ).read()
            emails.append(email)

        birthday = Value_reader(
            Screen(f"Введіть дату народження",
                   "Дата має бути в форматі [dd.mm.YYYY] | Можете залишити рядок пустим | Enter - для підтвердження"),
            Validator(Contact_reader.DATE_PATTERN)
        ).read()


        return Contact(name, address, phones, emails, birthday)



