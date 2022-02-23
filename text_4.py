number = int(input())
max_num=number%10
number=number//10
while number>0:
    n = number%10
    if n>max_num:
        number = number // 10
        continue
    if n<=max_num:
        n=max_num
print(n)