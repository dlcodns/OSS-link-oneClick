import tkinter
import tkinter.font
import tkinter.ttk
import random

window = tkinter.Tk()
window.title("업다운 게임")
window.geometry("500x400")
window.resizable(False,False)
window["bg"]="olivedrab"

font1=tkinter.font.Font(family="맑은 고딕", size=10, weight="bold")
font2=tkinter.font.Font(family="맑은 고딕", size=15, weight="bold")
font3=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
font4=tkinter.font.Font(family="맑은 고딕", size=25, weight="bold")

ran = random.randint(1,100)
count = 0

def updown():
    global ran, count
  
    b2=tkinter.Button(window, text="게임 종료",bg="olivedrab",relief="raised",borderwidth=1,font=font2,command=exit_game)
    b2.place(x=200,y=300,width=100,height=50)
    
 
    tkinter.Label(window, text="숫자 하나를 적으세요.",bg="darkslategray",fg="white",borderwidth=2,relief="raised", font=font1).place(x=190,y=130,width=124,height=30)

    number = tkinter.StringVar()
    number_entered = tkinter.ttk.Entry(window, width=20, textvariable=number)
    number_entered.place(x=180,y=180)

    action = tkinter.Button(window, text="확인", font=font1, command=lambda:[calc(number_entered)])
    action.place(x=330,y=176)
    

            
def calc(enteredNum):
    global ran, count
    
    num = int(enteredNum.get())
     
     
     
    if count < 6 :
        if ran > num:
            if count !=5:
                tkinter.Label(window, text="up!", font=font4, bg="olivedrab",fg="white",borderwidth=2,relief="flat").place(x=168,y=220,width=170,height=50)
        elif ran < num:
            if count !=5:
                tkinter.Label(window, text="down!", font=font4, bg="olivedrab",fg="white",borderwidth=2,relief="flat").place(x=167,y=220,width=170,height=50)
        elif ran == num:
            win = random.randint(1,3)
            if win == 1:
                tkinter.Label(window, text="딩동댕~ 정답!", font=font4, bg="olivedrab",fg="white",borderwidth=2,relief="flat").place(x=190,y=220,width=124,height=30)
            if win == 2:
                tkinter.Label(window, text="운이 좋으시네요. :)", font=font4, bg="olivedrab",fg="white",borderwidth=2,relief="flat").place(x=190,y=220,width=124,height=30)
            if win == 3:
                tkinter.Label(window, text="올ㅋ",bg="olivedrab", font=font4, fg="white",borderwidth=2,relief="flat").place(x=190,y=220,width=124,height=30)
        count= count+1
        if count == 6 :
            tkinter.Label(window, text="정답은 ran이었습니다! 메롱", font=font4, bg="olivedrab",fg="white",borderwidth=2,relief="flat").place(x=160,y=220,width=200,height=30)


def exit_game():
    window.destroy()

    
b1=tkinter.Button(window, text="게임 시작",bg="olivedrab",relief="raised",borderwidth=1,font=font2,command=updown)
b1.place(x=200,y=300,width=100,height=50)
    
window.mainloop()
