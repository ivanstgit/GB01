# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести
# текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class MyError(ValueError):
    def __init__(self, txt):
        self.txt = txt


def to_number(line: str):
    try:
        if line.isdigit():
            result = int(line)
        else:
            result = float(line)
    except ValueError:
        raise MyError('Некорректный ввод')
    return result


if __name__ == '__main__':
    STOP_COMMAND = 'stop'
    print(f'Вводите числа, нажимая Enter. Для остановки введите {STOP_COMMAND}.')
    line = ''
    my_list = []
    while line != STOP_COMMAND:
        line = input(' ')
        if line == STOP_COMMAND:
            break

        try:
            my_list.append(to_number(line))
        except MyError as e:
            print(e.txt)

    print(my_list)
