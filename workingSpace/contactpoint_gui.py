import tkinter
import tkinter.font
import tkinter.ttk
import tkinter.messagebox as msgbox
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
    newwindow.geometry("590x430")
    newwindow['bg']='honeydew'

    contactpointImglabel=tkinter.Label(newwindow, image=contactpointImg, relief="flat").place(x =-1, y =-1)

#교수님 이메일 
    
    emailValues=['전체', '컴퓨터공학과', '교양']
    emailCombobox=tkinter.ttk.Combobox(newwindow, values=emailValues, background="#E2F0D9")
    emailCombobox.place(x=20,y=118,width=80,height=20)
    emailCombobox.set("전체")

    emailEntry = Entry(newwindow)  
    emailEntry.place(x=100,y=118,width=115,height=20)

    def emailFind():
        flag = 0
        mailCnt = 0
        mailbook = []
        f = open("mail_book.csv",'r')
        rdr = csv.reader(f)
        for row in rdr:
            mailbook.append(row)
        f.close

        emailListbox = Listbox(newwindow, selectmode = 'extended',relief="flat",bg="#E2F0D9",width=38, height = 9)
        emailListbox.place(x=290,y=83)  

        for i in mailbook:
            if (emailCombobox.get() == i[0]) or (emailCombobox.get() == "전체"):
                if (emailEntry.get() in i[0] or emailEntry.get() in i[1] or emailEntry.get() in i[2]):
                    emailListbox.insert(mailCnt, "[{}] {} {}".format(i[0], i[1], i[2]))
                    mailCnt = mailCnt+1 
                    flag = 1

        if flag == 0:
            print("없음")

    emailbtn = Button(newwindow) 
    emailbtn.config(text = "확인",background="#E2F0D9")
    emailbtn.config(command = emailFind)
    emailbtn.place(x=215,y=118,width=40,height=20)

#전화번호 

    phoneValues=['전체', '컴퓨터공학과', '교양 교수님', '교양교육본부']
    numberCombobox=tkinter.ttk.Combobox(newwindow, values=phoneValues)
    numberCombobox.place(x=20,y=205,width=80,height=20)
    numberCombobox.set("전체")

    numberEntry = Entry(newwindow) 
    numberEntry.place(x=100,y=205,width=115,height=20)

    def numberFind():
        flag = 0
        phoneCnt = 0
        phonebook = []
        f = open("phone_book.csv",'r') 
        rdr = csv.reader(f)
        for row in rdr:
            phonebook.append(row)
        f.close

        phoneListbox = Listbox(newwindow, selectmode = 'extended',relief="flat",bg="#E2F0D9",width=38, height = 9)
        phoneListbox.place(x=290,y=85) 

        for i in phonebook:
            if (numberCombobox.get() == i[0]) or (numberCombobox.get() == "전체"):
                if (numberEntry.get() in i[0] or numberEntry.get() in i[1] or numberEntry.get() in i[2]):
                    phoneListbox.insert(phoneCnt, "[{}] {} {}".format(i[0], i[1], i[2]))
                    phoneCnt = phoneCnt+1 
                    flag = 1

        if flag == 0:
            print("없음")

    phonebtn = Button(newwindow) 
    phonebtn.config(text = "확인",background="#E2F0D9")
    phonebtn.config(command = numberFind)
    phonebtn.place(x=215,y=205, width=40,height=20)
    
   
#메일 추가

    emaill=tkinter.ttk.Label(newwindow, text="메일 추가", background="#CCF4D9")
    emaill.place(x=18,y=320)

    emailAddEnt = Entry(newwindow) 
    emailAddEnt.place(x=75,y=320,width=140,height=20)
    def emailAdd():
        f = open("mail_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = emailAddEnt.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

        msgbox.showinfo( "알림", "저장되었습니다." )

    emailAddbtn = Button(newwindow) 
    emailAddbtn.config(text = "확인",background="#E2F0D9")
    emailAddbtn.config(command = emailAdd)
    emailAddbtn.place(x=215,y=320,width=40,height=20)

#전화번호 추가
    phonee=tkinter.ttk.Label(newwindow, text="번호 추가", background="#CCF4D9")
    phonee.place(x=18,y=350)

    phoneAddEnt = Entry(newwindow) 
    phoneAddEnt.place(x=75,y=350,width=140,height=20)
    def phoneAdd():
        f = open("phone_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = phoneAddEnt.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

        msgbox.showinfo( "알림", "저장되었습니다." )

    phoneAddbtn = Button(newwindow) 
    phoneAddbtn.config(text = "확인",background="#E2F0D9")
    phoneAddbtn.config(command = phoneAdd)
    phoneAddbtn.place(x=215,y=350,width=40,height=20)

#메모장
    memoCnt = 0    
    memo = []

    f = open("memo.csv",'r')
    rdr = csv.reader(f)
    for row in rdr:
        memo.append(row)
    f.close

    memolistbox = Listbox(newwindow,selectmode = 'extended',relief="flat",bg="#DAE3F3")
    memolistbox.place(x=280,y=270,width=290, height = 80)

    for i in memo:
        memolistbox.insert(memoCnt, i)
        memoCnt=memoCnt+1  

    memoEntry = Entry(newwindow)
    memoEntry.place(x = 278, y = 350,width=255, height =25)  
     
    def memoAdd():
        f = open("memo.csv",'a',newline="")
        wr = csv.writer(f) 
        a = memoEntry.get().split('/')
        wr.writerow([a[0]])       
        f.close()
    
    memobtn = Button(newwindow) 
    memobtn.config(text = "저장",width=4,height=1 )
    memobtn.config(command = memoAdd)
    memobtn.place(x=533,y= 350)
    
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")    

b12=tkinter.Button(window, text="충북대학교\n연락망",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=contactpointWindow)
b12.place(x=505,y=380,width=80,height=50)

window.mainloop()
