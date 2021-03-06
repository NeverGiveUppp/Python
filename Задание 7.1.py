'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.'''
class Matrix:
    def __init__(self, matrix_1):
        self.matrix_2 = '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_1])
        my_list = []
        for i in matrix_1:
            my_list.append([j for j in i])
        self.matrix_1 = my_list

    def __str__(self):
        self.matrix_3 = str(self.matrix_2)
        return self.matrix_3

    def __add__(self, other):
        a = len(self.matrix_1)
        b = len(other.matrix_1[0])
        for i in range(a):
            for j in range(b):
                self.matrix_1[i][j] = self.matrix_1[i][j] + other.matrix_1[i][j]
            result = self.matrix_1
        return Matrix(result)
m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(m_1 + m_2)

