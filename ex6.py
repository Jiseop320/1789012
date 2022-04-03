import math

r = int(input("반지름의 길이를 입력하시오: "))

s = 4 * math.pi * (r**2)
v = (4 / 3) * math.pi * (r**3)

print("구의 겉면적 S: %.2f \n 구의 부피 V: %.2f" %(s, v))