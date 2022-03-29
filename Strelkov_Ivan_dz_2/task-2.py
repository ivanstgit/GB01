# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

src_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
res_list = []

for src_element in src_list:
    # check for sign
    if src_element.startswith('+') or src_element.startswith('-'):
        src_element_prefix = src_element[0:1]
        src_element_wo_prefix = src_element[len(src_element_prefix):len(src_element)]
    else:
        src_element_prefix = ''
        src_element_wo_prefix = src_element

    # check is numeric
    if src_element_wo_prefix.isnumeric():
        src_element_value = int(src_element)
        res_list.append('"')
        if src_element_value < 10:
            res_list.append(src_element_prefix + src_element_wo_prefix.zfill(2))
        else:
            res_list.append(src_element)
        res_list.append('"')
    else:
        res_list.append(src_element)

# join не подходит, т.к. добавляет пробелы между кавычками и числом
# Отслеживаем открывающие/закрывающие кавычки - is_opened = True/False
res_string = ''
is_opened = 0
for elem in res_list:
    res_string += elem
    if elem == '"':
        if is_opened == 0:
            is_opened = 1
        else:
            is_opened = 0
            res_string += ' '
    elif is_opened == 0:
        res_string += ' '

print(res_string)
