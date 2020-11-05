'''2. Создать текстовый файл (не программно),
ъсохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''
with open("first_fail.txt", "r", encoding="utf-8") as my_file:
    i = 0
    while string := my_file.readline():
        words = len(string.split())
        i = i + 1
        print(f' В {i} строке: {words} слов(о/а)')
