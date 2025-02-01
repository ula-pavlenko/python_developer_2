TAX_RATE = {
    'car': 2.5,
    'truck': 5.0
}

class Car:
    """ Базовый класс автомобиля."""

    def __init__(self, brand: str, model: str, production_year: int, horsepower: int):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param production_year: Год выпуска автомобиля.
        :param horsepower: Мощность двигателя в лошадиных силах.

        """
        self.brand = brand
        self.model = model
        self.year = production_year
        self.horsepower = horsepower

    def __str__(self):
        return f"Автомобиль {self.brand} {self.model} {self.year} года выпуска, мощностью {self.horsepower} л.с."

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, production_year={self.year!r}, horsepower={self.horsepower!r})"

    def start_engine(self):
        """ Запуск двигателя. """
        print(f"{self} Двигатель запущен")

    def stop_engine(self):
        """ Остановка двигателя. """
        print(f"{self} Двигатель остановлен")

    def calc_tax(self) -> float:
        """ Подсчет налога. Перегружен в дочерних классах. """
        return 0.0


class PassengerCar(Car):
    def __init__(self, brand: str, model: str, production_year: int, horsepower: int, num_doors: int):
        """
        Конструктор класса PassengerCar.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param production_year: Год выпуска автомобиля.
        :param horsepower: Мощность двигателя в лошадиных силах.
        :param num_doors: Количество дверей автомобиля.
        """
        super().__init__(brand, model, production_year, horsepower)
        self.num_doors = num_doors

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, production_year={self.year!r}, horsepower={self.horsepower!r}, num_doors={self.num_doors!r})"

    def open_trunk(self):
        """ Открытие багажника. """
        print(f"{self} Багажник открыт")

    def close_trunk(self):
        """ Закрытие багажника. """
        print(f"{self} Багажник закрыт")

    def calc_tax(self) -> float:
        """ Подсчет налога с учетом ставки на легковой автомобиль. """
        return self.horsepower * TAX_RATE['car']


class Truck(Car):
    def __init__(self, brand: str, model: str, production_year: int, horsepower: int, max_load: float):
        """
        Конструктор класса Truck.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param production_year: Год выпуска автомобиля.
        :param horsepower: Мощность двигателя в лошадиных силах.
        :param max_load: Грузоподъемность.
        """
        super().__init__(brand, model, production_year, horsepower)
        self.max_load = max_load

    def __str__(self):
        return f"Грузовик {self.brand} {self.model} {self.year} года выпуска, мощностью {self.horsepower} л.с."

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, production_year={self.year!r}, horsepower={self.horsepower!r}, max_load={self.max_load!r})"

    def load_cargo(self, weight: float):
        """
        Погрузка грузовика.

        :param weight: Вес груза.
        """
        if weight > self.max_load:
            raise ValueError("Вес груза превышает грузоподъемность")
        print(f"{self} Загружен на {int(weight / self.max_load * 100)}%")

    def calc_tax(self) -> float:
        """ Подсчет налога с учетом ставки на грузовой автомобиль. """
        return self.horsepower * TAX_RATE['truck']


if __name__ == "__main__":
    car = PassengerCar('Toyota', 'Corolla', 2020, 99, 4)
    print(car)
    print(repr(car))
    car.start_engine()
    car.stop_engine()
    car.open_trunk()
    car.close_trunk()
    print(f'Налог на {car}: {car.calc_tax()}')
    truck = Truck('МАЗ', '4371', 2020, 170, 4.5)
    print(truck)
    print(repr(truck))
    truck.start_engine()
    truck.stop_engine()
    truck.load_cargo(4.5)
    print(f'Налог на {truck}: {truck.calc_tax()}')
