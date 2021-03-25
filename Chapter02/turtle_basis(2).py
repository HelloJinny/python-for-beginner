import turtle

## 함수 선언부분 ##

## 변수선언 부분 ##
myT = None  # 초기화

## 메인 코드 부분 ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0, 4):
    myT.forward(200)
    myT.right(90)

turtle.done()
