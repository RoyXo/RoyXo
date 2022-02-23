seconds = int(input())
h = seconds//3600
m = seconds//60-(h*60)
s = seconds-(m*60)-(h*3600)
print(f"{h}:{m}:{s}")