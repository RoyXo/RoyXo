a = int(input("Введите километраж: "))
d = int(input("Введите день пробежки: "))
day=0
for i in range(1, d):
    a=a*1.1
    day=i+1
print(f"На {day}-й день не менее {a} км.")