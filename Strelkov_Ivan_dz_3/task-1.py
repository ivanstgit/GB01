# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

def num_translate(text_eng, dictionary):
    """
    Translate string to another language using chosen dictionary
    :param text_eng: text to translate
    :param dictionary: dict used
    :return: string with translated text
    """
    return dictionary.get(text_eng, None)


dictionary_eng_ru = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

print(num_translate('one', dictionary_eng_ru))
print(num_translate('eight', dictionary_eng_ru))
print(num_translate('eit', dictionary_eng_ru))
