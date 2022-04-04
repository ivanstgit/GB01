# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы
# с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

import requests as rq
import datetime as dt
import decimal as dec


def currency_rates(currency: str):
    """
    Return last currency rate from CBR
    :param currency: currency code, for instance 'USD'
    :return: tuple(datetime.date date, decimal rate)
    """
    curr = currency.upper()

    cbr_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    cbr_request = rq.get(cbr_url)

    # parse xml on main tag <Valute> and tags <Valcurs>
    xml = cbr_request.text
    valute_list_trash = xml.split('<Valute')
    date_str = valute_list_trash[0].split('<ValCurs Date="')[1][0:10]
    date_day, date_mon, date_year = date_str.split('.')
    res_date = dt.date(day=int(date_day), month=int(date_mon), year=int(date_year))

    nominal_str = ''
    value_str = ''
    for trash in valute_list_trash[1:]:
        curr_str = trash.split('<CharCode>')[1][0:3]
        if curr_str == curr:
            nominal_str = trash.split('<Nominal>')[1].split('</Nominal>')[0].replace(',', '.')
            value_str = trash.split('<Value>')[1].split('</Value>')[0].replace(',', '.')
            break

    if value_str != '' and nominal_str != '':
        result = (res_date, dec.Decimal(value_str) / dec.Decimal(nominal_str))
    else:
        result = None
    return result


if __name__ == '__main__':
    for currency in ['USD', 'EUR', 'UZS', 'RUB']:
        rate = currency_rates(currency)
        if rate:
            print(f'{currency}: {rate[1]} on {rate[0]}')
        else:
            print(f'{currency}: {rate}')

    # import lxml.etree as et
    # xml_root = et.fromstring(cbr_request.content)
    # for valute in xml_root.getchildren():
    #     return 0

    # xml_doc = minidom.parseString(cbr_request.text)
    # xml_main_mode = xml_doc.getElementsByTagName('ValCurs')[0]
    # curs_date = xml_main_mode.getAttribute('Date')
    # print(curs_date)
    # for node in xml_doc.getElementsByTagName('Valute'):
    #     print(node)