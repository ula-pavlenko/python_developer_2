import doctest


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        >>> book = PaperBook('Стихи', 'Пушкин', '100')
        Traceback (most recent call last):
        ...
        TypeError: The type of PaperBook.pages should be int
        >>> book = PaperBook('Стихи', 'Пушкин', -100)
        Traceback (most recent call last):
        ...
        ValueError: The value of PaperBook.pages should be positive integer
        """
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        """
        >>> book = PaperBook('Стихи', 'Пушкин', 100)
        >>> repr(book)
        "PaperBook(name='Стихи', author='Пушкин', pages=100)"
        >>> str(book)
        'Книга Стихи. Автор Пушкин'
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"The type of {self.__class__.__name__}.pages should be int")
        if not value > 0:
            raise ValueError(f"The value of {self.__class__.__name__}.pages should be positive integer")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        >>> book = AudioBook('Стихи', 'Пушкин', '2.5')
        Traceback (most recent call last):
        ...
        TypeError: The type of AudioBook.duration should be float
        >>> book = AudioBook('Стихи', 'Пушкин', -2.5)
        Traceback (most recent call last):
        ...
        ValueError: The value of AudioBook.duration should be positive float
        """
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        >>> book = AudioBook('Стихи', 'Пушкин', 2.5)
        >>> repr(book)
        "AudioBook(name='Стихи', author='Пушкин', duration=2.5)"
        >>> str(book)
        'Аудиокнига Стихи. Автор Пушкин'
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, float):
            raise TypeError(f"The type of {self.__class__.__name__}.duration should be float")
        if not value > 0:
            raise ValueError(f"The value of {self.__class__.__name__}.duration should be positive float")
        self._duration = value


if __name__ == "__main__":
    doctest.testmod()
