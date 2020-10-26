'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.'''
import time


def timer_(i):
    timing = time.time()
    while i > 0:
        if time.time() - timing >= 1:
            i = i - 1
            timing = time.time()
            print(f"{i} секунд")


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self, color):
        print("Смена цвета через: ")
        self.color = color


a = TrafficLight("RED")
print(a._TrafficLight__color)
timer_(7)
a.running("RED")

a_2 = TrafficLight("YELLOW")
print(a_2._TrafficLight__color)
timer_(2)
a_2.running("YELLOW")

a_2 = TrafficLight("GREEN")
print(a_2._TrafficLight__color)
timer_(7)
a_2.running("GREEN")
