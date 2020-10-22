'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''
inter = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
translate = []
with open("text_4.txt", "r", encoding="utf-8") as my_file:
    for n in my_file:
        n = n.split(' ', 1)
        translate.append(inter[n[0]] + n[1])
    print(translate)

with open('text_4_new.txt', 'w', encoding="utf-8") as my_new_file:
    my_new_file.writelines(translate)