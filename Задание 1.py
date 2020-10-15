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
