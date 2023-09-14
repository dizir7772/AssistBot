import datetime


class Contact:
    """ Клас що описує сутність - контакт """
    DT_FORMAT = "%d.%m.%Y"
    MAX_PHONES = 3
    MAX_EMAILS = 3

    def __init__(self, name: str, address: str | None, phones: list[str | None], email: [str | None], birthday: str | None) -> None:
        self.name = name
        self.address = address
        self.phones = phones
        self.email = email
        self.birthday = birthday
        self.creation_date = datetime.datetime.now()

    def __contains__(self, value: str):
        """ Перевантаження оператору in """
        value = value.upper()

        if value in self.name.upper():
            return True
        if self.address and value in self.address.upper():
            return True
        for phone in self.phones:
            if phone and value in phone.upper():
                return True
        for email in self.email:
            if email and value in email.upper():
                return True
        if self.birthday and value in self.birthday:
            return True

        return False

    def __str__(self):
        """ Рядкове представлення """
        string = f'Ім`я : {self.name}\n'
        string += f'Адреса : {self.address if self.address else "-"}\n'
        for i, phone in enumerate(self.phones):
            string += f'Телефон №{i+1} : {phone if phone else "-"}\n'
        for i, mail in enumerate(self.email):
            string += f'Email №{i+1} : {mail if mail else "-"}\n'
        string += f'День народження : {self.birthday if self.birthday else "-"}\n'
        return string

    @property
    def create_date(self):
        return datetime.datetime.strftime(self.creation_date, Contact.DT_FORMAT)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str | None):
        self._address = value

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, value: list[str | None]):
        self._phones = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: list[str | None]):
        self._email = value

    @property
    def birthday(self):
        if self._birthday is None:
            return None
        else:
            return datetime.datetime.strftime(self._birthday, Contact.DT_FORMAT)

    @birthday.setter
    def birthday(self, value: str | None):
        if value is None:
            self._birthday = None
        else:
            self._birthday = datetime.datetime.strptime(
                value, Contact.DT_FORMAT)

