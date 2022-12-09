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
        
#def jeabi():
    #재시작, 종료 버튼 만들기
    #인원수num 프린트하기
    #2~8명 제한
    #a배열 만들기
    #역할 정하기 라벨(나열 후 전체 확인)
    #
    #shake(num)
    #최종 제비들 나열
    #클릭하면 역할 보이기
    #

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
startImgPath=resource_path("src/start.png")
startImg=tkinter.PhotoImage(file = startImgPath)

#시작 버튼 위치
startBtn=tkinter.Button(window, image=startImg ,relief="flat", bg="#385723").place(x=163.5,y=230)

window.mainloop()
