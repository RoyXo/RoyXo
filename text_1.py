# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.



with open('my_first.txt', 'w+', encoding="utf-8") as file:
    while True:
        line_file = input('Погнали!!!!: ')
        file.write(line_file + '\n')
        if not line_file:
            break