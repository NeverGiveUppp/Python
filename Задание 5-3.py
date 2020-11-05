'''3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудниковr и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''
with open("text_3.txt", "r", encoding="utf-8") as my_fail:
    my_d = {}
    average = 0.00
    for line in my_fail:
        key, value = line.split()
        my_d[key] = value
    print(my_d)
average = sum(map(float, my_d.values())) / len(my_d)
print(f'Средняя зарплата работников составила: {average} рублей')

with open('text_3.txt', 'r', encoding='utf-8') as my_fail:
    my_d = {}
    for line in my_fail:
        key, value = line.split()
        my_d[key] = value
        if float(value) < 20000.00:
            print(f'{key} {value}: зарплата меньше 20000')