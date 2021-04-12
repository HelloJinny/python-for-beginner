import turtle
import random
from tkinter.simpledialog import *
import math

## 전역 변수 선언 부분 ##
inStr = ''
swidth, sheight = 300, 300
tX, tY, txtSize = 0, 0, 20
radius, angle, radian = 100, 0, 0

## 메인 코드 부분 ##
turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

angle = 360 / len(inStr)

for ch in inStr:
    radian = 3.14*angle/180

    tX = radius*math.cos(radian)
    tY = radius*math.sin(radian)
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.goto(tX, tY)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize,  'bold'))

    angle += 360 / len(inStr)

turtle.done()
