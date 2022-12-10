import tkinter
import tkinter.font
import tkinter.ttk
import random
import os
import sys

#배열에 집어넣기
#-오류 없길-
#제비 개수 라벨지 만들기
#제비 나열해서 버튼 만들고 이벤트 열기

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
def jebi():
    jgrassLoopImglabel=tkinter.Label(window, image=jgrassLoopImg, relief="flat", bg="light yellow").place(x=-23,y=-41)

    #startCover=tkinter.Label(window, bg="light yellow",relief="flat").place(x=164,y=270,width=170,height=62)
    #jtitleCover=tkinter.Label(window, bg="light yellow",relief="flat").place(x=150,y=160,width=200,height=62)
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", command=jebi).place(x=125,y=285)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", command=exit_game).place(x=277,y=285)
    
    tkinter.Label(window, text="-- 2~8명만 가능합니다. --",bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=150,y=145,width=200)
    
    #tkinter.Label(window, image=jnum,bg="darkslategray",fg="white",borderwidth=2,relief="raised").place(x=110,y=80,width=80,height=30)
    tkinter.Label(window, text="인원 수 입력", relief="ridge", font=font2,bg="#FAD2AA",fg="black").place(x=90,y=87,width=160)
    
    number = tkinter.StringVar()
    number_entered = tkinter.ttk.Entry(window, font=font2, width=10, textvariable=number)
    number_entered.place(x=260,y=87)
    
    
    action = tkinter.Button(window, text="확인", font=font1, command=lambda:[input(action, number_entered)])
    action.place(x=395,y=91)

#입력과 배열 설정
def input(action, enteredNum):
    action.config(state="disabled")
    
    num = int(enteredNum.get())
    if num>8 or num<2 :
        jebi()
           
    a = []
    if num<=8 and num>=2 :
        tkinter.Label(window, text="-- 제비마다 역할을 정해주세요. --",bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=150,y=145,width=200)
    
    #입력창 설정
    jebi_1 = tkinter.StringVar()
    jebi_1_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_1)
    jebi_2 = tkinter.StringVar()
    jebi_2_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_2)
    jebi_3 = tkinter.StringVar()
    jebi_3_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_3)
    jebi_4 = tkinter.StringVar()
    jebi_4_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_4)
    jebi_5 = tkinter.StringVar()
    jebi_5_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_5)
    jebi_6 = tkinter.StringVar()
    jebi_6_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_6)
    jebi_7 = tkinter.StringVar()
    jebi_7_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_7)
    jebi_8 = tkinter.StringVar()
    jebi_8_entered = tkinter.ttk.Entry(window, font=font1, width=6, textvariable=jebi_8)

    #인원 수에 따라 라벨 개수와 형태를 다르게 함.
    if num>=2 and num<=4:
        for i in range(0,num):
            tkinter.Label(window, text=i+1, relief="flat",font=font3, bg="darkslategray",fg="white").place(x=80+i*90,y=190) 
        jebi_1_entered.place(x=105,y=208)
        jebi_2_entered.place(x=195,y=208)
        if num>=3:
            jebi_3_entered.place(x=285,y=208)   
        if num>=4:
            jebi_4_entered.place(x=375,y=208) 
             
    if num>4 and num<=8:
        for i in range(0,4):
            tkinter.Label(window, text=i+1, relief="flat",font=font3, bg="darkslategray",fg="white").place(x=80+i*90,y=170,height=33)
        for i in range(4,num):
            tkinter.Label(window, text=i+1, relief="flat",font=font3, bg="darkslategray",fg="white").place(x=80+(i-4)*90,y=210,height=33)
        jebi_1_entered.place(x=105,y=180)
        jebi_2_entered.place(x=195,y=180)
        jebi_3_entered.place(x=285,y=180)
        jebi_4_entered.place(x=375,y=180)
        if num>=5:
            jebi_5_entered.place(x=105,y=220)
        if num>=6:
            jebi_6_entered.place(x=195,y=220)
        if num>=7:
            jebi_7_entered.place(x=285,y=220)
        if num==8:
            jebi_8_entered.place(x=375,y=220) 
            
    #위의 모든 입력창들이 확인 한번에 입력되게 함. 확인 후 shake 호출
    action2 = tkinter.Button(window, text="확인", font=font1, command=lambda:[shake(a,num, jebi_1_entered,jebi_2_entered,jebi_3_entered,jebi_4_entered,jebi_5_entered,jebi_6_entered,jebi_7_entered,jebi_8_entered)])
    action2.place(x=395,y=142)


#배열 만들기, 랜덤 셔플 반복문, 최종 출력 함수
def shake(a,num,enteredOne,enteredTwo,enteredThree,enteredFour,enteredFive,enteredSix,enteredSeven,enteredEight):
   
    num=num
    
    a.append(enteredOne.get())
    a.append(enteredTwo.get())
    if num>=3:
        a.append(enteredThree.get())
    if num>=4:
        a.append(enteredFour.get())
    if num>=5:
        a.append(enteredFive.get())
    if num>=6:
        a.append(enteredSix.get())
    if num>=7:
        a.append(enteredSeven.get())
    if num==8:
        a.append(enteredEight.get())
        
    #난수 인덱스의 배열과 (0,num-2)의 배열을 바꾸는 과정
    for i in range(0,num-2):
        rand=random.randint
        ran=rand%(num-i)+i
        
        temp=a[i]
        a[i]=a[ran]
        a[ran]=temp
    
    #최종 출력
    for i in range(0, num-1):
        print('제비',i+1,'역할',a[i])

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
jstartBtn=tkinter.Button(window, image=jstartImg ,relief="flat",bg="light yellow", command=jebi).place(x=174,y=270)

window.mainloop()
