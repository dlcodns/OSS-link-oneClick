import tkinter
import tkinter.font
import tkinter.ttk
import tkinter.messagebox as msgbox
from tkinter import *
import csv
import pandas as pd
import os
import sys


#연락망 새창
def showContactpoint():
    newwindow=tkinter.Toplevel()
    newwindow.geometry("590x430")
    newwindow['bg']='honeydew'

    
    # exe 제작을 위한 이미지 경로 설정 함수
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        
        return os.path.join(base_path, relative_path)

    # CSV 파일 초기 생성
    mailCsvtPath = resource_path('oneClickData/mail_book.csv')
    phonebookCsvtPath = resource_path('oneClickData/phone_book.csv')
    memoCsvtPath = resource_path('oneClickData/memo.csv')

    if not os.path.isfile('oneClickData/mail_book.csv'):
        mailbookFile = []
        f = open(mailCsvtPath,'r')
        rdr = csv.reader(f)
        for row in rdr:
            mailbookFile.append(row)
        f.close
        f = open('oneClickData/mail_book.csv','w', newline='')
        wr = csv.writer(f)
        wr.writerows(mailbookFile)
        f.close()

    if not os.path.isfile('oneClickData/phone_book.csv'):
        phonebookFile = []
        f = open(phonebookCsvtPath,'r')
        rdr = csv.reader(f)
        for row in rdr:
            phonebookFile.append(row)
        f.close
        f = open('oneClickData/phone_book.csv','w', newline='')
        wr = csv.writer(f)
        wr.writerows(phonebookFile)
        f.close()

    if not os.path.isfile('oneClickData/memo.csv'):
        memoFile = []
        f = open(memoCsvtPath,'r')
        rdr = csv.reader(f)
        for row in rdr:
            memoFile.append(row)
        f.close
        f = open('oneClickData/memo.csv','w', newline='')
        wr = csv.writer(f)
        wr.writerows(memoFile)
        f.close()    


    #배경 사진
    contactpointImgPath=resource_path("src/contactpoint.png")
    contactpointImg=tkinter.PhotoImage(file= contactpointImgPath)

    contactpointImglabel=tkinter.Label(newwindow, image=contactpointImg, relief="flat").place(x =-1, y =-1)


#교수님 이메일 
    
    emailValues=['전체', '컴퓨터공학과', '교양(교수님)','SW사업단']
    emailCombobox=tkinter.ttk.Combobox(newwindow, values=emailValues, state="readonly", background="#E2F0D9")
    emailCombobox.place(x=20,y=118,width=80,height=20)
    emailCombobox.set("전체")

    emailEntry = Entry(newwindow, justify='center')  
    emailEntry.place(x=100,y=118,width=115,height=20)

    def emailFind():
        flag = 0
        mailCnt = 0
        mailbook = []
        f = open("./oneClickData/mail_book.csv",'r')
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

    phoneValues=['전체', '컴퓨터공학과','전자정보대학', '교양(교수님)', '교양교육본부', '국제교류본부','취업지원본부','SW사업단']
    numberCombobox=tkinter.ttk.Combobox(newwindow, state="readonly", values=phoneValues)
    numberCombobox.place(x=20,y=205,width=80,height=20)
    numberCombobox.set("전체")

    numberEntry = Entry(newwindow, justify='center') 
    numberEntry.place(x=100,y=205,width=115,height=20)

    def numberFind():
        flag = 0
        phoneCnt = 0
        phonebook = []
        f = open("./oneClickData/phone_book.csv",'r') 
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
        f = open("./oneClickData/mail_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = emailAddEnt.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

        emailAddEnt.delete(0,END)

        msgbox.showinfo( "알림", "저장되었습니다." )
        newwindow.lift()

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
        f = open("./oneClickData/phone_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = phoneAddEnt.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

        phoneAddEnt.delete(0,END)
        msgbox.showinfo( "알림", "저장되었습니다." )
        newwindow.lift()

    phoneAddbtn = Button(newwindow) 
    phoneAddbtn.config(text = "확인",background="#E2F0D9")
    phoneAddbtn.config(command = phoneAdd)
    phoneAddbtn.place(x=215,y=350,width=40,height=20)

#메모장
    memoCnt = 0    
    memo = []

    f = open("./oneClickData/memo.csv",'r')
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
        f = open("./oneClickData/memo.csv",'a',newline="")
        wr = csv.writer(f) 
        a = memoEntry.get().split('/')
        wr.writerow([a[0]])       
        f.close()

        memoCnt = 0    
        memo = []

        f = open("./oneClickData/memo.csv",'r')
        rdr = csv.reader(f)
        for row in rdr:
            memo.append(row)
        f.close

        memolistbox = Listbox(newwindow,selectmode = 'extended',relief="flat",bg="#DAE3F3")
        memolistbox.place(x=280,y=270,width=290, height = 80)

        for i in memo:
            memolistbox.insert(memoCnt, i)
            memoCnt=memoCnt+1  

        memoEntry.delete(0,END)
    
    memobtn = Button(newwindow) 
    memobtn.config(text = "저장",width=4,height=1 )
    memobtn.config(command = memoAdd)
    memobtn.place(x=533,y= 350)

#삭제 

    # delMail = Entry(newwindow) 
    # delMail.place(x=75,y=380,width=140,height=20)

    # def del_mail():

    #     delmail = delMail.get()

    #     dropMail = pd.read_csv("mail_book.csv")

    #     new_Mail = dropMail.drop(columns= delmail, inplace = True)
    #     new_Mail.head()

    # dbtn = Button(newwindow) 
    # dbtn.config(text = "삭제",width=4,height=1 )
    # dbtn.config(command = del_mail)
    # dbtn.place(x=215,y= 380)



    newwindow.mainloop()

