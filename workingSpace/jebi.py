import tkinter
import tkinter.font
import tkinter.ttk
import random
import os
import sys
from tkinter import *

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

    homeBtn=tkinter.Button(window, image=homeImg ,relief="flat", bg="gold", command=main).place(x=440,y=340)
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", command=jebi).place(x=125,y=285)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", command=exit_game).place(x=277,y=285)
    
    tkinter.Label(window, text="-- 2~8명만 가능합니다. --",bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=150,y=145,width=200)
    
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
        return
           
    a = []
    if num<=8 and num>=2 :
        tkinter.Label(window, text="-- 빈칸도 입력 가능합니다. --",bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=162.5,y=245,width=175, height=20)
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
    action2 = tkinter.Button(window, text="확인", font=font1, command=lambda:[shake(action2,a,num, jebi_1_entered,jebi_2_entered,jebi_3_entered,jebi_4_entered,jebi_5_entered,jebi_6_entered,jebi_7_entered,jebi_8_entered)])
    action2.place(x=395,y=142)


#배열 만들기, 랜덤 셔플 반복문, 최종 출력 함수
def shake(action2,a,num,enteredOne,enteredTwo,enteredThree,enteredFour,enteredFive,enteredSix,enteredSeven,enteredEight):

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
    for i in range(0,num-1):
        rand=random.randint(0, 10000)
        ran=rand%(num-i)+i
        
        temp=a[i]
        a[i]=a[ran]
        a[ran]=temp
    
    printer(a,num)
    
    #잘 됐는지 터미널에서 확안
    for i in range(0, num):
        print('제비',i+1,'역할',a[i])
        
#제비버튼을 출력하는 함수
def printer(a,num):
    num=num
    a=a
    jgrassLoopImglabel=tkinter.Label(window, image=jgrassLoopImg, relief="flat", bg="light yellow").place(x=-23,y=-41)
    homeBtn=tkinter.Button(window, image=homeImg ,relief="flat", bg="gold", command=main).place(x=440,y=340)
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", command=jebi).place(x=125,y=285)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", command=exit_game).place(x=277,y=285)
    tkinter.Label(window, text="-- 한 사람당 하나씩 뽑아보세요. --",bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=150,y=45,width=200)
    openBtn=tkinter.Button(window,text="전체 공개",relief="ridge", font=font1,bg="#FAD2AA",fg="black",command=lambda:[all(a)]).place(x=200,y=233,width=100)
    button1=tkinter.Button(window, image=jebi1Img,relief="flat",bg="#FDEDA6",command=lambda:[open1(a)]).place(x=90+18,y=70+3)
    button2=tkinter.Button(window, image=jebi2Img,relief="flat",bg="#FDEDA6",command=lambda:[open2(a)]).place(x=160+18,y=70+3)
    if num>=3:
        button3=tkinter.Button(window, image=jebi3Img,relief="flat",bg="#FDEDA6",command=lambda:[open3(a)]).place(x=230+18,y=70+3)
    if num>=4:    
        button4=tkinter.Button(window, image=jebi4Img,relief="flat",bg="#FDEDA6",command=lambda:[open4(a)]).place(x=300+18,y=70+3)
    if num>=5:    
        button5=tkinter.Button(window, image=jebi5Img,relief="flat",bg="#FDEDA6",command=lambda:[open5(a)]).place(x=90+18,y=149+3)
    if num>=6:    
        button6=tkinter.Button(window, image=jebi6Img,relief="flat",bg="#FDEDA6",command=lambda:[open6(a)]).place(x=160+18,y=149+3)
    if num>=7:    
        button7=tkinter.Button(window, image=jebi7Img,relief="flat",bg="#FDEDA6",command=lambda:[open7(a)]).place(x=230+18,y=149+3)
    if num==8:    
        button8=tkinter.Button(window, image=jebi8Img,relief="flat",bg="#FDEDA6",command=lambda:[open8(a)]).place(x=300+18,y=149+3)
    
def all(a):
    a=a
    open1(a)
    open2(a) 
    open3(a)    
    open4(a)       
    open5(a)    
    open6(a)    
    open7(a)    
    open8(a)    

def open1(a):
    a=a
    text1="제비 1\n\n"+a[0]
    tkinter.Label(window,text= text1,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=108,y=73,width=70, height=81)  
    return

def open2(a):
    a=a
    text2="제비 2\n\n"+a[1]
    tkinter.Label(window,text= text2,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=178,y=73,width=70, height=81)  
    return
    
def open3(a):
    a=a
    text3="제비 3\n\n"+a[2]
    tkinter.Label(window,text= text3,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=248,y=73,width=70, height=81)  
    return

def open4(a):
    a=a
    text4="제비 4\n\n"+a[3]
    tkinter.Label(window,text= text4,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=318,y=73,width=70, height=81)  
    return

def open5(a):
    a=a
    text5="제비 5\n\n"+a[4]
    tkinter.Label(window,text= text5,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=108,y=154,width=70, height=81)  
    return

def open6(a):
    a=a
    text6="제비 6\n\n"+a[5]
    tkinter.Label(window,text= text6,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=178,y=154,width=70, height=81)  
    return

def open7(a):
    a=a
    text7="제비 7\n\n"+a[6]
    tkinter.Label(window,text= text7,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=248,y=154,width=70, height=81)  
    return

def open8(a):
    a=a
    text8="제비 8\n\n"+a[7]
    tkinter.Label(window,text= text8,bg="#FDEDA6",fg="black",relief="flat", font=font1).place(x=318,y=154,width=70, height=81)  
    return

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

def main():
    #기본 이미지
    jgrassImgPath=resource_path("src/jgrass.png")
    jgrassImg=tkinter.PhotoImage(file= jgrassImgPath)
    jgrassImglabel=tkinter.Label(window, image=jgrassImg, relief="flat", bg="light yellow").place(x=-23,y=-41)

    jgrassLoopImgPath=resource_path("src/jgrassLoop.png")
    jgrassLoopImg=tkinter.PhotoImage(file = jgrassLoopImgPath)
    jnumImgPath=resource_path("src/jnum.png")
    jnumImg=tkinter.PhotoImage(file = jnumImgPath)

    #버튼 이미지
    jstartImgPath=resource_path("src/jstart.png")
    jstartImg=tkinter.PhotoImage(file = jstartImgPath)
    homeImgPath=resource_path("src/updown_home.png")
    homeImg=tkinter.PhotoImage(file = homeImgPath)
    restartImgPath=resource_path("src/restart.png")
    restartImg=tkinter.PhotoImage(file = restartImgPath)
    exitImgPath=resource_path("src/exit.png")
    exitImg=tkinter.PhotoImage(file = exitImgPath)
    jebi1ImgPath=resource_path("src/jebi_jebi1.png")
    jebi1Img=tkinter.PhotoImage(file = jebi1ImgPath)
    jebi2ImgPath=resource_path("src/jebi_jebi2.png")
    jebi2Img=tkinter.PhotoImage(file = jebi2ImgPath)
    jebi3ImgPath=resource_path("src/jebi_jebi3.png")
    jebi3Img=tkinter.PhotoImage(file = jebi3ImgPath)
    jebi4ImgPath=resource_path("src/jebi_jebi4.png")
    jebi4Img=tkinter.PhotoImage(file = jebi4ImgPath)
    jebi5ImgPath=resource_path("src/jebi_jebi5.png")
    jebi5Img=tkinter.PhotoImage(file = jebi5ImgPath)
    jebi6ImgPath=resource_path("src/jebi_jebi6.png")
    jebi6Img=tkinter.PhotoImage(file = jebi6ImgPath)
    jebi7ImgPath=resource_path("src/jebi_jebi7.png")
    jebi7Img=tkinter.PhotoImage(file = jebi7ImgPath)
    jebi8ImgPath=resource_path("src/jebi_jebi8.png")
    jebi8Img=tkinter.PhotoImage(file = jebi8ImgPath)

    #시작 버튼 위치
    jstartBtn=tkinter.Button(window, image=jstartImg ,relief="flat",bg="light yellow", command=jebi).place(x=174,y=270)

    window.mainloop()

if __name__ == '__main__':
    #기본 이미지
    jgrassImgPath=resource_path("src/jgrass.png")
    jgrassImg=tkinter.PhotoImage(file= jgrassImgPath)
    jgrassImglabel=tkinter.Label(window, image=jgrassImg, relief="flat", bg="light yellow").place(x=-23,y=-41)

    jgrassLoopImgPath=resource_path("src/jgrassLoop.png")
    jgrassLoopImg=tkinter.PhotoImage(file = jgrassLoopImgPath)
    jnumImgPath=resource_path("src/jnum.png")
    jnumImg=tkinter.PhotoImage(file = jnumImgPath)

    #버튼 이미지
    jstartImgPath=resource_path("src/jstart.png")
    jstartImg=tkinter.PhotoImage(file = jstartImgPath)
    homeImgPath=resource_path("src/updown_home.png")
    homeImg=tkinter.PhotoImage(file = homeImgPath)
    restartImgPath=resource_path("src/restart.png")
    restartImg=tkinter.PhotoImage(file = restartImgPath)
    exitImgPath=resource_path("src/exit.png")
    exitImg=tkinter.PhotoImage(file = exitImgPath)
    jebi1ImgPath=resource_path("src/jebi_jebi1.png")
    jebi1Img=tkinter.PhotoImage(file = jebi1ImgPath)
    jebi2ImgPath=resource_path("src/jebi_jebi2.png")
    jebi2Img=tkinter.PhotoImage(file = jebi2ImgPath)
    jebi3ImgPath=resource_path("src/jebi_jebi3.png")
    jebi3Img=tkinter.PhotoImage(file = jebi3ImgPath)
    jebi4ImgPath=resource_path("src/jebi_jebi4.png")
    jebi4Img=tkinter.PhotoImage(file = jebi4ImgPath)
    jebi5ImgPath=resource_path("src/jebi_jebi5.png")
    jebi5Img=tkinter.PhotoImage(file = jebi5ImgPath)
    jebi6ImgPath=resource_path("src/jebi_jebi6.png")
    jebi6Img=tkinter.PhotoImage(file = jebi6ImgPath)
    jebi7ImgPath=resource_path("src/jebi_jebi7.png")
    jebi7Img=tkinter.PhotoImage(file = jebi7ImgPath)
    jebi8ImgPath=resource_path("src/jebi_jebi8.png")
    jebi8Img=tkinter.PhotoImage(file = jebi8ImgPath)

    #시작 버튼 위치
    jstartBtn=tkinter.Button(window, image=jstartImg ,relief="flat",bg="light yellow", command=jebi).place(x=174,y=270)

    window.mainloop()
