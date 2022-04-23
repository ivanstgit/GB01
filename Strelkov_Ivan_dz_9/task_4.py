# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы:go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
import random


class Car:
    _speed: float
    color: str
    name: str
    _is_police: bool
    __direction: str
    directions = frozenset({'right', 'left', 'top', 'down'})

    def __init__(self, color='', name='', is_police=False):
        self._speed = 0.0
        self.color = color
        self.name = name
        self._is_police = is_police
        self.__direction = 'top'

    def _get_print_name(self):
        return self.color + ' ' + self.name

    def go(self, speed: float, direction='right'):
        if direction not in self.directions:
            raise ValueError('Incorrect direction')
        if speed <= 0:
            raise ValueError('Incorrect speed')

        self._speed = speed
        self.__direction = direction
        print(f'{self._get_print_name()} starts going {self.__direction} with speed {self._speed}')

    def turn(self, direction: str):
        if direction not in self.directions:
            raise ValueError(f'Incorrect direction for car {self._get_print_name()}')
        if not self._speed:
            raise ValueError(f'Car {self._get_print_name()} stopped, turning is impossible')

        print(f'changing direction from {self.__direction} to {direction}')
        self.__direction = direction

    def stop(self):
        self._speed = 0
        print(f'{self._get_print_name()} stopped')

    def show_speed(self):
        print(f'Speed of {self._get_print_name()}: {self._speed}')


class TownCar(Car):
    def __init__(self, color='', name=''):
        super().__init__(color=color, name=name, is_police=False)

    def show_speed(self):
        Car.show_speed(self)
        if self._speed > 60:
            print(f'legal speed limit exceeded')


class SportCar(Car):
    def __init__(self, color='', name=''):
        super().__init__(color=color, name=name, is_police=False)


class WorkCar(Car):
    def __init__(self, color='', name=''):
        super().__init__(color=color, name=name, is_police=False)

    def show_speed(self):
        Car.show_speed(self)
        if self._speed > 40:
            print(f'legal speed limit exceeded')


class PoliceCar(Car):
    def __init__(self, color='', name=''):
        super().__init__(color=color, name=name, is_police=True)


if __name__ == '__main__':
    car_list = [TownCar('white', 'BMW'),
                SportCar('red', 'ferrari'),
                WorkCar('yellow', 'kamaz'),
                PoliceCar('apple', 'horse')]
    for car in car_list:
        print('==============================================================================================')
        print(f'Car {type(car)}: {car.__dict__}')
        rand_speed = random.randint(61, 100)
        car.go(rand_speed)
        print(f' status: {car.__dict__}')
        car.show_speed()
        car.turn(random.choice(list(Car.directions)))
        print(f' status: {car.__dict__}')
        car.stop()
        print(f' status: {car.__dict__}')

    # incorrect value testing
    try:
        car_list[0].turn('f')
    except ValueError as e:
        print(e)
    try:
        car_list[0].turn('top')
    except ValueError as e:
        print(e)
    try:
        car_list[0].go(-1)
    except ValueError as e:
        print(e)
