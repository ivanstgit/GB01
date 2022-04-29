# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


def divide(nominator: float, denominator: float):
    if denominator == 0:
        raise MyZeroDivisionError('Попытка деления на ноль')
    else:
        return nominator / denominator


if __name__ == '__main__':
    my_str = input('Введите числитель и знаменатель через пробел: ')
    try:
        nominator, denominator = map(float, my_str.split())
        print(divide(nominator, denominator))
    except MyZeroDivisionError as e:
        print(e.txt)
    except ValueError as e:
        print('Некорректный ввод')

