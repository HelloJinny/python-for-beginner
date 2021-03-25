import turtle
import random

## 함수 선언 부분 ##

# 기능 1 : 마우스 왼쪽 버튼을 누르면 거북이가 클릭한 지점까지 임의의 색상으로 선을 그리면서 따라오도록 한다. + 임의의 색성이 지정 , 커북이으 ㅣ크기 변경


def screenLeftClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    turtle.pendown()
    turtle.goto(x, y)


# 기능 2 : 마우스 오른쪽 버튼을 누르면 거북이가 클릭한 지점까지 선울 그리지 않고 이동만 하도록 한다.


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

# 기능 3 : 마우스 가운데 버튼을 누르면 거북이가 임의로 크기를 확대 또는 축소한다.


def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()


## 변수 선언 부분 ##
pSize, tSize = 10, 0  # 선의 두께와 거북이의 크기
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
