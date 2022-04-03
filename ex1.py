n = int(input("자연수 n을 입력하시오: "))
sum = 0
for i in range(0, n, 1):
    sum += i

print("n까지의 자연수의 합은? %d" %sum)