# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = int(input("Enter number "))

result = str(num)

number1 = result + result
num1 = int(number1)

number2 = result + result + result
num2 = int(number2)

summa = num + num1 + num2
print(summa)