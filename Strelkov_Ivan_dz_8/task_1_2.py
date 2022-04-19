# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?
import re

FILE_NAME = 'nginx_logs.txt'
RE_LOG = re.compile(r"((?:\d{1,3}\.){3}\d{1,3}|(?:\S*\:){1,7}\S*)[\s-]{5}\[(.*)\]\s\"([a-zA-Z]+)\s(\S+)\s.+\"\s(\d{1,"
                    r"3})\s(\d+)")
    # r"(.+)[\s-]{5}\[(.*)\]\s\"([a-zA-Z]+)\s(\S+)\s.+\"\s(\d{1,3})\s(\d+)")


def parse_log_string(in_str: str):
    """
    Parse string into tuple
    :param in_str:
    :return: ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
    """
    if RE_LOG.match(in_str):
        result = RE_LOG.findall(in_str)[0]
    else:
        raise ValueError('Wrong_line')
    return result


file_list = list()
counter = 0

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    for line in f:
        counter += 1
        try:
            elem = parse_log_string(line)
            # ля демонстрации выводим 10 строк
            if counter < 11 or counter == 5694 or counter == 23957:
                print(elem)
        except ValueError:
            print(f'Error in line {counter}, {line}')
