from cleanfolder import CleanFolder
from valuereader import Value_reader
from screen import Screen
from pathlib import Path

""" 
|------------------------------------------|
|           INPUT FOLDER DIRECTORY         |
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



class CleanFolder_reader:
    
    
    def __init__(self) -> None:
        pass
    
    
    def read(self):
        try:
            path = Value_reader(Screen("Введіть шлях до папки, де потрібно навести 'порядок'", "Поле не може бути пустим | Enter - для підтвердження")).read()
            return CleanFolder().sort(Path(path.replace('"', '')))
        except FileNotFoundError:
            pass