# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

firm_list = []
firm_tmp = {}
firm_summ = 0
firm_count = 0
try:
    src_file = open("text_5-7.txt", "r", encoding="utf-8")
    for line in src_file:
        firm_name, firm_type, debit, credit = line.split()
        firm = firm_name + " " + firm_type
        summ = float(debit) - float(credit)
        firm_tmp[firm] = summ
        if summ > 0:
            firm_count += 1
            firm_summ += summ
    src_file.close()
    firm_list.append(firm_tmp)
    if firm_count:
        firm_summ = firm_summ / firm_count
        summation = dict(average_profit=firm_summ)
        firm_list.append(summation)
    print(firm_list)
except FileNotFoundError:
    print('Ошибка открытия файла')
try:
    with open("less_5-7.json", "w", encoding="utf-8") as firm_json_file:
        json.dump(firm_list, firm_json_file, ensure_ascii=False, indent=4)
except FileNotFoundError:
    print('Ошибка записи JSON файла')
