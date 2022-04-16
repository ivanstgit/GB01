# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import json
import math
import os

ENCODING = 'utf-8'


def get_dict_key(int_size):
    """
    Generates int key for dict (up to 10^x)
    :param int_size:
    :return:
    """
    try:
        log_size = math.log10(int_size) // 1
        result = 10 ** int(log_size + 1)
    except ValueError:
        result = 0
    return result


def get_statistics(root_dir):
    size_dict = dict()

    for root, dirs, files in os.walk(root_dir):
        if len(files):
            for item in os.scandir(root):
                if item.is_file():
                    file_size = item.stat().st_size
                    file_ext = item.name.split('.')[-1]
                    dict_key = get_dict_key(file_size)
                    elem = size_dict.get(dict_key)
                    if not elem:
                        elem = (1, [file_ext])
                        size_dict[dict_key] = elem
                    else:
                        elem = (elem[0] + 1, elem[1])
                        if not elem[1].count(file_ext):
                            elem[1].append(file_ext)
                        size_dict[dict_key] = elem
    return size_dict


if __name__ == '__main__':
    my_dir = 'my_project'
    # my_dir = 'some_data' # Очень большой коммит получается...
    my_dict = get_statistics(my_dir)
    # print(my_dict)
    try:
        with open(my_dir + '_summary.json', 'w', encoding=ENCODING) as f:
            json.dump(my_dict, f)
    except Exception as e:
        print(f'Result file save error:{e}')
        exit(1)
