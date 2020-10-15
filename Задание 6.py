# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def my_func(text):
    for i in text:
        if 97 <= ord(i) <= 122 or ord(i) == 32:
            pass
        else:
            text = text.replace(i, "", 1)
    text = text.split()
    for num, word in enumerate(text):
        text[num] = word.capitalize()
    text = " ".join(text)

    return text


print(my_func(input('Введите слово из маленьких латинских букв ')))

# def int_func():
#     user_input = input("Введите слово из маленьких латинских букв ")
#     print(user_input.title())
#     return
# int_func()
