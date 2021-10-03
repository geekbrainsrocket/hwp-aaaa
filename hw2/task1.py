# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 11
my_float = 1.1
my_str = "pycharm"
my_list = ['git', '2']
my_tuple = ('commit', '3')
my_dict = {'device': 'portal', 'browser': 'firefox'}

my_final_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in my_final_list:
    print(f'{i} is {type(i)}')
