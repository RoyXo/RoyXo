# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    if x < y:
        x, y = y, x
    if y < z:
        y, z = z, y
    return int(x) + int(y)


print(my_func(input(), input(), input()))

