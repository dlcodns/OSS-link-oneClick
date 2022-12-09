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

#난수 설정
#def shake():
    #for i in range(0,):
        
def jeabi():
    startCover=tkinter.Label(window, bg="light yellow",relief="flat").place(x=164,y=290,width=170,height=62)
    
    restartBtn=tkinter.Button(window, image=restartImg ,relief="flat", command=jeabi).place(x=125,y=271)
    exitBtn=tkinter.Button(window, image=exitImg ,relief="flat", command=exit_game).place(x=277,y=271)
    #재시작, 종료 버튼 만들기(완료)
    #인원수num 프린트하기
    #2~8명 제한
    #a배열 만들기
    #역할 정하기 라벨(나열 후 전체 확인)
    #
    #shake(num)
    #최종 제비들 나열
    #클릭하면 역할 보이기
    #

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

#버튼 이미지
jstartImgPath=resource_path("src/jstart.png")
jstartImg=tkinter.PhotoImage(file = jstartImgPath)
restartImgPath=resource_path("src/restart.png")
restartImg=tkinter.PhotoImage(file = restartImgPath)
exitImgPath=resource_path("src/exit.png")
exitImg=tkinter.PhotoImage(file = exitImgPath)

#시작 버튼 위치
jstartBtn=tkinter.Button(window, image=jstartImg ,relief="flat", command=jeabi).place(x=174,y=290)

window.mainloop()
