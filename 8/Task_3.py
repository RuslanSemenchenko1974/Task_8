"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой."""


class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data1 = input("Введите 1 число: ")
inp_data2 = input("Введите 2 число: ")

try:
    inp_data1 = int(inp_data1)
    inp_data2 = int(inp_data2)

    if inp_data2 == 0:
        raise MyOwnError("Вы ввели ноль!")
    result = inp_data1 / inp_data2
except ValueError:
    print("Вы ввели не число")
except MyOwnError as err:
    print(err)
else:
    print(f"{inp_data2}/{inp_data1} = {result}")
