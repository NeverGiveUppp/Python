'''1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''
user_enter = []
while True:
    line = input("Введите любое кол-во строк, для завершения оставьте поле пустым: ")
    if line == '':
        exit()
    else:
        newline = line + '\n'
        user_enter.append(newline)
    with open("first_fail.txt", "w", encoding="utf-8") as my_fail:
        my_fail.writelines(user_enter)


