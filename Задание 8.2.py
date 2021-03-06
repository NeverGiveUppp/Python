'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''
class StopError(Exception):
    def __init__(self, a):
        self.a = a

a = int(input('Введите число делитель для делимого 100: '))
try:
    a = int(a)
    res = 100 / a
    if a <= 0:
        raise StopError('Число должно быть больше 0')
except (ZeroDivisionError, TypeError, StopError) as err:
    print('ошибочка')
else:
    print(res)
finally:
    print("Программа завершена")