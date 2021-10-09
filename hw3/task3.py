# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_sum(num_1, num_2, num_3):
    my_sum = num_1 + num_2 + num_3
    return my_sum - min(num_1, num_2, num_3)

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
print(f'{my_sum(a, b, c)}')
