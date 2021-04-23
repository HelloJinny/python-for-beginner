num1 = int(input("*** 시작 숫자를 입력하세요 (2이상) : "))
num2 = int(input("*** 끝 숫자를 입력하세요 : "))
sum = 0

# for i in range(num1, num2 + 1):
#     sum = 0

#     for k in range(1, i + 1):


for i in range(num1, num2):

    sum = sum + i

    if num % i == 0:
        a = 1
        break
    else:
        a = 0

    for j in range(2, i):
        if i % j == 0:
            break

if a == 1:
    print("%d는 소수가 아닙니다." % num)
else:
    print("%d는 소수입니다." % num)

print("%d부터 %d까지 소수의 합은 %d입니다." % num1, num2, sum)
