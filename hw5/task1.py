# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


txt_file = open("text_5-1.txt", "w", encoding="utf-8")
print("Введенный вами текст будет записан в файл\nНачните ввод текста :\n")
input_flag = True
while input_flag:
    in_str = input()
    if in_str:
        print(in_str, file=txt_file)
    else:
        print('Текст записан в файл text_5-1.txt')
        input_flag = False
txt_file.close()
