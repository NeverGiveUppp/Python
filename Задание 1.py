
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func():
    try:
        arg_1 = int(input("Введите первое число "))
        arg_2 = int(input("Введите второе число "))
        result = round(arg_1 / arg_2, 2)
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "ZeroDivisionError"

    return result


print(f'Результат деления равен {(my_func())}')
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
a = [123, True, 'abc', 18.6, [56, 75]]
print(a)
for i in a:
    print(type(i))

