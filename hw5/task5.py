# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def func(xx):
    tmp = []
    for x in (el for el in range(1, xx, 3)):
        yield x


try:
    with open('text_5-5_nums.txt', "w", encoding="utf-8") as new_file:
        for el in func(130):
            print(f'{el}', end=" ", file=new_file)
    try:
        with open('text_5-5_nums.txt') as num_file:
            summ = 0
            for line in num_file:
                tmp_list = map(int, line.split())
                for num in tmp_list:
                    summ += num
            print(summ)
    except FileNotFoundError:
        print('Ошибка обработки файла, программа завершена !')
except FileNotFoundError:
    print('Ошибка генерации файла')
