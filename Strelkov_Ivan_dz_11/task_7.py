# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
# import decimal
from decimal import Decimal, getcontext
from random import random, randint


class MyComplexNum:
    def __init__(self, real: Decimal, img: Decimal):
        self.__real = real
        self.__img = img

    def __add__(self, other):
        return MyComplexNum(self.__real + other.__real,
                            self.__img + other.__img)

    def __mul__(self, other):
        return MyComplexNum(self.__real * other.__real - self.__img * other.__img,
                            self.__img * other.__real + self.__real * other.__img)

    def __str__(self):
        return f'({self.__real},{self.__img}i)'


if __name__ == '__main__':
    getcontext().prec = 3
    my_pairs = [(MyComplexNum(Decimal(randint(-100, 100))/10, Decimal(randint(-10, 10))),
                 MyComplexNum(Decimal(randint(-10, 10)), Decimal(randint(-10, 10))))
                for i in range(10)]

    for num1, num2 in my_pairs:
        print(f'{num1} + {num2} = {num1 + num2}')
        print(f'{num1} * {num2} = {num1 * num2}')
