# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом
# расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
import os

WRITE_MODE = 'OVERWRITE'
CONFIG_FILE = 'config.yaml'
ENCODING = 'utf-8'
CONFIG_SHIFT = '   '
CONFIG_LEAVE_PREFIX = '- '
CONFIG_FOLDER_SUFFIX = ':'


def get_level_filename(config_line: str):
    """
    Calculation of level (depth) of file and filename
    :return tuple (int level, str file, bool is_folder)
    """
    level = 0
    filename = ''
    is_folder = False
    tmp_str = config_line
    if tmp_str.endswith('\n'):
        tmp_str = tmp_str[:-1]
    while True:
        if tmp_str.startswith(CONFIG_SHIFT):
            tmp_str = tmp_str[len(CONFIG_SHIFT):]
            level += 1
        elif tmp_str.startswith(CONFIG_LEAVE_PREFIX):
            filename = tmp_str[len(CONFIG_LEAVE_PREFIX):]
            break
        elif tmp_str.endswith(CONFIG_FOLDER_SUFFIX):
            filename = tmp_str[:-len(CONFIG_FOLDER_SUFFIX)]
            is_folder = True
            break
        else:
            break
    return level, filename, is_folder


config_list = list()
try:
    with open(CONFIG_FILE, 'r', encoding=ENCODING) as f_conf:
        config_list = f_conf.readlines()
except Exception as e:
    print(f'config read error: {e}')

dir_path_list = ['.']
counter = 0

for line in config_list:
    counter += 1
    level, filename, is_folder = get_level_filename(line)
    if not filename:
        print(f'config error in line {counter}')
        exit(1)

    dir_path_list = dir_path_list[:level]

    if is_folder:
        dir_path_list.append(filename)
        dir_path = os.path.join(*dir_path_list)
        if not os.path.exists(dir_path):
            try:
                os.mkdir(dir_path)
            except Exception as e:
                print(f'directory {dir_path} creation error:{e}')
    else:
        dir_path = os.path.join(*dir_path_list)
        file_path = os.path.join(dir_path, filename)
        if not os.path.exists(file_path) or WRITE_MODE == 'OVERWRITE':
            try:
                with open(file_path, 'w', encoding=ENCODING) as f:
                    f.write('')
            except Exception as e:
                print(f'file {file_path} error:{e}')
                exit(2)
        else:
            print(f'file {file_path} exists, interrupting')
            exit(3)

print(f'done: {counter} files and folders created')
