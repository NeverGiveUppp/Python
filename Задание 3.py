# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
while True:
    num_month = int(input("Enter the number of the month from 1 to 12 "))
    if num_month > 0 and num_month <= 12:
        break
    else:
        print("Error. Enter the number from 1 to 12 ")
# Решение через словарь
seasons = {
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn",
    12: "Winter"
}
month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
answer_ses = seasons[num_month]
answer_mon = month[num_month]
print(f'User unswer: {answer_mon}, this is {answer_ses} ')

# Решение через список
list_season = ["", "Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn",
               "Autumn", "Winter"]
print("This number corresponds to the time of year", list_season[num_month])
