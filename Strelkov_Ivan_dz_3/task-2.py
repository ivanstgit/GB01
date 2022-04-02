# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(text_eng: str, dictionary: dict):
    """
    Translate string to another language using chosen dictionary. Keeps capitalized word.
    :param text_eng: text to translate
    :param dictionary: dict used
    :return: string with translated text
    """
    result = dictionary.get(text_eng.lower(), None)
    if text_eng[0].isupper():
        result = str(result).capitalize()
    return result


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

print(num_translate_adv('one', dictionary_eng_ru))
print(num_translate_adv('Eight', dictionary_eng_ru))
print(num_translate_adv('eit', dictionary_eng_ru))
