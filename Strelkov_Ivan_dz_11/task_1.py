# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    __SEP = '-'

    def __init__(self, date_str: str):
        self.__date_str = date_str

    @classmethod
    def split(cls, date_str: str):
        """
        Split date (w/o validation)
        :return: (year: int, month: int, day: int)
        """
        return tuple(map(int, date_str.split(cls.__SEP)))

    @staticmethod
    def is_valid(date_str: str):

        try:
            day, mon, year = Date.split(date_str)
        except ValueError as e:
            # print(e)
            return False

        if year < 0 or year > 9999 or mon < 0 or mon > 12:
            return False

        if mon == 2:
            days_in_mon = 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29
        elif mon in {1, 3, 5, 7, 8, 10, 12}:
            days_in_mon = 31
        else:
            days_in_mon = 30

        if day < 0 or day > days_in_mon:
            return False

        return True


if __name__ == '__main__':
    def trace(date_str: str):
        if Date.is_valid(date_str):
            print(f'Date {date_str}: {Date.split(date_str)}')
        else:
            print(f'Date {date_str} is not valid.')


    trace('20-11-2019')
    trace('20/11/2019')
    trace('31-11-2019')
    trace('20--11-2019')

