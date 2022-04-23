# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


if __name__ == '__main__':
    my_list = [Stationery('Скрепка'),
               Pen('Ручка'),
               Pencil('Карандаш'),
               Handle('Маркер')]
    for elem in my_list:
        print(f'{type(elem)}: {elem.__dict__}')
        elem.draw()
