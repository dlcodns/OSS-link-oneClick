from tkinter import *
import tkinter.font
import tkinter.ttk
import random
import os
import sys

count = 0
cnt=0
answer = False # 정답 맞췃는지 확인

def playUpDown() :

    #윈도우 창 설정
    window = Toplevel()
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


    #게임 진행 함수
    def updown(isReset=False):
        playgroundLoopImglabel=Label(window, image=playgroundLoopImg,relief="flat", bg="#d4e157").place(x=-2,y=1)

        global count, answer
        count =0 
        cnt =0
        answer = False
        
        homeBtn=Button(window, image=homeImg ,relief="flat", bg="gold", command=main).place(x=440,y=340)
        restartBtn=Button(window, image=restartImg ,relief="flat", bg="#385723", command=updown).place(x=125,y=271)
        exitBtn=Button(window, image=exitImg ,relief="flat", bg="#385723", command=exit_game).place(x=277,y=271)
        
        ran = random.randint(1,100)
        Label(window, text="숫자 하나를 적으세요.",bg="darkslategray",fg="white",borderwidth=2,relief="raised", font=font1).place(x=281,y=70,width=140,height=30)

        Label(window, text="-- 범위 1~100 --",bg="#d4e157",fg="black",relief="flat", font=font).place(x=274,y=102,width=150,height=20)
        Label(window, text="-- 6번의 기회 --",bg="#FFFF89",fg="black",relief="flat", font=font).place(x=90,y=47,width=65,height=20)

        if isReset:
            Label(window, text="범위는 1~100입니다.", font=font2, bg="#d4e157",fg="black",borderwidth=2,relief="flat").place(x=265,y=170,height=50)

        number = StringVar()
        number_entered = Entry(window, font=font1, width=18, textvariable=number, justify="center")
        number_entered.place(x=275,y=130)

        action = Button(window, text="확인", font=font1, command=lambda:[calc(number_entered,ran)])
        action.place(x=431,y=126)
        
    #업다운 비교 함수          
    def calc(enteredNum,ran):
        global count, cnt, answer
        
        rowNum = enteredNum.get()
        if rowNum == "" and count == 6:
            tkinter.Label(window, text="게임이 종료되었습니다.", font=font2, bg="#d4e157",fg="black",borderwidth=2,relief="flat").place(x=263,y=170,height=50)
        elif rowNum == "":
            tkinter.Label(window, text="숫자를 입력하세요.", font=font2, bg="#d4e157",fg="black",borderwidth=2,relief="flat").place(x=265,y=170,height=50)
        else :
            num = int(rowNum)     
            if (not answer) and (1<=num<=100) and count < 6 :
                if ran > num:
                    if count !=5:
                        enteredNum.delete(0,END)
                        tkinter.Label(window, text="up!", font=font4, bg="#d4e157",fg="light yellow",borderwidth=2,relief="flat").place(x=250,y=170,width=210,height=50)
                elif ran < num:
                    if count !=5:
                        enteredNum.delete(0,END)
                        tkinter.Label(window, text="down!", font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=250,y=170,width=210,height=50)
                elif ran == num:
                    enteredNum.delete(0,END)
                    cnt = 0
                    win = random.randint(1,6)
                    if win == 1 and count != 1 and count != 0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text="딩동댕~ 정답!", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=243,y=170,width=200,height=50)
                    if win == 2 and count != 1 and count != 0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text="운이 좋으시네요. :)", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=243,y=170,width=200,height=50)
                    if win == 3 and count != 1 and count != 0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text="올ㅋ 잘하시는데요?",bg="#d4e157", font=font2, fg="blue1",borderwidth=2,relief="flat").place(x=243,y=170,width=200,height=50)
                    if win == 4 and count != 1 and count != 0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text="대단해요!", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=243,y=170,width=200,height=50)
                    if win == 5 and count != 1 and count != 0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text="ㄴㅇㄱ 굉장해엄청나!", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=243,y=170,width=210,height=50)
                    if win == 6 and count != 1 and count != 0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text="정답! 게임 한 판 더?", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=243,y=170,width=210,height=50)
                    if count==0:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text=" (((φ(◎ロ◎;)φ)))\n복권 하나 사세요!",bg="#d4e157", font=font2, fg="black",borderwidth=2,relief="flat").place(x=275,y=170,height=50)
                    if count==1:
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text=" Σ(っ °Д °;)っ\n어떻게 알았지?",bg="#d4e157", font=font2, fg="black",borderwidth=2,relief="flat").place(x=275,y=170,width=150,height=50)
                    
                    text1 = str(count+1)+" 번째 숫자 = "+str(num)
                    tkinter.Label(window, text= text1, font=font1, bg="#6A8334",fg="light yellow",borderwidth=2,relief="flat").place(x=60,y=46+(count+1)*25,width=120,height=20)

                    count=6
                    return
                text1 = str(count+1)+" 번째 숫자 = "+str(num)
                if(count<6):
                    tkinter.Label(window, text= text1, font=font1, bg="#6A8334",fg="light yellow",borderwidth=2,relief="flat").place(x=60,y=46+(count+1)*25,width=120,height=20)
                    if ran>num:
                        tkinter.Label(window, text= "↑", font=font1, bg="#6A8334",fg="red3",borderwidth=2,relief="flat").place(x=177,y=45+(count+1)*25,width=5,height=20)
                    if ran<num:
                        tkinter.Label(window, text= "↓", font=font1, bg="#6A8334",fg="blue3",borderwidth=2,relief="flat").place(x=177,y=45+(count+1)*25,width=5,height=20)

                    count= count+1
            msg1 = "정답은 "+ str(ran)+"!\n"+"또 틀렸어( Ĭ ^ Ĭ )"
            msg2 = "정답은 "+ str(ran)+"..\n"+"틀렸어요( ˃̣̣̥᷄⌓˂̣̣̥᷅ )"
            msg3 = "정답은 "+ str(ran)+"\n"+"이런 (> д <)"
            msg4 = "땡! 정답은 " + str(ran) + " 입니다."
            
            if count == 6 :
                cnt=cnt+1
                if cnt>=2:
                    cnt1 = random.randint(1,3)
                    if cnt1 == 1:
                        enteredNum.delete(0, 'end')
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text=msg1, font=font2, bg="#d4e157",fg="red3",borderwidth=2,relief="flat").place(x=253,y=170,width=195,height=50)
                    if cnt1 == 2:
                        enteredNum.delete(0, 'end')
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text=msg2, font=font2, bg="#d4e157",fg="red3",borderwidth=2,relief="flat").place(x=253,y=170,width=195,height=50)
                    if cnt1 == 3:
                        enteredNum.delete(0, 'end')
                        enteredNum.config(state='disabled')
                        tkinter.Label(window, text=msg3, font=font2, bg="#d4e157",fg="red3",borderwidth=2,relief="flat").place(x=253,y=170,width=195,height=50)
                
                if not cnt>=2:
                    enteredNum.delete(0, 'end')
                    enteredNum.config(state='disabled')
                    tkinter.Label(window, text=msg4, font=font2, bg="#d4e157",fg="red3",borderwidth=2,relief="flat").place(x=263,y=170,width=195,height=50)
                
            elif not(1 <= num <= 100):
                count=0
                updown(True)
            elif answer:
                pass

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

    def main() :
        #기본 이미지
        playgroundImgPath=resource_path("src/updown_playground.png")
        playgroundImg=PhotoImage(file = playgroundImgPath)
        playgroundImglabel=Label(window, image=playgroundImg, relief="flat", bg="#d4e157").place(x=-2,y=1)
        titleImgPath=resource_path("src/updown_title.png")
        titleImg=PhotoImage(file = titleImgPath)
        titleImglabel=Label(window, image=titleImg, relief="flat", bg="#d4e157").place(x=77.5,y=80)
        playgroundLoopImgPath=resource_path("src/updown_playgroundLoop.png")
        playgroundLoopImg=PhotoImage(file = playgroundLoopImgPath)
        
        #버튼 이미지
        startImgPath=resource_path("src/updown_start.png")
        startImg=PhotoImage(file = startImgPath)
        homeImgPath=resource_path("src/updown_home.png")
        homeImg=PhotoImage(file = homeImgPath)
        restartImgPath=resource_path("src/updown_restart.png")
        restartImg=PhotoImage(file = restartImgPath)
        exitImgPath=resource_path("src/updown_exit.png")
        exitImg=PhotoImage(file = exitImgPath)

        #시작 버튼 위치
        startBtn=Button(window, image=startImg ,relief="flat", bg="#385723", command=updown).place(x=163.5,y=230)

        window.mainloop()    

    #기본 이미지
    playgroundImgPath=resource_path("src/updown_playground.png")
    playgroundImg=PhotoImage(file = playgroundImgPath)
    playgroundImglabel=Label(window, image=playgroundImg, relief="flat", bg="#d4e157").place(x=-2,y=1)
    titleImgPath=resource_path("src/updown_title.png")
    titleImg=PhotoImage(file = titleImgPath)
    titleImglabel=Label(window, image=titleImg, relief="flat", bg="#d4e157").place(x=77.5,y=80)
    playgroundLoopImgPath=resource_path("src/updown_playgroundLoop.png")
    playgroundLoopImg=PhotoImage(file = playgroundLoopImgPath)

    #버튼 이미지
    startImgPath=resource_path("src/updown_start.png")
    startImg=PhotoImage(file = startImgPath)
    homeImgPath=resource_path("src/updown_home.png")
    homeImg=PhotoImage(file = homeImgPath)
    restartImgPath=resource_path("src/updown_restart.png")
    restartImg=PhotoImage(file = restartImgPath)
    exitImgPath=resource_path("src/updown_exit.png")
    exitImg=PhotoImage(file = exitImgPath)

    #시작 버튼 위치
    startBtn=Button(window, image=startImg ,relief="flat", bg="#385723", command=updown).place(x=163.5,y=230)

    window.mainloop()
