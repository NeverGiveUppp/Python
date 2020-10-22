'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь 
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''
import json
my_dict = {}
pr = {}
prof = 0
i = 0
prof_aver = 0
with open("text_7.txt", "r", encoding="utf-8") as my_file:
    for string_ in my_file.readlines():
        name, firm, proceeds, costs = string_.split()
        my_dict[name] = int(proceeds) - int(costs)
        if my_dict.setdefault(name) >= 0:
            prof = prof + my_dict.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    my_dict.update(pr)
    print(f'Прибыль каждой компании - {my_dict}')

with open('text_77.json', 'w', encoding="utf-8") as my_file:
    json.dump(my_dict, my_file)

    js_dict = json.dumps(my_dict)
    print(f'Файл с расширением json: {js_dict}')