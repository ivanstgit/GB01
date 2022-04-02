# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
from random import sample, choices


def get_jokes(cnt: int, repeats_permitted=True):
    """
    :param cnt: number of jokes returned
    :param repeats_permitted: repeats of words permitted
    :return: list of strings with jokes
    """
    if repeats_permitted:
        func = choices
    else:
        func = sample

    result_list = list()
    for noun, adverb, adjective in zip(func(nouns, k=cnt), func(adverbs, k=cnt), func(adjectives, k=cnt)):
        result_list.append(f'{noun} {adverb} {adjective}')

    return result_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(3))
print(get_jokes(3, False))
