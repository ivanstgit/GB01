# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.


FILE_NAME = 'nginx_logs.txt'
file_list = list()
ip_dict = dict()

with open(FILE_NAME, 'r', encoding='utf-8') as f:

    for line in f:
        str1, str2 = line.strip().split('] "')
        remote_address = str1.split(' -')[0]
        request_type, requested_resource = str2.split(' ')[0:2]
        new_list_elem = (remote_address, request_type, requested_resource)
        # task1
        file_list.append(new_list_elem)

        # task2
        if ip_dict.get(remote_address):
            ip_dict[remote_address] += 1
        else:
            ip_dict[remote_address] = 1

# task1
for elem in file_list:
    print(elem)

# task2
spammer_cnt = max(ip_dict.values())
gen_dict = (ip for ip, counter in ip_dict.items() if counter == spammer_cnt)
for spammer_ip in gen_dict:
    print(f'Spamer: {spammer_ip} with {spammer_cnt}')
gen_dict.close()







