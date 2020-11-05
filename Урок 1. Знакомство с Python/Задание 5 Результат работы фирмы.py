# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Введите выручку фирмы "))
cost = int(input("Введите издержку фирмы "))
profit = revenue - cost

if cost > revenue:
    print("Фирма имеет убыток ", "-", profit)

elif revenue > cost:
    print("Фирма имеет прибыль ", "+", profit)

if profit > 0:
    rent = (profit / revenue) * 100
    print(f'Рентабельность равна, {rent:.2f}, %')

if profit > 0:
    staff = int(input("Введите количество сотрудников фирмы "))
    staff_prof = profit / staff
    print(f'{staff_prof:.2f}, прибыль фирмы на одного сотрудника')
