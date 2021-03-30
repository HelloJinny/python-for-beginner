import random

a = random.randrange(1, 7)
b = random.randrange(1, 7)

print("A의 주사의 숫자는 %d입니다." % a)
print("B의 주사의 숫자는 %d입니다." % b)

if a > b:
    print("A가 이겼습니다.")
elif a < b:
    print("B가 이겼습니다.")
else:
    print("비겼습니다.")
