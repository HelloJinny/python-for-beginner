import os.path
import os
from tkinter import *

## 함수 선언 부분 ##


def clickListBox(evt):
    global currentDir, searchDirList
    if (dirListBox.curselection() == ()):
        return
    dirName = str(dirListBox.get(dirListBox.curselection()))
    if dirName == '상위폴더':
        if len(searchDirList) == 1:
            return
        searchDirList.pop()
    else:
        searchDirList.append(currentDir + dirName + '\\')
    fillListBox()


def fillListBox():
    global currentDir, searchDirList, dirLabel, dirListBox, fileListBox
    dirListBox.delete(0, END)
    fileListBox.delete(0, END)

    dirListBox.insert(END, "상위폴더")
    currentDir = searchDirList[len(searchDirList) - 1]
    dirLabel.configure(text=currentDir)
    folderList = os.listdir(currentDir)

    index = 0  # 파일 목록 위치
    for item in folderList:
        if os.path.isdir(currentDir + item):
            dirListBox.insert(END, item)
        elif os.path.isfile(currentDir + item):
            fileSize = os.path.getsize(
                currentDir + item)    # 파일 사이즈 저장 (Byte 단위)
            fileName, fileExt = os.path.splitext(item)  # 파일 이름과 확장자를 튜플로 분리

            '''
            1MB 미만은 KB 단위로 출력,
            1MB 이상은 MB단위로 출력
            '''
            if fileSize < 1000000:   # 1MB 미만
                fileSize = fileSize // 1000     # KB 단위로 (소수점 x)
                fileListBox.insert(END, item + "   " +
                                   "[" + str(fileSize) + " KB]")
            elif 1000000 <= fileSize:
                fileSize = fileSize // 1000000     # MB 단위로 (소수점 x)
                fileListBox.insert(END, item + "   " +
                                   "[" + str(fileSize) + " MB]")

            '''
            실행 파일인 exe, msi 등은 초록색,
            그림 파일인 jpg, bmp, png, gif 등은 빨간색,
            파이썬 파일인 py는 파란색
            '''
            fileExt = fileExt.lower()  # 대문자 확장자일 경우 소문자로 변환
            if fileExt == '.exe' or fileExt == '.msi':  # 확장자 별로 분류
                fileListBox.itemconfig(index, foreground="green")
            elif fileExt == '.jpg' or fileExt == '.bmp' or fileExt == '.png' or fileExt == '.gif':
                fileListBox.itemconfig(index, foreground="red")
            elif fileExt == '.py':
                fileListBox.itemconfig(index, foreground="blue")

            index += 1


## 전역 변수 선언 부분 ##
window = None
searchDirList = ['C:\\']
currentDir = 'C:\\'
dirLabel, dirListBox, fileListBox = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__":
    window = Tk()
    window.title("폴더 및 파일 목록 보기")
    window.geometry('300x500')

    dirLabel = Label(window, text=currentDir)
    dirLabel.pack()

    dirListBox = Listbox(window)
    dirListBox.pack(side=LEFT, fill=BOTH, expand=1)
    dirListBox.bind('<<ListboxSelect>>', clickListBox)

    fileListBox = Listbox(window)
    fileListBox.pack(side=RIGHT, fill=BOTH, expand=1)

    fillListBox()

    window.mainloop()
