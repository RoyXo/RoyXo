n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end="")
    for j in range(i, 1, -1):
        print(j - 1, end="")
    print("")

# Дано натуральное число nn.
# Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером: