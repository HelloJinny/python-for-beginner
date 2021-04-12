inStr = ""
upper, lower, digit, hangle, etc = [0] * 5

inStr = input("문자열을 입력하세요 : ")

## 아스키 코드 값을 이용하는 방법 ##
for x in inStr:
    if ord('A') <= ord(x) and ord(x) <= ord('Z'):  # 대문자
        upper += 1
    elif ord('a') <= ord(x) and ord(x) <= ord('z'):  # 소문자
        lower += 1
    elif ord('가') <= ord(x) and ord(x) <= ord('힣'):  # 한글
        hangle += 1
    elif ord('0') <= ord(x) and ord(x) <= ord('9'):  # 숫자
        digit += 1
    else:  # 기타 문자
        etc += 1

print("대문자 : %d 소문자 : %d 숫자 : %d 한글 : %d 기타 : %d " %
      (upper, lower, digit, hangle, etc))
