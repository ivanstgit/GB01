# * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором
# ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

def get_keys(string: str):
    """
    Generate keys for dictionary
    :param string: string with pattern <key1 key2>
    :return: list of keys
    """
    return [string.split()[1][0], string.split()[0][0]]


def get_sort_key(elem: str):
    """
    Generate key for sorting
    :param elem: string with pattern <key1 key2>
    :return: string with key
    """
    return ''.join(get_keys(elem))


def thesaurus_adv(*args, sort_order: str = None):
    """
    Transforms list of arguments into dict
    :param args: names
    :param sort_order = None, 'asc' - ascending, 'desc' - descending
    :return: dictionary of names
    """

    # convert to list for sorting and sort
    arg_list = list(args)
    if sort_order == 'asc':
        arg_list.sort(key=get_sort_key)
    elif sort_order == 'desc':
        arg_list.sort(key=get_sort_key, reverse=True)

    # generate dict
    my_dict = dict()
    for name in arg_list:
        key1, key2 = get_keys(name)

        dict2 = my_dict.get(key1)
        if not dict2:
            dict2 = dict()
            my_dict[key1] = dict2

        value = dict2.get(key2)
        if value:
            value.append(name)
        else:
            dict2[key2] = [name]
    return my_dict


# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", sort_order='asc'))
