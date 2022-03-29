# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

import random

price_list = [57.8, 46.51, 97, 0.1]
for i in range(0, 15):
    price_list.append(random.randint(5, 10000) / 100)
print(f'Исходный список: {price_list}')

# Разбиваем на рубли/копейки для разного форматирования
part1 = ''
part2 = ''
for price in price_list:
    if part1 != '' or part2 != '':
        print(f', ', end='')
    part1 = str(int(price // 1))
    part2 = str(int((price * 100) % 100))
    if len(part2) == 1:
        part2 = part2.zfill(2)
    print(f'{part1} руб {part2} коп', end='')
print('')

# По возрастанию (логику печати повторяем, т.к. функции пока не проходили)
list_id1 = id(price_list)
price_list.sort()
list_id2 = id(price_list)
print(f'До сортировки {list_id1}, после {list_id2} => совпадение {list_id1 == list_id2}')
print('По возрастанию:')

part1 = ''
part2 = ''
for price in price_list:
    if part1 != '' or part2 != '':
        print(f', ', end='')
    part1 = str(int(price // 1))
    part2 = str(int((price * 100) % 100))
    if len(part2) == 1:
        part2 = part2.zfill(2)
    print(f'{part1} руб {part2} коп', end='')
print('')


# По убыванию (логику печати повторяем, т.к. функции пока не проходили)
price_list_new = price_list.copy()
price_list_new.sort(reverse=True)
list_id3 = id(price_list_new)
print(f'До сортировки {list_id2}, после {list_id3} => совпадение {list_id1 == list_id3}')
print('По убыванию:')

part1 = ''
part2 = ''
for price in price_list_new:
    if part1 != '' or part2 != '':
        print(f', ', end='')
    part1 = str(int(price // 1))
    part2 = str(int((price * 100) % 100))
    if len(part2) == 1:
        part2 = part2.zfill(2)
    print(f'{part1} руб {part2} коп', end='')
print('')

# Топ 5 по возрастанию (наверно, из второго списка?)
print('Топ 5:')
part1 = ''
part2 = ''
for price in reversed(price_list_new[0:5]):
    if part1 != '' or part2 != '':
        print(f', ', end='')
    part1 = str(int(price // 1))
    part2 = str(int((price * 100) % 100))
    if len(part2) == 1:
        part2 = part2.zfill(2)
    print(f'{part1} руб {part2} коп', end='')
print('')
