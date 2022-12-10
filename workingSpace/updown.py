import tkinter
import tkinter.font
import tkinter.ttk
import random
import os
import sys

#해야 할 것
#if 끝나고 라벨 프린트하기-> loop 사진에 지금까지 경로 담기(완료)
# 정답이랑 오답 이쁘게 프린트하기, 또는 사진으로 만들기(시간이 되면)(안해도 이쁨(아마도))

#윈도우 창 설정
window = tkinter.Tk()
window.title("업다운 게임")
window.geometry("500x400")
window.resizable(False,False)
window["bg"]="#d4e157"

#폰트 크기 설정
font=tkinter.font.Font(family="맑은 고딕", size=9, weight="bold")
font1=tkinter.font.Font(family="맑은 고딕", size=10, weight="bold")
font2=tkinter.font.Font(family="맑은 고딕", size=15, weight="bold")
font3=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
font4=tkinter.font.Font(family="맑은 고딕", size=25, weight="bold")

#난수 설정
ran = random.randint(1,100)
count = 0

#게임 진행 함수
def updown():
    #TcoverImgPath=resource_path("src/Tcover.png")
    #TcoverImg=tkinter.PhotoImage(file = TcoverImgPath)
    #TcoverImglabel=tkinter.Label(window, image=TcoverImg, relief="flat", bg="#d4e157").place(x=77.5,y=80)
    #ScoverImgPath=resource_path("src/Scover.png")
    #ScoverImg=tkinter.PhotoImage(file = ScoverImgPath)
    #ScoverImglabel=tkinter.Label(window, image=ScoverImg, relief="flat", bg="#d4e157").place(x=164,y=230,width=175)
    #CcoverImgPath=resource_path("src/Ccover.png")
    #CcoverImg=tkinter.PhotoImage(file = CcoverImgPath)
    #CcoverImglabel=tkinter.Label(window, image=CcoverImg, relief="flat", bg="#d4e157").place(x=164,y=230)
    #loopImgPath=resource_path("src/loop.png")
    #loopImg=tkinter.PhotoImage(file = loopImgPath)
    #loopImglabel=tkinter.Label(window, image=loopImg, relief="flat", bg="#385723").place(x=30,y=40)
    #titleCover=tkinter.Label(window, bg="#d4e157",relief="flat").place(x=77,y=80,width=348,height=96)
    #startCover=tkinter.Label(window, bg="#d4e157",relief="flat").place(x=164,y=230,width=170,height=60)
    #calcCover=tkinter.Label(window, bg="#d4e157",relief="flat").place(x=164,y=230,width=170,height=60)
    #loopImg=tkinter.Label(window, bg="#385723",relief="flat").place(x=35,y=40,width=171,height=201)
    playgroundLoopImglabel=tkinter.Label(window, image=playgroundLoopImg,relief="flat", bg="#d4e157").place(x=-2,y=1)
        
    global ran, count
    
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", bg="#385723", command=updown).place(x=125,y=271)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", bg="#385723", command=exit_game).place(x=277,y=271)
    
    #b1=tkinter.Button(window, text="재시작",bg="#385723",relief="flat",borderwidth=1,font=font2,command=updown)
    #b1.place(x=120,y=271,width=100,height=50)
    #b2=tkinter.Button(window, text="게임 종료",bg="#385723",relief="flat",borderwidth=1,font=font2,command=exit_game)
    #b2.place(x=280,y=271,width=100,height=50)
    
    tkinter.Label(window, text="숫자 하나를 적으세요.",bg="darkslategray",fg="white",borderwidth=2,relief="raised", font=font1).place(x=281,y=70,width=140,height=30)

    tkinter.Label(window, text="-- 범위 1~100 --",bg="#d4e157",fg="black",relief="flat", font=font).place(x=274,y=102,width=150,height=20)
    
    number = tkinter.StringVar()
    number_entered = tkinter.ttk.Entry(window, font=font1, width=18, textvariable=number)
    number_entered.place(x=275,y=130)

    action = tkinter.Button(window, text="확인", font=font1, command=lambda:[calc(number_entered)])
    action.place(x=431,y=126)
    
#업다운 비교 함수          
def calc(enteredNum):
    global ran, count
    
    num = int(enteredNum.get())
     
    if (1<=num<=100) and count < 6 :
        if ran > num:
            if count !=5:
                tkinter.Label(window, text="up!", font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=273,y=170,width=170,height=50)
        elif ran < num:
            if count !=5:
                tkinter.Label(window, text="down!", font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=273,y=170,width=170,height=50)
        elif ran == num:
            win = random.randint(1,3)
            if win == 1:
                tkinter.Label(window, text="딩동댕~ 정답!", font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=273,y=170,width=170,height=50)
            if win == 2:
                tkinter.Label(window, text="운이 좋으시네요. :)", font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=273,y=170,width=170,height=50)
            if win == 3:
                tkinter.Label(window, text="올ㅋ",bg="#d4e157", font=font4, fg="white",borderwidth=2,relief="flat").place(x=273,y=170,width=170,height=50)
        count= count+1
        msg = "땡! 정답은 " + str(ran) + " 입니다."
        if count == 6 :
            tkinter.Label(window, text=msg, font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=240,y=250,width=200,height=30)
    else:
        updown()
        
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
playgroundImgPath=resource_path("src/playground.png")
playgroundImg=tkinter.PhotoImage(file = playgroundImgPath)
playgroundImglabel=tkinter.Label(window, image=playgroundImg, relief="flat", bg="#d4e157").place(x=-2,y=1)
titleImgPath=resource_path("src/title.png")
titleImg=tkinter.PhotoImage(file = titleImgPath)
titleImglabel=tkinter.Label(window, image=titleImg, relief="flat", bg="#d4e157").place(x=77.5,y=80)
playgroundLoopImgPath=resource_path("src/playgroundLoop.png")
playgroundLoopImg=tkinter.PhotoImage(file = playgroundLoopImgPath)


#버튼 이미지
startImgPath=resource_path("src/start.png")
startImg=tkinter.PhotoImage(file = startImgPath)
restartImgPath=resource_path("src/restart.png")
restartImg=tkinter.PhotoImage(file = restartImgPath)
exitImgPath=resource_path("src/exit.png")
exitImg=tkinter.PhotoImage(file = exitImgPath)

#시작 버튼 위치
startBtn=tkinter.Button(window, image=startImg ,relief="flat", bg="#385723", command=updown).place(x=163.5,y=230)

window.mainloop()
