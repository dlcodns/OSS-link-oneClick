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
    newwindow.geometry("400x300")
    
#교수님 이메일 
    label1=tkinter.ttk.Label(newwindow, text="")
    label1.pack()

    label2=tkinter.ttk.Label(newwindow, text="교수님 이메일")
    label2.pack()

    value=['컴퓨터공학과', '교양']
    combobox2=tkinter.ttk.Combobox(newwindow, values=value)
    combobox2.pack()
    combobox2.set("목록 선택")

    label3=tkinter.ttk.Label(newwindow, text="교수님 이메일 검색")
    label3.pack()

    label4=tkinter.ttk.Label(newwindow, text="")
    label4.pack()

    ent = Entry(label4)  
    ent.pack() 

#전화번호 
    label5=tkinter.ttk.Label(newwindow, text="")
    label5.pack()

    label6=tkinter.ttk.Label(newwindow, text="")
    label6.pack()

    label7=tkinter.ttk.Label(newwindow, text="전화번호 찾기")
    label7.pack()

    values=['컴퓨터공학과', '교양 교수님', '교양교육본부']
    combobox7=tkinter.ttk.Combobox(newwindow, values=values)
    combobox7.pack()
    combobox7.set("목록 선택")

    label8=tkinter.ttk.Label(newwindow, text="전화번호 검색")
    label8.pack()

    label9=tkinter.ttk.Label(newwindow, text="")
    label9.pack()

    ent = Entry(label9) 
    ent.pack() 
    
    
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")    

b12=tkinter.Button(window, text="충북대학교\n연락망",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=contactpointWindow)
b12.place(x=505,y=380,width=80,height=50)

window.mainloop()
