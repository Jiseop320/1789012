n = int(input("자연수 n을 입력하시오: "))
sum = 0

for i in range(0, n, 2):
    sum += i

print("자연수 n 사이의 짝수의 합은: %d" %sum)