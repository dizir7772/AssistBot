import datetime


class Note:
    """ Клас що описує сунтість - нотатка """
    MAX_COLUMNS = 64
    MAX_ROWS = 8
    DT_FORMAT = "%d.%m.%Y, %H:%M:%S"

    def __init__(self, content) -> None:
        self._tags = []
        self.content = content

    def __str__(self):
        value = ''
        for line in self.content:
            value += line + '\n'
        return value


    @property
    def last_change(self):
        return datetime.datetime.strftime(self._last_change, Note.DT_FORMAT)

    @property
    def tags(self):
        return self._tags

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, _value):
        self._content = _value
        self._last_change = datetime.datetime.now()

        self._tags = []
        for line in _value:
            for word in line.split(' '):
                if word.startswith('#') and len(word) > 0:
                    self._tags.append(word.strip('#'))

