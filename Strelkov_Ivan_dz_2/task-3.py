# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.
#  2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов


src_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Отслеживаем индекс текущего элемента
current_index = 0

# (функции смещения на следующий элемент списка вроде get_next() или оператора ++ не нашел)
# Пробелов между словами не может быть больше, чем слов - используем простой цикл
max_index = 2*len(src_list)

for i in range(max_index):
    if current_index >= len(src_list):
        break
    src_element = src_list[current_index]

    # check for sign
    if src_element.startswith('+') or src_element.startswith('-'):
        src_element_prefix = src_element[0:1]
        src_element_wo_prefix = src_element[len(src_element_prefix):len(src_element)]
    else:
        src_element_prefix = ''
        src_element_wo_prefix = src_element

    # check is numeric
    if src_element_wo_prefix.isnumeric():
        src_list.insert(current_index, '"')
        current_index += 1
        if int(src_element) < 10:
            src_list[current_index] = src_element_prefix + src_element_wo_prefix.zfill(2)
        current_index += 1
        src_list.insert(current_index, '"')

    current_index += 1

# join не подходит, т.к. добавляет пробелы между кавычками и числом
# Отслеживаем открывающие/закрывающие кавычки - is_opened = True/False
res_string = ''
is_opened = 0
for elem in src_list:
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
