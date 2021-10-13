# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_list = ["один", "два", "три", "четыре"]
try:
    src_file = open("text_5-4_source.txt", "r", encoding="utf-8")
    res_file = open("text_5-4_result.txt", "w", encoding="utf-8")
    for line in src_file:
        text, spl, num = line.split()
        print(f"{rus_list[int(num) - 1]} {spl} {num}", file=res_file)
    src_file.close()
    res_file.close()
except FileNotFoundError:
    print('Ошибка открытия файла')
