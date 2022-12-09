import tkinter
import tkinter.font
import tkinter.ttk
from tkinter import *
import csv

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
    label1.grid(column=0,row=0)

    label2=tkinter.ttk.Label(newwindow, text="교수님 이메일")
    label2.grid(column=1,row=1)

    value=['컴퓨터공학과', '교양']
    combobox2=tkinter.ttk.Combobox(newwindow, values=value)
    combobox2.grid(column=1,row=2)
    combobox2.set("목록 선택")

    label3=tkinter.ttk.Label(newwindow, text="교수님 이메일 검색")
    label3.grid(column=3,row=1)

    label4=tkinter.ttk.Label(newwindow, text="")
    label4.grid(column=2,row=2)

    ent1 = Entry(newwindow)  
    ent1.grid(column=3,row=2)
    def ent1_s():
        mailbook = []

        f = open("mail_book.csv",'r')
        rdr = csv.reader(f)
        for row in rdr:
            mailbook.append(row)
        f.close

        a = ent1.get()
        for i in mailbook:
                if a == "":
                    print("[{}] {} {}".format(i[0], i[1], i[2])) 
                elif a in i[0] or a in i[1] or a in i[2]:
                    print("[{}] {} {}".format(i[0], i[1], i[2]))

    btn = Button(newwindow) 
    btn.config(text = "확인")
    btn.config(command = ent1_s)
    btn.grid(column=4,row=2)


#전화번호 
    label5=tkinter.ttk.Label(newwindow, text="")
    label5.grid(column=0,row=3)

    label6=tkinter.ttk.Label(newwindow, text="")
    label6.grid(column=0,row=4)

    label7=tkinter.ttk.Label(newwindow, text="전화번호 찾기")
    label7.grid(column=1,row=5)

    values=['컴퓨터공학과', '교양 교수님', '교양교육본부']
    combobox7=tkinter.ttk.Combobox(newwindow, values=values)
    combobox7.grid(column=1,row=6)
    combobox7.set("목록 선택")

    label8=tkinter.ttk.Label(newwindow, text="전화번호 검색")
    label8.grid(column=3,row=5)

    label9=tkinter.ttk.Label(newwindow, text="")
    label9.grid(column=3,row=6)

    ent2 = Entry(newwindow) 
    ent2.grid(column=3,row=6)
    def ent2_s(): 
        phonebook = []

        f = open("phone_book.csv",'r')
        rdr = csv.reader(f)
        for row in rdr:
            phonebook.append(row)
        f.close

        a = ent2.get()
        for i in phonebook:
                if a == "":
                    print("[{}] {} {}".format(i[0], i[1], i[2])) 
                elif a in i[0] or a in i[1] or a in i[2]:
                    print("[{}] {} {}".format(i[0], i[1], i[2]))

    btn = Button(newwindow) 
    btn.config(text = "확인")
    btn.config(command = ent2_s)
    btn.grid(column=4,row=6)
    
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")    

b12=tkinter.Button(window, text="충북대학교\n연락망",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=contactpointWindow)
b12.place(x=505,y=380,width=80,height=50)

window.mainloop()
