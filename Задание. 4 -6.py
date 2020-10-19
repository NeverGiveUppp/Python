# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count
from itertools import cycle

user_enter = count(int(input('Введите число ')), 1)
n = int(input('Количество шагов: '))
i = 0
while i <= n:
    i += 1
    print(next(user_enter))

##         CYCLE


ent = cycle(input('Введите любое слово или набор цифр: '))
a = 0
while a <= 15:
    a += 1
    print(next(ent))
