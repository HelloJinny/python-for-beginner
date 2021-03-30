num = int(input('시프트할 숫자는? : '))
count = int(input('출력할 횟수는? : '))

for i in range(1, count + 1):
    print("%d << %d = %d" % (num, i, num << i))

for i in range(1, count + 1):
    print("%d >> %d = %d" % (num, i, num >> i))
