"""
Создай класс Album у которого есть поля
- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**
**Создай два экземпляра album_1 и album_2**
Исполнитель: Queen
Название: Killer Queen
Треки: Brighton rock, Killer Queen, Tenement Funster
Исполнитель: Metallica
Название: Black Album
Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:
    # Создаём конструктор - инициализатор полей класса.
    # Нотации (указания типов после двоеточия) нужны, чтобы редактор кода подсвечивал неправильные типы.
    # Писать нотации необязательно, хотя иногда они здорово облегчают понимание.
    def __init__(self, artist: str, title: str, tracks: list):
        self.artist = artist
        self.title = title
        self.tracks = tracks


# Создаём экземпляры класса с полями, которые определили в конструкторе __init__.
# Т.к. именованных, т.е. со значением по умолчанию аргументов в __init__ нет, то обязательно указывать все.
# Если каких-то аргументов класса изначально может не быть или они одинаковые для всех экземпляров класса,
# то лучше задать в __init__ значение по умолчанию. Например, artist="Unknown Artist", title="Unknown Title".
# Таким образом, при отсутствии названия артиста будет подставляться "Unknown Artist" и т.п.

album_1 = Album('Queen', 'Killer Queen', ['Brighton rock', 'Killer Queen', 'Tenement Funster'])
album_2 = Album('Metallica', 'Black Album', ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])

# Печатаем название артиста, название альбома, количество треков в альюоме.
# В tracks у нас список, поэтому чтобы узнать количество треков, выводим длину списка.
print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков
