## 변수의 선언 부분 ##
i, k, starNum = 0, 0, 0
numStr, ch, statStr = "", "", ""

## 메인 코드 부분 ##
if __name__ == "__main__":
    numStr = input("숫자를 여러 개 입력하세요 : ")
    print("")

    i = 0
    ch = numStr[i]
    while True:
        starNum = int(ch)

        statStr = ""
        for k in range(0, starNum):
            statStr += "\u2665"
            k += 1

        print(statStr * 2)

        i += 1
        if (i > len(numStr) - 1):
            break
        ch = numStr[i]
