'''45. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open("text_5.txt", "w+", encoding="utf-8") as my_fail:
    try:
        user_enter = input('Введите числа для подсчета суммы ')
        my_fail.writelines(user_enter)
        answer = user_enter.split()
    except ValueError:
        print('Ошибка при вводе данных')
    print(sum(map(int, answer)))