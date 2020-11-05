# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
# from random import randint
# numbers = [randint(10, 1000) for i in range(15)]
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # как не выводить 300???????????
new_list = []
i = 0
for el in numbers:
    if el > numbers[i - 1]:
        new_list.append(el)
    i += 1
new_list.pop(0)

print(numbers)
print(new_list)

''' 2 способ'''
# new_list = [el for el in numbers if el > numbers[numbers.index(el) -1]]
# print(new_list)
