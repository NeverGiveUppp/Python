# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
name, hours, rate_per_hour, prize = argv
resultat = (int(hours) * int(rate_per_hour)) + int(prize)
print(resultat)

# hours = выработка в часах
# rate_per_hour = ставка в час
# prize = премия
