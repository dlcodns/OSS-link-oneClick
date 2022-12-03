import tkinter
import tkinter.font
import tkinter.ttk
from tkinter import *

window=tkinter.Tk()
window.title("One Click")
window.geometry("600x450+100+100")
window.resizable(False,False)
window['bg']='cornsilk'

#연락망 새창
def contactpointWindow():
    newwindow=tkinter.Toplevel(window)
    newwindow.geometry("400x400")

#교수님 이메일 
    label1=tkinter.ttk.Label(newwindow, text="교수님 이메일")
    label1.pack()

    value=['컴퓨터공학과', '교양']
    combobox1=tkinter.ttk.Combobox(newwindow, values=value)
    combobox1.pack()
    combobox1.set("목록 선택")

    label2=tkinter.ttk.Label(newwindow, text="교수님 이메일 검색")
    label2.pack()

    label3=tkinter.ttk.Label(newwindow, text="")
    label3.pack()

    ent = Entry(label3) 
    ent.pack() 


font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")    

b12=tkinter.Button(window, text="충북대학교\n연락망",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=contactpointWindow)
b12.place(x=505,y=380,width=80,height=50)

window.mainloop()