import turtle

## 전역 변수 선언 부분 ##
swidth, sheight = 500, 500

## 메인 코드 부분 ##
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()  # 거북이를 아래쪽으로 이동
turtle.goto(0, -sheight / 2)
turtle.pendown()
turtle.speed(10)  # 거북이 속도 설정 (10 - 빨리, 1 - 천천히, 0 - 움직임이 보이지 않을 정도로 가장 빨리 움직임)

for radius in range(1, 250):
    if radius % 7 == 1:
        turtle.pencolor('red')
    elif radius % 7 == 2:
        turtle.pencolor('orange')
    elif radius % 7 == 3:
        turtle.pencolor('yellow')
    elif radius % 7 == 4:
        turtle.pencolor('green')
    elif radius % 7 == 5:
        turtle.pencolor('blue')
    elif radius % 7 == 6:
        turtle.pencolor('navyblue')
    else:
        turtle.pencolor('purple')

    turtle.circle(radius)

turtle.done()
