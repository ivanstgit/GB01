# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
import decimal


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: decimal.Decimal, bonus: decimal.Decimal):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


if __name__ == '__main__':

    positions = [Position('Иван', 'Иванов', 'Дворник', decimal.Decimal('100'), decimal.Decimal('21.4')),
                 Position('Иван', 'Петров', 'Охранник', decimal.Decimal('200'), decimal.Decimal('0')),
                 Position('Jonh', 'Smith', 'Director', decimal.Decimal('1000'), decimal.Decimal('666.66'))]
    for pos in positions:
        print(pos.__dict__)
        print(f'{pos.get_full_name()}: {pos.get_total_income()}')
