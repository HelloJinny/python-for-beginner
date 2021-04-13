from tkinter import *
window = Tk()

label1 = Label(window, text="Python을")
label2 = Label(window, text="열심히", font=("나눔고딕", 30), fg="blue")
label3 = Label(window, text="공부 중입니다.", bg="magenta",
               width=100, height=10, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
