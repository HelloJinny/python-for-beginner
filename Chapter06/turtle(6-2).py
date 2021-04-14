import turtle
import random

## 전역 변수 부분 ##
swidth, sheight = 350, 350
r, g, b, angle, dist = 0, 0, 0, 30, 5

## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle. title('거북이 소라 모양 그리기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 30, height=sheight + 30)
    turtle.screensize(swidth, sheight)
    turtle.pensize(5)

    for i in range(80):
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor((r, g, b))

        dist += 1
        turtle.forward(dist)
        turtle.left(angle)

    turtle.done()
