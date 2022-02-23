total = int(input("Выручка: "))
minus = int(input("Расходы: "))
if total>minus:
    persons = int(input("Колличество персонала: "))
    profit = (total-minus)/persons
    print(total-minus, "$ Ваща выручка.", profit, "$ На каждого сотрудника.")
else:
    print(minus-total, "Ващи убытки.")