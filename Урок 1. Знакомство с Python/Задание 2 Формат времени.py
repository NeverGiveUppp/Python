# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_sec = int(input('Enter the number of seconds to convert to hours and minutes '))
minutes = user_sec // 60
seconds = user_sec % 60
hours = minutes // 60
answer = minutes // 60
print(f'{hours:02.0f}:{answer:02.0f}:{seconds:02.0f}')