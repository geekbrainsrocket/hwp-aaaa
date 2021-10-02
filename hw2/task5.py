# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

number = int(input("Введите новое число: "))
my_list = [8, 5, 4, 3]
count_in = my_list.count(number)
for element in my_list:
    if count_in > 0:
        i = my_list.index(number)
        my_list.insert(i+count_in, number)
        break
    else:
        if number > element:
            temp_el = my_list.index(element)
            my_list.insert(temp_el, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
