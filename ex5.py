t = int(input("온도를 입력하시오: "))
conv = input("섭씨(C)로 바꿀건가요? 화씨(F)로 바꿀건가요?")

if(conv == 'C'):
    Tc = (5 / 9) * (t - 32)
    print("%d F = %d C" %(t, Tc))

elif(conv == 'F'):
    Tf = (9 / 5) * t + 32
    print("%d C = %d F" %(t, Tf))