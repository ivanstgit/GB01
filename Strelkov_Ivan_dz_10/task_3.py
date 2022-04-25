# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». 
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()). 
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до 
# целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух 
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток 
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. 
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. 
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.

class Cell:
    def __init__(self, parts: int):
        self.__parts = parts

    def __str__(self):
        return f'Cell with {self.__parts} parts'

    def __add__(self, other):
        if type(other) is not Cell:
            raise ValueError(f'{other} is not Cell')
        return Cell(self.__parts + other.__parts)

    def __sub__(self, other):
        if type(other) is not Cell:
            raise ValueError(f'{other} is not Cell')
        result = self.__parts - other.__parts
        if result < 0:
            raise ValueError(f'{other} bigger than {self}')
        return Cell(result)

    def __mul__(self, other):
        if type(other) is not Cell:
            raise ValueError(f'{other} is not Cell')
        return Cell(self.__parts * other.__parts)

    def __truediv__(self, other):
        if type(other) is not Cell:
            raise ValueError(f'{other} is not Cell')
        return Cell(self.__parts // other.__parts)

    def __floordiv__(self, other):
        return self / other

    def make_order(self, cnt):
        return ''.join(['*\n' if i % cnt == 0 and i < self.__parts else '*' for i in range(1, self.__parts + 1)])


if __name__ == '__main__':
    a = Cell(15)
    b = Cell(4)

    print(f'{a}+{b}={a + b}')
    print(f'{a}-{b}={a - b}')
    print(f'{a}*{b}={a * b}')
    print(f'{a}/{b}={a / b}')
    print(f'{a}//{b}={a // b}')
    print('make_4')
    print(f'{a.make_order(4)}')
    print('make_5')
    print(f'{a.make_order(5)}')
    print('make_20')
    print(f'{a.make_order(20)}')
