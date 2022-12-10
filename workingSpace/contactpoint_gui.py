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
    email=tkinter.ttk.Label(newwindow, text="이메일 검색")
    email.place(x=15,y=80)
    
    emailValues=['전체', '컴퓨터공학과', '교양']
    emailCombobox=tkinter.ttk.Combobox(newwindow, values=emailValues)
    emailCombobox.place(x=15,y=100,width=80,height=20)
    emailCombobox.set("전체")

    emailPrint=Label(newwindow)
    emailPrint.config(relief='sunken', width=41, height = 7)
    emailPrint.place(x=280,y=80)

    emailEnt = Entry(newwindow)  
    emailEnt.place(x=95,y=100,width=120,height=20)

    def searchEmail(a,b,c):
        if emailCombobox.get() == a:
            emailCnta = 0
            mailbook = []
            print("전체")
            f = open("mail_book.csv",'r')
            rdr = csv.reader(f)
            for row in rdr:
                mailbook.append(row)
            f.close

            a = emailEnt.get()

            emailListboxa = Listbox(newwindow, selectmode = 'extended',width=41, height = 7)
            emailListboxa.place(x=280,y=80)            
            for i in mailbook:
                
                    if a == "":
                        emailListboxa.insert(emailCnta, "[{}] {} {}".format(i[0], i[1], i[2]))
                        emailCnta = emailCnta+1
                    elif a in i[0] or a in i[1] or a in i[2]:
                        emailListboxa.insert(emailCnta, "[{}] {} {}".format(i[0], i[1], i[2]))
                        emailCnta = emailCnta+1


        elif  emailCombobox.get()==b:
                emailCntb = 0
                mailbook = []
                print("컴공")
                f = open("mail_bookA.csv",'r')
                rdr = csv.reader(f)
                for row in rdr:
                    mailbook.append(row)
                f.close

                a = emailEnt.get()

                emailListboxb = Listbox(newwindow, selectmode = 'extended',width=41, height = 7)
                emailListboxb.place(x=280,y=80) 
                for i in mailbook:
                        if a == "":
                            emailListboxb.insert(emailCntb, "[{}] {} {}".format(i[0], i[1], i[2]))
                            emailCntb = emailCntb+1
                        elif a in i[0] or a in i[1] or a in i[2]:
                            emailListboxb.insert(emailCntb, "[{}] {} {}".format(i[0], i[1], i[2]))
                            emailCntb = emailCntb+1                    
                            

        elif  emailCombobox.get() == c:
                emailCntc = 0
                mailbook = []
                print("교양")
                f = open("mail_bookB.csv",'r')
                rdr = csv.reader(f)
                for row in rdr:
                    mailbook.append(row)
                f.close

                a = emailEnt.get()

                emailListboxc = Listbox(newwindow, selectmode = 'extended',width=41, height = 7)
                emailListboxc.place(x=280,y=80)                
                for i in mailbook:
                        if a == "":
                            emailListboxc.insert(emailCntc, "[{}] {} {}".format(i[0], i[1], i[2]))
                            emailCntc = emailCntc+1
                        elif a in i[0] or a in i[1] or a in i[2]:
                            emailListboxc.insert(emailCntc, "[{}] {} {}".format(i[0], i[1], i[2]))
                            emailCntc = emailCntc+1  
      
    emailbtn = Button(newwindow) 
    emailbtn.config(text = "확인")
    emailbtn.config(command = lambda:[searchEmail(emailValues[0],emailValues[1],emailValues[2])])
    emailbtn.place(x=215,y=100,width=40,height=20)


#전화번호 
    phone=tkinter.ttk.Label(newwindow, text="전화번호 검색")
    phone.place(x=15,y=140)

    phoneValues=['전체', '컴퓨터공학과', '교양 교수님', '교양교육본부']
    phonecombobox=tkinter.ttk.Combobox(newwindow, values=phoneValues)
    phonecombobox.place(x=15,y=160,width=80,height=20)
    phonecombobox.set("전체")

    phoneEnt = Entry(newwindow) 
    phoneEnt.place(x=95,y=160,width=120,height=20)
    def searchPhone(a,b,c,d): 
        if  phonecombobox.get()==a:
            phonebook = []
            print("전체")
            f = open("phone_book.csv",'r')  
            rdr = csv.reader(f)
            for row in rdr:
                phonebook.append(row)
            f.close
            a = phoneEnt.get()
            for i in phonebook:
                    if a == "":
                        print("[{}] {} {}".format(i[0], i[1], i[2])) 
                    elif a in i[0] or a in i[1] or a in i[2]:
                        print("[{}] {} {}".format(i[0], i[1], i[2]))    

        elif  phonecombobox.get() == b:
            phonebook = []
            print("컴퓨터공학과")
            f = open("phone_bookA.csv",'r')  
            rdr = csv.reader(f)
            for row in rdr:
                phonebook.append(row)
            f.close
            a = phoneEnt.get()
            for i in phonebook:
                    if a == "":
                        print("[{}] {} {}".format(i[0], i[1], i[2])) 
                    elif a in i[0] or a in i[1] or a in i[2]:
                        print("[{}] {} {}".format(i[0], i[1], i[2]))                         

        elif phonecombobox.get() == c:
            phonebook = []
            print("교양 교수님")
            f = open("phone_bookB.csv",'r')  
            rdr = csv.reader(f)
            for row in rdr:
                phonebook.append(row)
            f.close
            a = phoneEnt.get()
            for i in phonebook:
                    if a == "":
                        print("[{}] {} {}".format(i[0], i[1], i[2])) 
                    elif a in i[0] or a in i[1] or a in i[2]:
                        print("[{}] {} {}".format(i[0], i[1], i[2]))       

        elif phonecombobox.get() == d:
            phonebook = []
            print("교양교육본부")
            f = open("phone_bookC.csv",'r')  
            rdr = csv.reader(f)
            for row in rdr:
                phonebook.append(row)
            f.close
            a = phoneEnt.get()
            for i in phonebook:
                    if a == "":
                        print("[{}] {} {}".format(i[0], i[1], i[2])) 
                    elif a in i[0] or a in i[1] or a in i[2]:
                        print("[{}] {} {}".format(i[0], i[1], i[2])) 


    phonebtn = Button(newwindow) 
    phonebtn.config(text = "확인")
    phonebtn.config(command = lambda:[searchPhone(phoneValues[0],phoneValues[1],phoneValues[2],phoneValues[3])])
    phonebtn.place(x=215,y=160,width=40,height=20)
    
   
#메일 추가
    contactAdd=tkinter.ttk.Label(newwindow, text="<연락망 추가하기>")
    contactAdd.place(x=15,y=210)

    ex1=tkinter.ttk.Label(newwindow, text="예시) 컴공/김민서/asdfghjkl@chungbuk.ac.kr")
    ex1.place(x=15,y=240)

    ex2=tkinter.ttk.Label(newwindow, text="예시) 컴공/김민서/010-1234-5678")
    ex2.place(x=15,y=260)  

    emaill=tkinter.ttk.Label(newwindow, text="메일 추가:")
    emaill.place(x=15,y=290)

    emailAddEnt = Entry(newwindow) 
    emailAddEnt.place(x=75,y=290,width=140,height=20)
    def emailAdd():
        f = open("mail_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = emailAddEnt.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

    emailAddbtn = Button(newwindow) 
    emailAddbtn.config(text = "확인")
    emailAddbtn.config(command = emailAdd)
    emailAddbtn.place(x=215,y=290,width=40,height=20)

#전화번호 추가
    phonee=tkinter.ttk.Label(newwindow, text="번호 추가:")
    phonee.place(x=15,y=320)

    phoneAddEnt = Entry(newwindow) 
    phoneAddEnt.place(x=75,y=320,width=140,height=20)
    def phoneAdd():
        f = open("phone_book.csv",'a',newline="")
        wr = csv.writer(f) 

        a = phoneAddEnt.get().split('/')
        
        wr.writerow([a[0],a[1],a[2]])
        f.close()

    phoneAddbtn = Button(newwindow) 
    phoneAddbtn.config(text = "확인")
    phoneAddbtn.config(command = phoneAdd)
    phoneAddbtn.place(x=215,y=320,width=40,height=20)
    
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")    

b12=tkinter.Button(window, text="충북대학교\n연락망",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=contactpointWindow)
b12.place(x=505,y=380,width=80,height=50)

window.mainloop()
