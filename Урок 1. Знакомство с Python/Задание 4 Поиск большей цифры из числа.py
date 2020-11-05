# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число "))
max = 0
while number > 0:
    x = number % 10
    if x > max:
        max = x
    number = number // 10
print(f'Max number is {max}')
