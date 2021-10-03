# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

i = 0
test_list = ['1', '2', '3', '4', '5']
if len(test_list) % 2 == 0:
    while i < len(test_list):
        temp_el = test_list[i]
        test_list[i] = test_list[i+1]
        test_list[i+1] = temp_el
        i += 2
else:
    while i < len(test_list) - 1:
        temp_el = test_list[i]
        test_list[i] = test_list[i + 1]
        test_list[i + 1] = temp_el
        i += 2
print(test_list)
