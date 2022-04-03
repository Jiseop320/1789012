import random
count = 1
o = 0
while True:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)

    print("%d * %d =" %(n1, n2))
    p = int(input("정답을 입력하시오."))
    if(p == (n1*n2)):
        print("정답입니다.")
        o = o + 1
    else:
        print("정답이 아닙니다.")

    con = input("계속하시겠습니까?(y/n) ")
    if(con == 'y'):
        count += count
        continue
    elif(con == 'n'):
        print("정답률은: %.1f입니다."%(o/count*100))
        break


