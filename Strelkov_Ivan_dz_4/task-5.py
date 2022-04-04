# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
#  Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
#  Убедиться, что ничего лишнего не происходит.
# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
import utils


if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:
        currency_list = sys.argv[1:]
    else:
        currency_list = ['USD', 'EUR', 'UZS', 'RUB']

    for currency in currency_list:
        rate = utils.currency_rates(currency)
        if rate:
            print(f'{rate[1]}, {rate[0]}')
        else:
            print(f'{rate}')
