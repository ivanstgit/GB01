# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def get_key(elem: str):
    """
    Generate key for a string
    :param elem: source string
    :return: str key
    """
    return elem[0]


def thesaurus(*args, sort=False):
    """
    Transforms list of arguments into dict
    :param args: names
    :param sort: keys should be sorted
    :return: dictionary of names
    """
    key_list = list(map(get_key, args))
    if sort:
        key_list.sort()

    my_dict = dict.fromkeys(key_list)
    for key in my_dict.keys():
        my_dict[key] = list(filter(lambda elem: get_key(elem) == key, args))

    return my_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
print(thesaurus("Петр", "Иван", "Мария", "Илья", sort=True))
