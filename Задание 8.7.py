'''1)Реализовать проект «Операции с комплексными числами». 2)Создайте класс «Комплексное число», 3)реализуйте перегрузку методов
сложения и умножения комплексных чисел. 4)Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.'''
class ComplexNumber:
    def __init__(self, A = 0, B = 0):
        self.A = A
        self.B = B

    def __add__(self, other):
        print(f'Сумма равна')
        return f'{self.A + other.A} + {self.B + other.B}j'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'{self.A * other.A - (self.B * other.B)} + {self.B * other.A + other.B}j'



enter_1 = ComplexNumber(1, 1)
enter_2 = ComplexNumber(1, 4)
print(enter_1 + enter_2)
print(enter_1 * enter_2)