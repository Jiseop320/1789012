a = []
b = []
def listProd(a, b):

    a.append(int(input("a의 첫번째 숫자는?: ")))
    a.append(int(input("a의 두번째 숫자는?: ")))
    a.append(int(input("a의 세번째 숫자는?: ")))
    b.append(int(input("b의 첫번째 숫자는?: ")))
    b.append(int(input("b의 두번째 숫자는?: ")))
    b.append(int(input("b의 세번째 숫자는?: ")))

    value = 0
    value = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    print("a =", a)
    print("b =", b)
    print("두 리스트의 곱의 합은? :%d" %value)

listProd(a, b)