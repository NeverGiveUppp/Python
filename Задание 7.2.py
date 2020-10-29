'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def square_coat(self):
        return self.v / 6.5 + 0.5

    def square_suit(self):
        return 2 * self.h + 0.3

    @property
    def total_area(self):
        return f'Площадь ткани для пальто: {round(self.v / 6.5 + 0.5)}\nПлощадь ткани для костюма:{2 * self.h + 0.3}'

class Coat(Clothes):      # (V/6.5 + 0.5)
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_coat = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Количество ткани на пальто: {self.square_coat}'


class Suit(Clothes):         # (2*H + 0.3)
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_suit = round(2 * self.v + 0.3)

    def __str__(self):
        return f'Количество ткани на костюм: {self.square_suit}'



c = Coat(10, 10)
s = Suit(10, 10)

print(c.total_area)

