import turtle
import random

## 함수 선언 부분 ##

# 기능 : 마우스 왼쪽 버튼을 누르면 클릭한 위치에 다양한 색상, 크기, 각도의 거북이 모양 도장이 찍힌다.


def screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()

    tSize = random.randrange(1, 10)
    tAngle = random.randrange(1, 360)

    turtle.color(r, g, b)
    turtle.shapesize(tSize)
    turtle.right(tAngle)

    turtle.stamp()

    turtle.penup()
    turtle.goto(x, y)


## 변수 선언 부분 ##
tAngle, tSize = 0, 0
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.onscreenclick(screenLeftClick, 1)

turtle.done()
