# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, init_val: list):
        self.__row_size = len(init_val)
        self.__col_size = 0
        self.__matrix = list()

        for row in init_val:
            if not self.__col_size:
                self.__col_size = len(row)
            elif self.__col_size != len(row):
                raise ValueError('different size!')

            self.__matrix.append(row.copy())

    def __str__(self):
        result = ''
        for row in self.__matrix:
            if result:
                result += '\n'
            result += f'|{" ".join(map(str,row))}|'
        return result

    def __add__(self, other):
        if type(other) is not Matrix:
            raise ValueError('Only matrix supported!')
        if self.__row_size != other.__row_size or self.__col_size != other.__col_size:
            raise ValueError('Different size!')

        new_list = [[self.__matrix[i][j] + other.__matrix[i][j]
                     for j in range(self.__col_size)]
                    for i in range(self.__row_size)]
        c = Matrix(new_list)
        return c


if __name__ == '__main__':
    a = Matrix([[1, 33.2], [3, 4]])
    print(f'{a.__dict__}')
    print(a)
    print('+')
    b = Matrix([[2, 1], [-1, 7]])
    print(b)
    print('=')
    print(a+b)

