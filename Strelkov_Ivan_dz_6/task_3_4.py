# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями
# — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг
# данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
# преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа.
# Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.

# task3
import json

FILE_NAME_USERS = 'users.csv'
FILE_NAME_HOBBIES = 'hobby.csv'
FILE_NAME_RESULT = 'user_hobby.json'
FILE_NAME_RESULT1 = 'user_hobby_t4.json'
SEPARATOR = ','

if __name__ == '__main__':

    import sys

    # python3 task_3_4.py user/users.csv hobby.csv user_w_hobby.json
    if len(sys.argv) > 1:
        params = {index: value for index, value in zip(range(len(sys.argv) - 1), sys.argv[1:])}
        if params.get(0):
            FILE_NAME_USERS = params[0]
        if params.get(1):
            FILE_NAME_HOBBIES = params[1]
        if params.get(2):
            FILE_NAME_RESULT = params[2]

with open(FILE_NAME_USERS, 'r', encoding='utf-8') as f:
    user_list = [' '.join(line.strip().split(SEPARATOR)) for line in f.read().splitlines()]

with open(FILE_NAME_HOBBIES, 'r', encoding='utf-8') as f:
    hobby_list = [line.strip() for line in f.read().splitlines()]

if len(hobby_list) > len(user_list):
    exit(1)

hobby_dict = {index: hobbies for index, hobbies in zip(range(len(hobby_list)), hobby_list)}
user_dict = {user: hobby_dict.get(index) for user, index in zip(user_list, range(len(user_list)))}

with open(FILE_NAME_RESULT, 'w', encoding='utf-8') as f:
    json.dump(user_dict, f)


# task 4
# Чтобы хоть как-то можно было бы понять содержимое файла, сохраняем атрибуты юзера в словарь
# Так как нет гарантий уникальности имени и не задан алгоритм обработки дубликатов, а также логика их определения
# (например, Иванов и ИВАНОВ), то генерируем синтетический ключ записи

user_dict.clear()
with open(FILE_NAME_USERS, 'r', encoding='utf-8') as f_u, \
        open(FILE_NAME_HOBBIES, 'r', encoding='utf-8') as f_h:
    user_counter = 0
    for line in f_u:
        user_counter += 1
        hobby_line = f_h.readline()
        if hobby_line:
            hobby_list = hobby_line.strip().split(SEPARATOR)
        else:
            hobby_list = None
        user_key = 'user_'+str(user_counter).zfill(10)
        user_data = dict()
        user_data['name_parsed'] = line.strip().split(SEPARATOR)
        user_data['hobbies'] = hobby_list
        user_dict[user_key] = user_data

    hobby_line = f_h.readline()
    if hobby_line:
        exit(1)

with open(FILE_NAME_RESULT1, 'w', encoding='utf-8') as f_res:
    json.dump(user_dict, f_res)
