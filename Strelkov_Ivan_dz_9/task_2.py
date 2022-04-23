# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
import decimal


class Road:
    _length: int
    _width: int

    def __init__(self, length_m: int, width_m: int):
        self._length = length_m
        self._width = width_m

    def calc_mass_in_tons(self, mass_kg_per_square_m_cm=25, height_cm=1):
        return decimal.Decimal(self._length * self._width * mass_kg_per_square_m_cm * height_cm / 1000)


if __name__ == '__main__':
    my_road = Road(length_m=5000, width_m=20)
    print(my_road.calc_mass_in_tons())
