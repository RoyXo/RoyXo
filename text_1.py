# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func(x, y):
    try:
        return int(x)/int(y)
    except ZeroDivisionError:
        print("Division by zero is not possible.")
    except ValueError:
        print("You should inter integers.")


print(my_func(input(), input()))
