# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Device:
    _groups = []

    def __init__(self, group: str, title: str):
        self._group = group
        self._title = title
        if group not in Device._groups:
            Device._groups.append(group)

    @property
    def group(self):
        return self._group

    @staticmethod
    def groups():
        return Device._groups.copy()


class Printer(Device):
    def __init__(self, group: str, title: str, *args):
        super().__init__(group=group, title=title)
        self._is_color = args[0]

    def __str__(self):
        return f'Принтер [{self.group}] {self._title}'


class Scanner(Device):
    def __init__(self, group: str, title: str, *args):
        super().__init__(group=group, title=title)
        self._is_potable = args[0]

    def __str__(self):
        return f'Сканер [{self.group}] {self._title}'


class UnitNotFound(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self):
        self.__counter = 0
        self.__stock = dict()

    def __str__(self):
        result = 'Склад с оборудованием: \n'
        for group in Device.groups():
            device_cnt = sum([1 for item in self.__stock.values() if item and item.group == group])
            if device_cnt:
                result += f'   {group}: {device_cnt}\n'
        return result

    def add_unit(self, unit: Device):
        self.__counter += 1
        self.__stock[self.__counter] = unit
        return f'{str(unit)} прибыл на склад с присвоением учетного номера [{self.__counter}] '

    def remove_unit(self, id: int):
        unit = self.__stock.get(id)
        if unit:
            self.__stock[id] = None
        else:
            raise UnitNotFound('Оборудование отсутствует на складе')

        return f'{str(unit)} [{id}] выбыл со склада'


if __name__ == '__main__':

    DEVICES = {
        'printer': ('Printer', '<Цветной? True/False>'),
        'scaner': ('Scanner', '<Портативный?  True/False>'),
    }

    COMMANDS = {
        'stop': ('Остановка программы', 'нет'),
        'add': ('Приемка на склад', '<группа номенклатуры> <название> <параметры группы>'),
        'remove': ('Отпуск', '<код учета>'),
        'status': ('Баланс', 'нет')
    }

    my_storage = Storage()
    print(f'Вводите команды, нажимая Enter. Перечень команд:')
    for key, value in COMMANDS.items():
        print(f' {key}, назначение: {value[0]}, параметры: {value[1]}')
    print(f'Группы номенклатуры и их параметры:')
    for key, value in DEVICES.items():
        print(f' {key}: {value[1]}')
    print('Например, "add printer Xerox2n True", "remove 1"')

    line = ''
    my_list = []
    while True:
        line = input(' ')

        try:
            my_list = line.split()
            command = my_list[0]
            if command == 'stop':
                break
            elif command == 'status':
                print(my_storage)
            elif command == 'remove':
                unit_id = int(my_list[1])
                print(my_storage.remove_unit(unit_id))
            elif command == 'add':
                group = my_list[1]
                device = globals()[DEVICES.get(group)[0]]
                title = my_list[2]
                print(my_storage.add_unit(device(group, title, my_list[2:])))
            else:
                print('Команда отсутствует')

        except UnitNotFound as e:
            print(e.txt)
        except Exception as e:
            print('Неверный синтаксис')
