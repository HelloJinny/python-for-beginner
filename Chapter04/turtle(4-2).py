import turtle

## 전역 변수 선언 부분 ##
num = 0  # 입력 받을 10진수
swidth, sheight = 1000, 300  # 윈도창의 폭과 넓이
curX, curY = 0, 0  # 거북이의 현재 위치

## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)  # 거북이가 위쪽을 바라보도록 설정

    num = int(input("숫자를 입력하세요. : "))
    binary = bin(num)  # 입력받은 숫자를 2진수 문자열로 변환
    curX = swidth / 2  # 거북이 초기 위치를 윈도창 오른쪽 끝으로 설정
    curY = 0
    for i in range(len(binary) - 2):  # 5를 입력시 0b101이므로 앞 0b를 제외한 101 글자 수에 해당하는 3번을 반족
        turtle.goto(curX, curY)  # 거북이랑 계산된 좌표로 이동
        if num & 1:  # 2진수로 변환했을 때 맨 하위 비트가 1인지 체크
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()  # 위에서 설정된 크기와 색상으로 거북이 도장을 현재 위치에 찍는다.
        curX -= 50  # X좌표를 왼쪽으로 50만큼 이동시킨다.
        num >>= 1  # 숫자를 오른쪽을 1 시프트시킨다. 오른쪽 비트는 이미 앞에서 표현했으므로 제거

turtle.done()
