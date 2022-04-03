f = open("C:/Users/82106/Desktop/file.txt", 'r')

count = 0
lines = f.readlines()
for line in lines:
    if lines == '':
        break
    count += 1
    print("%d." %cnt, line)

f.close()