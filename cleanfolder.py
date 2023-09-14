from pathlib import Path
from messagebox import Messagebox
from screen import Screen
import readchar as rc

class CleanFolder:
    """ Клас що отримує в користувача шлях до папки та сортує в ньому файли """
    IMAGE = []
    VIDEO = []
    DOCUMENT = []
    AUDIO = []
    ARCHIVE = []
    MY_OTHER = []


    REGISTER_EXTENSIONS = {
        "JPEG": IMAGE, "JPG": IMAGE, "SVG": IMAGE, "PNG": IMAGE,
        "AVI" : VIDEO, "MP4":VIDEO, "MOV" : VIDEO, "MKV": VIDEO,
        "DOC": DOCUMENT, "DOCX": DOCUMENT, "TXT": DOCUMENT, "PDF": DOCUMENT, "XLSX": DOCUMENT, "PPTX": DOCUMENT,
        "MP3": AUDIO, "OGG": AUDIO, "WAV": AUDIO, "AMR": AUDIO,
        "ZIP": ARCHIVE, "GZ": ARCHIVE, "TAR": ARCHIVE, "RAR": ARCHIVE,
    }

    FOLDERS = []
    EXTENSIONS = set()
    UNKNOWN = set()
    
    def __init__(self) -> None:
        pass
    
    def get_extension(self, filename: str) -> str:
        return Path(filename).suffix[1:].upper()


    def scan(self, folder: Path) -> None:
        for item in folder.iterdir():
            if item.is_dir():
                if item.name not in ("Archives", "Video", "Audio", "Documents", "Images", "MY_OTHER"):
                    self.FOLDERS.append(item)
                    self.scan(item)               
                continue
            ext = self.get_extension(item.name)
            fullname = folder / item.name
            if not ext:
                self.MY_OTHER.append(fullname)
            else:
                try:
                    container = self.REGISTER_EXTENSIONS[ext]
                    self.EXTENSIONS.add(ext)
                    container.append(fullname)
                except KeyError:
                    self.UNKNOWN.add(ext)
                    self.MY_OTHER.append(fullname)
    
    
    def handle_media(self, filename: Path, target_folder: Path):
        target_folder.mkdir(exist_ok=True, parents=True)
        filename.replace(target_folder / filename.name)


    def handle_other(self, filename: Path, target_folder: Path):
        target_folder.mkdir(exist_ok=True, parents=True)
        filename.replace(target_folder / filename.name)


    def handle_folder(self, folder: Path):
        try:
            folder.rmdir()
        except OSError:
            pass


    def sort(self, folder: Path):
        self.scan(folder)
        for file in self.IMAGE:
            self.handle_media(file, folder / "Image")
        for file in self.VIDEO:
            self.handle_media(file, folder / "Video")
        for file in self.DOCUMENT:
            self.handle_media(file, folder / "Documents")
        for file in self.AUDIO:
            self.handle_media(file, folder / "Audio")

        for file in self.MY_OTHER:
            self.handle_other(file, folder / "Other")
        for file in self.ARCHIVE:
            self.handle_media(file, folder / "Archives")
        for folder in self.FOLDERS[::-1]:
            self.handle_folder(folder)
    
    def interactive(self):
        self._screen = Screen(
            'Успіх', 'ESC - назад')     
        while True:
            self._screen.draw()       
                # self._screen.title = 'Перегляд нотаток'
                #     Messagebox(
                #         self._screen, "Нотатки не знайдені...\nДодайте нові або змініть параметри пошуку").draw()
            Messagebox(self._screen, "Всі файли успішно відсортовано, можете повернутися до основного меню.").draw()
            key = rc.readkey()
            if key == rc.key.ESC:
                break