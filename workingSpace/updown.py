import tkinter
import tkinter.font
import tkinter.ttk
import random
import os
import sys

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


count = 0
answer = False # 정답 맞췃는지 확인

#게임 진행 함수
def updown(isReset=False):
    playgroundLoopImglabel=tkinter.Label(window, image=playgroundLoopImg,relief="flat", bg="#d4e157").place(x=-2,y=1)

    global count, answer
    count =0 
    answer = False
    
    homeBtn=tkinter.Button(window, image=homeImg ,relief="flat", bg="gold", command=main).place(x=440,y=340)
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", bg="#385723", command=updown).place(x=125,y=271)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", bg="#385723", command=exit_game).place(x=277,y=271)
    
    ran = random.randint(1,100)
    tkinter.Label(window, text="숫자 하나를 적으세요.",bg="darkslategray",fg="white",borderwidth=2,relief="raised", font=font1).place(x=281,y=70,width=140,height=30)

    tkinter.Label(window, text="-- 범위 1~100 --",bg="#d4e157",fg="black",relief="flat", font=font).place(x=274,y=102,width=150,height=20)
    tkinter.Label(window, text="-- 6번의 기회 --",bg="#FFFF89",fg="black",relief="flat", font=font).place(x=90,y=47,width=65,height=20)

    if isReset:
        tkinter.Label(window, text="범위는 1~100입니다.", font=font2, bg="#d4e157",fg="black",borderwidth=2,relief="flat").place(x=265,y=170,height=50)

    number = tkinter.StringVar()
    number_entered = tkinter.ttk.Entry(window, font=font1, width=18, textvariable=number)
    number_entered.place(x=275,y=130)

    action = tkinter.Button(window, text="확인", font=font1, command=lambda:[calc(number_entered,ran)])
    action.place(x=431,y=126)
    
#업다운 비교 함수          
def calc(enteredNum,ran):
    global count, answer
    
    num = int(enteredNum.get())
    
    print(count, ran) #터미널로 미리 알고 테스트 해보고자 씀!
    
    if (not answer) and (1<=num<=100) and count < 6 :
        if ran > num:
            if count !=5:
                tkinter.Label(window, text="up!", font=font4, bg="#d4e157",fg="light yellow",borderwidth=2,relief="flat").place(x=263,y=170,width=200,height=50)
        elif ran < num:
            if count !=5:
                tkinter.Label(window, text="down!", font=font4, bg="#d4e157",fg="white",borderwidth=2,relief="flat").place(x=263,y=170,width=200,height=50)
        elif ran == num:
            win = random.randint(1,3)
            if win == 1:
                tkinter.Label(window, text="딩동댕~ 정답!", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=263,y=170,width=200,height=50)
            if win == 2:
                tkinter.Label(window, text="운이 좋으시네요. :)", font=font2, bg="#d4e157",fg="blue1",borderwidth=2,relief="flat").place(x=263,y=170,width=200,height=50)
            if win == 3:
                tkinter.Label(window, text="올ㅋ",bg="#d4e157", font=font2, fg="blue1",borderwidth=2,relief="flat").place(x=263,y=170,width=200,height=50)
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
        
        msg = "땡! 정답은 " + str(ran) + " 입니다."
        if count == 6 :
            tkinter.Label(window, text=msg, font=font2, bg="#d4e157",fg="red3",borderwidth=2,relief="flat").place(x=263,y=170,width=195,height=50)
            
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

def main():
    #기본 이미지
    playgroundImgPath=resource_path("src/updown_playground.png")
    playgroundImg=tkinter.PhotoImage(file = playgroundImgPath)
    playgroundImglabel=tkinter.Label(window, image=playgroundImg, relief="flat", bg="#d4e157").place(x=-2,y=1)
    titleImgPath=resource_path("src/updown_title.png")
    titleImg=tkinter.PhotoImage(file = titleImgPath)
    titleImglabel=tkinter.Label(window, image=titleImg, relief="flat", bg="#d4e157").place(x=77.5,y=80)
    playgroundLoopImgPath=resource_path("src/updown_playgroundLoop.png")
    playgroundLoopImg=tkinter.PhotoImage(file = playgroundLoopImgPath)

    #버튼 이미지
    startImgPath=resource_path("src/updown_start.png")
    startImg=tkinter.PhotoImage(file = startImgPath)
    homeImgPath=resource_path("src/updown_home.png")
    homeImg=tkinter.PhotoImage(file = homeImgPath)
    restartImgPath=resource_path("src/updown_restart.png")
    restartImg=tkinter.PhotoImage(file = restartImgPath)
    exitImgPath=resource_path("src/updown_exit.png")
    exitImg=tkinter.PhotoImage(file = exitImgPath)

    #시작 버튼 위치
    startBtn=tkinter.Button(window, image=startImg ,relief="flat", bg="#385723", command=updown).place(x=163.5,y=230)

    window.mainloop()

if __name__ == '__main__':
    #기본 이미지
    playgroundImgPath=resource_path("src/updown_playground.png")
    playgroundImg=tkinter.PhotoImage(file = playgroundImgPath)
    playgroundImglabel=tkinter.Label(window, image=playgroundImg, relief="flat", bg="#d4e157").place(x=-2,y=1)
    titleImgPath=resource_path("src/updown_title.png")
    titleImg=tkinter.PhotoImage(file = titleImgPath)
    titleImglabel=tkinter.Label(window, image=titleImg, relief="flat", bg="#d4e157").place(x=77.5,y=80)
    playgroundLoopImgPath=resource_path("src/updown_playgroundLoop.png")
    playgroundLoopImg=tkinter.PhotoImage(file = playgroundLoopImgPath)
    
    #버튼 이미지
    startImgPath=resource_path("src/updown_start.png")
    startImg=tkinter.PhotoImage(file = startImgPath)
    homeImgPath=resource_path("src/updown_home.png")
    homeImg=tkinter.PhotoImage(file = homeImgPath)
    restartImgPath=resource_path("src/updown_restart.png")
    restartImg=tkinter.PhotoImage(file = restartImgPath)
    exitImgPath=resource_path("src/updown_exit.png")
    exitImg=tkinter.PhotoImage(file = exitImgPath)

    #시작 버튼 위치
    startBtn=tkinter.Button(window, image=startImg ,relief="flat", bg="#385723", command=updown).place(x=163.5,y=230)

    window.mainloop()
