# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    txt_file = open("text_5-2.txt", "r", encoding="utf-8")
    string_count = 0
    words_count = 0
    for line in txt_file:
        string_count += 1
        words_count_line = len(line.split())
        words_count = words_count + words_count_line
        print(f"строка {string_count} содержит {words_count_line} слов;")
    print(f"Файл {txt_file.name} содержит {string_count} строк, и {words_count} слов.")
    print('Ошибка чтения файла, программа завершена !')
    txt_file.close()
except FileNotFoundError:
    print('Ошибка открытия файла')
