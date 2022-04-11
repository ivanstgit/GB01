# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
# значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
#
# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи
# и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию,
# когда пользователь вводит номер записи, которой не существует.
import decimal as dec

FILE_NAME = 'bakery.csv'
FILE_ENCODING = 'utf-8'
VALUE_LENGTH = 20
EXT_DELIMITER = ','


def ext_value_is_incorrect(str_ext: str):
    """
    Check value format & length
    """
    if not str_ext.replace(EXT_DELIMITER, '').isdecimal():
        return f'value {str_ext} is not a number'

    if len(str_ext.split(EXT_DELIMITER)[0]) + 2 > VALUE_LENGTH:
        return f'value {str_ext} is too big (max length {VALUE_LENGTH} permitted)'

    return None


def get_value_int(str_ext: str):
    """
    Convert value to internal format (fixed width)
    """
    dec.getcontext().prec = 2
    cleared_string = '{value:.2f}'.format(value=dec.Decimal(str_ext.replace(' ', '').replace(EXT_DELIMITER, '.')))
    return cleared_string.zfill(VALUE_LENGTH)


def get_value_ext(str_int: str):
    """
    Convert value to external format
    """
    str_ext = ''
    if str_int:
        str_ext = str(dec.Decimal(str_int)).replace('.', EXT_DELIMITER)

    return str_ext


def add_record(sale: str):
    """
    Add record to the file
    """

    err = ext_value_is_incorrect(sale)
    if err:
        return err

    sale_str = get_value_int(sale)
    sale_str += '\n'
    with open(FILE_NAME, 'a', encoding=FILE_ENCODING) as f:
        f.write(sale_str)
    return None


def get_records(start=1, end=0):
    """
    Get list of records from the file
    """
    result = list()
    with open(FILE_NAME, 'r', encoding=FILE_ENCODING) as f:
        if start > 1:
            # value stored in ANSI, fixed length with \n at the end
            f.seek((VALUE_LENGTH + 1) * (start - 1))
        curr_pos = start
        for line in f:
            if curr_pos > end and end:
                break
            result.append(get_value_ext(line.strip()))
            curr_pos += 1

    return result


def edit_record(pos: int, new_value: str):
    """
    Edit record in the file at selected pos
    :return result message
    """

    if not pos > 0:
        return f'position {pos} should be positive'

    err = ext_value_is_incorrect(new_value)
    if err:
        return err

    new_value_int = get_value_int(new_value)
    old_value = '0'

    with open(FILE_NAME, 'r+', encoding=FILE_ENCODING) as f:
        # check size of file
        new_position = (VALUE_LENGTH + 1) * (pos - 1)
        f.seek(0, 2)
        max_position = f.tell() - (VALUE_LENGTH + 1)
        if new_position > max_position:
            return f'position {pos} not found'

        # value stored in ANSI, fixed length with \n at the end
        f.seek(new_position, 0)
        #print(f.tell())
        old_value = get_value_ext(f.readline().strip())
        f.seek(new_position, 0)
        #print(f.tell())
        f.write(new_value_int)

    return f'position {pos} edited {old_value}->{new_value}'


if __name__ == '__main__':
    print('Test mode: ')
    with open(FILE_NAME, 'w', encoding=FILE_ENCODING) as f:
        print('file content deleted')
    print('Adding records (None - added): ')
    print(add_record('345f1'))
    print(add_record('86456745976567984756459765456456'))
    print(add_record('1345,1'))
    print(add_record('2345,1'))
    print(add_record('3345,1'))
    print(add_record('4345,1'))
    print(add_record('5345,1'))
    print(add_record('6345,1'))
    print(add_record('7345,1'))
    print(add_record('8345,1'))
    # print(get_records(1, 2222))
    print(get_records(5, 7))
    print(edit_record(6, '700'))
    print(get_records(5, 7))
    print(edit_record(-1, '700'))
    print(edit_record(1000000, '700'))
