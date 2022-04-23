# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
# и завершать скрипт.
import time


class TrafficLight:
    __color: str
    __color_settings = {'red': (7, 'yellow'),
                        'yellow': (2, 'green'),
                        'green': (1, 'red')}

    def __init__(self, color='red'):
        if color not in self.__color_settings.keys():
            raise ValueError('Incorrect color!')
        self.__color = color

    def __get_color_settings(self, color):
        return self.__color_settings.get(color)

    def running(self, color='red'):
        if color not in self.__color_settings.keys():
            raise ValueError('Incorrect color!')
        else:
            print(f'Running from {self.__color} to {color}')

        action = self.__get_color_settings(self.__color)
        action_list = [action]
        if self.__color != color:
            while action[1] != color:
                action = self.__get_color_settings(action[1])
                action_list.append(action)

        for action in action_list:
            print(f'   {self.__color}:', sep=' ')
            for i in range(action[0]):
                print(f'      {action[0] - i}')
                time.sleep(1)
            self.__color = action[1]
        return 'Running successful'


if __name__ == '__main__':
    my_traffic_light = TrafficLight('red')
    print(my_traffic_light.running('green'))
    print(my_traffic_light.running('red'))

# value checker
    try:
        print(my_traffic_light.running('grin'))
    except ValueError as e:
        print(e)
