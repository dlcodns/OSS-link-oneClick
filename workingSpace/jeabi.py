import tkinter
import tkinter.font
import tkinter.ttk
import random
import os
import sys

#윈도우 창 설정
window = tkinter.Tk()
window.title("제비뽑기")
window.geometry("500x400")
window.resizable(False,False)
window["bg"]="light yellow"

#폰트 크기 설정
font1=tkinter.font.Font(family="맑은 고딕", size=10, weight="bold")
font2=tkinter.font.Font(family="맑은 고딕", size=15, weight="bold")
font3=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
font4=tkinter.font.Font(family="맑은 고딕", size=25, weight="bold")

#제비뽑기 진행 함수
def jeabi():
    jgrassLoopImglabel=tkinter.Label(window, image=jgrassLoopImg, relief="flat", bg="light yellow").place(x=-23,y=-41)

    #startCover=tkinter.Label(window, bg="light yellow",relief="flat").place(x=164,y=270,width=170,height=62)
    #jtitleCover=tkinter.Label(window, bg="light yellow",relief="flat").place(x=150,y=160,width=200,height=62)
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", command=jeabi).place(x=125,y=285)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", command=exit_game).place(x=277,y=285)
    #재시작, 종료 버튼 만들기(완료)
    
    #tkinter.Label(window, image=jnum,bg="darkslategray",fg="white",borderwidth=2,relief="raised").place(x=110,y=80,width=80,height=30)
    tkinter.Label(window, text="인원 수 입력", relief="ridge", font=font2,bg="#FAD2AA",fg="black").place(x=90,y=87,width=160)
    
    number = tkinter.StringVar()
    number_entered = tkinter.ttk.Entry(window, font=font2, width=10, textvariable=number)
    number_entered.place(x=260,y=87)
    
    action = tkinter.Button(window, text="확인", font=font1, command=lambda:[input(action, number_entered)])
    action.place(x=395,y=91)
    
    #인원수num 입력하기(완료)
    #2~8명 제한
    #a배열 만들기
    #역할 정하기 라벨(나열 후 전체 확인)
    #
    #shake(num)
    #최종 제비들 나열
    #클릭하면 역할 보이기
    #

#입력과 배열 설정
def input(action, enteredNum):
    action.config(state="disabled")
    
    num = int(enteredNum.get())
    if num>8 or num<2 :
        print('2~8명만 가능합니다.')
        jeabi()
           
    a = []
    
    tkinter.Label(window, text="-- 제비마다 역할을 정해주세요. --",bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=150,y=145,width=200)
    
    jeabi_1 = tkinter.StringVar()
    jeabi_1_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_2 = tkinter.StringVar()
    jeabi_2_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_3 = tkinter.StringVar()
    jeabi_3_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_4 = tkinter.StringVar()
    jeabi_4_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_5 = tkinter.StringVar()
    jeabi_5_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_6 = tkinter.StringVar()
    jeabi_6_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_7 = tkinter.StringVar()
    jeabi_7_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)
    jeabi_8 = tkinter.StringVar()
    jeabi_8_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jeabi_1)

    
    if num<=4:
        for i in range(0,num):
            tkinter.Label(window, text=i+1, relief="flat",font=font3, bg="darkslategray",fg="white").place(x=80+i*90,y=190) 
        jeabi_1_entered.place(x=105,y=208)
        jeabi_2_entered.place(x=195,y=208)
        if num>=3:
            jeabi_3_entered.place(x=285,y=208)
        if num>=4:
            jeabi_4_entered.place(x=375,y=208)   
                      
    if num>4 and num<=8:
        for i in range(0,4):
            tkinter.Label(window, text=i+1, relief="flat",font=font3, bg="darkslategray",fg="white").place(x=80+i*90,y=170,height=33)
        for i in range(4,num):
            tkinter.Label(window, text=i+1, relief="flat",font=font3, bg="darkslategray",fg="white").place(x=80+(i-4)*90,y=210,height=33)
        jeabi_1_entered.place(x=105,y=180)
        jeabi_2_entered.place(x=195,y=180)
        jeabi_3_entered.place(x=285,y=180)
        jeabi_4_entered.place(x=375,y=180)         
        if num>=5:
            jeabi_5_entered.place(x=105,y=220)
        if num>=6:
            jeabi_6_entered.place(x=195,y=220)  
        if num>=7:
            jeabi_7_entered.place(x=285,y=220)
        if num==8:
            jeabi_8_entered.place(x=375,y=220) 
  
     
    for i in range(0,num):
        print('제비',i+1,' = ')
        input(a[i])
        
    for j in range(0,num-1):
        print('제비',i+1,' 역할: ',a[i])
    #for i in range(0,):

#난수 설정
#def shake():

#게임을 나가는 함수
def exit_game():
    window.destroy()

# exe 제작을 위한 이미지 경로 설정 함수
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#기본 이미지
#jtitleImgPath=resource_path("src/jtitle.png")
#jtitleImg=tkinter.PhotoImage(file = jtitleImgPath)
#jtitleImglabel=tkinter.Label(window, image=jtitleImg, relief="flat", bg="light yellow").place(x=105,y=80)
jgrassImgPath=resource_path("src/jgrass.png")
jgrassImg=tkinter.PhotoImage(file = jgrassImgPath)
jgrassImglabel=tkinter.Label(window, image=jgrassImg, relief="flat", bg="light yellow").place(x=-23,y=-41)

jgrassLoopImgPath=resource_path("src/jgrassLoop.png")
jgrassLoopImg=tkinter.PhotoImage(file = jgrassLoopImgPath)
jnumImgPath=resource_path("src/jnum.png")
jnumImg=tkinter.PhotoImage(file = jnumImgPath)

#버튼 이미지
jstartImgPath=resource_path("src/jstart.png")
jstartImg=tkinter.PhotoImage(file = jstartImgPath)
restartImgPath=resource_path("src/restart.png")
restartImg=tkinter.PhotoImage(file = restartImgPath)
exitImgPath=resource_path("src/exit.png")
exitImg=tkinter.PhotoImage(file = exitImgPath)

#시작 버튼 위치
jstartBtn=tkinter.Button(window, image=jstartImg ,relief="flat",bg="light yellow", command=jeabi).place(x=174,y=270)

window.mainloop()
