# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from functools import reduce

list_numbers = [i for i in range(100, 1001, 2)]
print(list_numbers)


def my_sum(first, second):
    return first + second

result = reduce(my_sum, list_numbers)
print(result)