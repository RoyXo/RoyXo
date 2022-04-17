# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivission:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def divide(x, y):
        try:
            return (x / y)
        except:
            return (f"Деление на ноль недопустимо")


div = ZeroDivission(10, 100)
print(ZeroDivission.divide(10, 0))
print(ZeroDivission.divide(10, 0.1))
print(div.divide(100, 0))
