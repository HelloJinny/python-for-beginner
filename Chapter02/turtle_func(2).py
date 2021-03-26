import turtle
import random

## 함수 선언 부분 ##

# 기능 1 : 마우스 왼쪽 버튼만 눌러도 임의의 색상이 지정되고 거북이의 크기가 변경되면서 선이 그려지도록 한다.


def screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 10)
    turtle.pencolor((r, g, b))
    turtle.shapesize(tSize)
    turtle.pendown()
    turtle.goto(x, y)


# 기능 2 : 마우스 오른쪽 버튼을 누르면 거북이가 클릭한 지점까지 선울 그리지 않고 이동만 하도록 한다.


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)


## 변수 선언 부분 ##
pSize, tSize = 10, 0  # 선의 두께와 거북이의 크기
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
