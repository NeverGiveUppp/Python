'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.\
Важно,чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —'''
my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as my_file:
    for string_ in my_file.readlines():
        string_ = string_.replace('(-)', '')
        string_ = string_.replace('(п)', '')
        string_ = string_.replace('(лаб)', '')
        string_ = string_.replace('(пр)', '')
        lesson = string_.split()[0]
        string_ = [int(el) for el in string_.split() if el.isdigit()]
        my_dict.update({lesson: sum(string_)})
    print(my_dict)