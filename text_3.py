# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32


def my_func():
    data = [['Putin ', '1000 \n'], ['Volodin ', '500 \n'], ['Zhara ', '1450000000 \n'], ['Ilon Mask ', '8000000']]
    try:
        with open('my_first.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(data)):
                file.writelines(data[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                zp = int((l[i].split())[1])
                if zp < 20000:
                    poor.append((l[i].split())[0])
                sum += zp
            print(f'Средний доход сотрудников  {sum / len(data) / 12:.2f}')
            print(f'Меньше 20 тыс. руб. у сотрудников: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'



