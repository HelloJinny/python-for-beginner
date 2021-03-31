num = input('16진수 한 글자 입력 : ')

if ('0' <= num <= '9') or ('A' <= num <= 'F') or ('a' <= num <= 'f'):
    print("10진수 ===> ", int(num, 16))
else:
    print("16진수가 아닙니다.")
