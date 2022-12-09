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
    newwindow.geometry("550x400")
    
#교수님 이메일 
    label3=tkinter.ttk.Label(newwindow, text="이메일 검색")
    label3.place(x=15,y=80)

    value=['컴퓨터공학과', '교양']
    combobox2=tkinter.ttk.Combobox(newwindow, values=value)
    combobox2.place(x=15,y=100,width=80,height=20)
    combobox2.set("전체")

    ent1 = Entry(newwindow)  
    ent1.place(x=95,y=100,width=120,height=20)
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
    btn.place(x=215,y=100,width=40,height=20)


#전화번호 
    label8=tkinter.ttk.Label(newwindow, text="전화번호 검색")
    label8.place(x=15,y=140)

    values=['컴퓨터공학과', '교양 교수님', '교양교육본부']
    combobox7=tkinter.ttk.Combobox(newwindow, values=values)
    combobox7.place(x=15,y=160,width=80,height=20)
    combobox7.set("전체")


    label9=tkinter.ttk.Label(newwindow, text="")
    label9.grid(column=3,row=6)

    ent2 = Entry(newwindow) 
    ent2.place(x=95,y=160,width=120,height=20)
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
    btn.place(x=215,y=160,width=40,height=20)
    
   
#메일 추가
    label10=tkinter.ttk.Label(newwindow, text="<연락망 추가하기>")
    label10.place(x=15,y=210)

    label11=tkinter.ttk.Label(newwindow, text="예시) 컴공/김민서/asdfghjkl@chungbuk.ac.kr")
    label11.place(x=15,y=240)

    label12=tkinter.ttk.Label(newwindow, text="예시) 컴공/김민서/010-1234-5678")
    label12.place(x=15,y=260)  

    label13=tkinter.ttk.Label(newwindow, text="메일 추가:")
    label13.place(x=15,y=290)

    ent3 = Entry(newwindow) 
    ent3.place(x=75,y=290,width=140,height=20)
    def ent3_s():
        f = open("mail_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = ent3.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

    btn = Button(newwindow) 
    btn.config(text = "확인")
    btn.config(command = ent3_s)
    btn.place(x=215,y=290,width=40,height=20)

#전화번호 추가
    label14=tkinter.ttk.Label(newwindow, text="번호 추가:")
    label14.place(x=15,y=320)

    ent4 = Entry(newwindow) 
    ent4.place(x=75,y=320,width=140,height=20)
    def ent3_s():
        f = open("phone_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = ent4.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

    btn = Button(newwindow) 
    btn.config(text = "확인")
    btn.config(command = ent3_s)
    btn.place(x=215,y=320,width=40,height=20)
    
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")    

b12=tkinter.Button(window, text="충북대학교\n연락망",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=contactpointWindow)
b12.place(x=505,y=380,width=80,height=50)

window.mainloop()
