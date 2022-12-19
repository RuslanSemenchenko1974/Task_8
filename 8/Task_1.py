"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    matrix_count = 0

    def __init__(self, param):
        self.param = param
        Matrix.matrix_count += 1

    def __str__(self):
        print(f'MATRIX: {Matrix.matrix_count}')
        for el in self.param:
            print(el)
        return ""

    def __add__(self, other):
        result = []
        for i in range(len(self.param)):
            prom1 = []
            for j in range(len(self.param[i])):
                prom1.append(self.param[i][j] + other.param[i][j])
            result.append(prom1)
        return Matrix(result)


list_1 = [i for i in range(5)]
list_2 = [i for i in range(5, 10)]
list_3 = [i for i in range(10, 15)]

my_list = [list_1, list_2, list_3]

d = Matrix(my_list)
print(d)
c = Matrix(my_list)
print(c)
print("Сумма:")
e = d + c
print(e)
