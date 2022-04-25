# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

class Clothes:
    def __init__(self, title: str):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @property
    def consumption(self):
        return None


class Coat(Clothes):
    def __init__(self, title: str, size: int):
        super().__init__(title)
        self.__size = size

    def __str__(self):
        return f'Пальто "{self.title}" размера {self.__size}'

    @property
    def consumption(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, title: str, height: int):
        super().__init__(title)
        self.__height = height

    def __str__(self):
        return f'Костюм "{self.title}" роста {self.__height}'

    @property
    def consumption(self):
        return 2 * self.__height + 0.3


if __name__ == '__main__':
    my_list = [Coat('НКВД 2.0', 45),
               Suit('Дипломат 144%', 4)]

    for el in my_list:
        print(f'Для {el} нужно {el.consumption} м2 ткани')