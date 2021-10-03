# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'зима',
                  2: 'зима',
                  3: 'весна',
                  4: 'весна',
                  5: 'весна',
                  6: 'лето',
                  7: 'лето',
                  8: 'лето',
                  9: 'осень',
                  10: 'осень',
                  11: 'осень',
                  12: 'зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц {number} из списка это {month_list[i]}")
            break
    print(f"Месяц {number} из словаря {month_dict[number]}")
else:
    print("You made a mistake")
