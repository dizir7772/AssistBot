import re


class Validator:
    """ Перевіряє по заданому регулярному виразу даний рядок """
    def __init__(self, pattern) -> None:
        self._patern = pattern

    def __call__(self, _value) -> bool:
        if re.match(self._patern, _value):
            return True
        else:
            return False
