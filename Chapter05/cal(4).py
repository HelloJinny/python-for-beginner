num1 = int(input("*** 시작 숫자를 입력하세요 (2이상) : "))
num2 = int(input("*** 끝 숫자를 입력하세요 : "))
sum = 0
sosuYN = True


for i in range(num1, num2 + 1):  # 합계
    cnt = 0

    if i == 1:  # 1은 소수 X, 2로 넘어가기
        continue

    for j in range(1, i + 1):
        if i % j == 0:  # i를 j로 나눠서 j에 대한 나머지가 0이 아니라면 i는 소수
            cnt += 1  # 소수일 때만 카운트 세기

    if cnt <= 2:  # 소수는 1과 자기 자신 이외에 나올 수 없다
        sum += i

print("%d부터 %d까지 소수의합은 %d입니다." % (num1, num2, sum))