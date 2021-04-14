from tkinter import *
from time import *

## 전역  변수 선언 부분 ##
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif",
             "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]  # 사진 9장의 파일명을 저장
photoList = [None] * 9  # PhotoImage() 함수로 생성할 변수 9개 준비
num = 0  # 현재 사진의 번호

## 함수 선언 부분 ##


def clickNext():
    global num  # num 전역 변수를 함수 안에서 사용
    num += 1
    if num > 8:  # 마지막 사진에서 <다음> 버튼을 누르면 처음 사진을 표시
        num = 0
    photo = PhotoImage(file="gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


# 메인 코드 부분
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="gif/" + fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
