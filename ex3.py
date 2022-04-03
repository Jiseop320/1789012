def factorial(n):
    fac = 1

    for i in range(1, n+1, 1):
        fac *= i
    print("n!은?: %d" %fac)

n = int(input("자연수 n을 입력하시오: "))
factorial(n)