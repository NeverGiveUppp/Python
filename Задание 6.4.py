'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.'''
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет вперед')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_left(self):
        print('Поворачивает на лево')

    def turn_right(self):
        print('Поворачивает на право')

    def show_speed(self):
        print(f'Превышении скорости автомобилем {self.name} Скорость {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Cкорость {self.name}  {self.speed} км/ч')
        if self.speed > 60:
            print(f'Внимание превышение скорости автомобилем  {self.name}')
        else:
            print(f'Авто {self.name} движется с нормальной скоростью')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Cкорость {self.name}  {self.speed} км/ч')
        if self.speed > 40:
            print(f'Внимание превышение скорости автомобилем  {self.name}')
        else:
            print(f'Авто {self.name} движется с нормальной скоростью')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police_car(self):
        if self.is_police:
            print(f'{self.name} это полицейский автомобиль')
        else:
            print(f'{self.name} это не полицейский автомобиль')

solaris = TownCar(20, 'white', 'solaris', False)
ferrari = SportCar(160, 'red', 'ferrari', False)
kamaz = WorkCar(55, 'orange', 'kamaz', False)
priora = PoliceCar(70, 'silvery', 'priora', True)

kamaz.show_speed()
solaris.show_speed()
ferrari.go()
ferrari.turn_left()
ferrari.turn_right()
ferrari.stop()
print(f'{ferrari.name} это полицейская машина? {ferrari.is_police} ')
print(f'{priora.name} это полицейская машина? {priora.is_police}')
print(f'{ferrari.name} цвета {ferrari.color}')



