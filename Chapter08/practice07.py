inStr, result = "", ""

inStr = input("문자열 --> ")

for x in inStr:
    if x.isdigit():
        continue
    result += x

print("숫자 제거 --> " + result)
