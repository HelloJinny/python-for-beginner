## 피보나치 수열 함수 ##
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


## 전역 변수 ##
n = 0

## main ##
if __name__ == "__main__":
    while(1):
        n = int(input("피보나치 수열 F(N)의 N값을 입력하세요 --> "))
        print("F(%d) = %d" % (n, fibo(n)))
