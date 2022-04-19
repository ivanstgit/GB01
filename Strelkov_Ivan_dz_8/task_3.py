# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arg_list = [f'{str(arg)}: {str(type(arg))}' for arg in args]
        arg_list.extend([f'{str(arg)}={str(arg_value)}: {str(type(arg_value))}' for arg, arg_value in kwargs.items()])
        print(f'{func.__name__}({", ".join(arg_list)}): {type(result)}')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_pow(x, y: int):
    return x ** y


def test_hiding(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@type_logger
@test_hiding
def calc_pow2(x, y: int):
    return x ** y


if __name__ == '__main__':
    print(calc_cube(3))
    print(calc_pow(3.5, y=3))
    print(calc_pow2(3.5, y=3))
