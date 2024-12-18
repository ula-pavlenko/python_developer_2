# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Audience:
    """Класс учебная аудитория"""

    def __init__(self, number: int, capacity: int):
        """
        Инициализация экземпляра класса учебная аудитория

        :param number: номер аудитории
        :param capacity: вместимость аудитории

        Примеры:
        >>> audience = Audience(10, 50)
        """
        if not isinstance(number, int):
            raise TypeError("Номер аудитории должен быть целым числом")
        if number < 0:
            raise ValueError("Номер аудитории должен быть положительным числом")

        if not isinstance(capacity, int):
            raise TypeError("Вместимость аудитории должна быть целым числом")
        if capacity <= 0:
            raise ValueError("Вместимость аудитории должна быть положительным числом")
        self.number = number
        self.capacity = capacity
        self.occupied = 0

    def start_lecture(self, students_count: int) -> None:
        """
        Начало лекции

        :param students_count: количество студентов

        Примеры:
        >>> audience = Audience(10, 50)
        >>> audience.start_lecture(40)
        >>> audience.occupied
        40
        >>> audience.stop_lecture()
        >>> audience.start_lecture(60)
        Traceback (most recent call last):
        ...
        ValueError: Количество студентов должно быть в интервале от 0 до 50
        """
        if not isinstance(students_count, int):
            raise TypeError("Количество студентов должно быть целым числом")

        if not 0 <= students_count <= self.capacity:
            raise ValueError(
                f"Количество студентов должно быть в интервале от 0 до {self.capacity}"
            )

        self.occupied = students_count

    def stop_lecture(self) -> None:
        """
        Конец лекции

        Примеры:
        >>> audience = Audience(10, 50)
        >>> audience.start_lecture(40)
        >>> audience.stop_lecture()
        >>> audience.occupied
        0
        """
        self.occupied = 0


class Subject:
    """Класс дисциплина обучения"""

    def __init__(self, name: str, duration_hours: int):
        """
        Инициализация экземпляра класса дисциплина обучения

        :param name: название дисциплины
        :param duration_hours: продолжительность дисциплины

        Примеры:
        >>> subject = Subject('Языкознание', 10)
        """
        if not isinstance(name, str):
            raise TypeError("Название дисциплины должно быть строкой")
        if not name:
            raise ValueError("Название дисциплины не может быть пустой строкой")

        if not isinstance(duration_hours, int):
            raise TypeError("Продолжительность дисциплины должна быть целым числом")
        if duration_hours <= 0:
            raise ValueError(
                "Продолжительность дисциплины должна быть положительным числом"
            )

        self.name = name
        self.duration_hours = duration_hours
        self.progress_hours = 0

    def learn(self, hours: int) -> None:
        """
        Процесс обучения

        :param hours: пройдено часов

        Примеры:
        >>> subject = Subject('Языкознание', 10)
        >>> subject.learn(5)
        >>> subject.learn(6)
        Traceback (most recent call last):
        ...
        ValueError: Количество пройденных часов должно быть в интервале от 0 до 5
        """
        if not isinstance(hours, int):
            raise TypeError("Количество пройденных часов должно быть целым числом")
        if not 0 <= hours <= self.remain_hours():
            raise ValueError(
                f"Количество пройденных часов должно быть в интервале от 0 до {self.remain_hours()}"
            )

        self.progress_hours += hours

    def remain_hours(self) -> int:
        """
        Оставшееся время обучения дисциплине

        :returns: в часах

        Примеры:
        >>> subject = Subject('Языкознание', 10)
        >>> subject.learn(5)
        >>> subject.remain_hours()
        5
        """
        return self.duration_hours - self.progress_hours


class Student:
    """Класс студент"""

    def __init__(self, name: str, courses_count: int):
        """
        Инициализация экземпляра класса студент

        :param name: имя студента
        :param courses_count: количество лет обучения

        Примеры:
        >>> student = Student('Иван', 3)
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть строкой")
        if not name:
            raise ValueError("Имя студента не может быть пустой строкой")

        if not isinstance(courses_count, int):
            raise TypeError("Количество лет обучения должно быть целым числом")
        if courses_count <= 0:
            raise ValueError("Количество лет обучения должно быть положительным числом")

        self.name = name
        self.courses_count = courses_count
        self.course = 1

    def next_course(self) -> None:
        """
        Переход на следующий курс

        Примеры:
        >>> student = Student('Иван', 3)
        >>> student.next_course()
        """
        self.course += 1

    def is_graduated(self) -> bool:
        """
        Получен ли диплом

        Примеры:
        >>> student = Student('Иван', 3)
        >>> student.is_graduated()
        False
        >>> student.next_course()
        >>> student.is_graduated()
        False
        >>> student.next_course()
        >>> student.is_graduated()
        False
        >>> student.next_course()
        >>> student.is_graduated()
        True
        """
        return self.course > self.courses_count


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
