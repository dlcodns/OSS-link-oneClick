import tkinter
import tkinter.font
import tkinter.ttk

#기본적인 윈도우창 설정
window=tkinter.Tk()
window.title("One Click")
window.geometry("540x450+100+100")
window.resizable(False,False)
window['bg']='cornsilk'

user_id, password = tkinter.StringVar(), tkinter.StringVar()

#전화번호부 새창
def createNumberWindow():
    newwindow=tkinter.Toplevel(window)
    newwindow.geometry("400x400")

#교수님 이메일 찾기
    label1=tkinter.ttk.Label(newwindow, text="교수님 이메일 찾기")
    label1.pack()

    value=['교양', '컴퓨터공학과']
    combobox1=tkinter.ttk.Combobox(newwindow, values=value)

    combobox1.pack()

    combobox1.set("목록 선택")

#전화번호 찾기
    label2=tkinter.ttk.Label(newwindow, text="전화번호 찾기")
    label2.pack()

    values=['교양교육본부', '행정지원실', '교양교육원', 'RC교육센터','의사소통센터','교양교수님', '컴공교수님']
    combobox2=tkinter.ttk.Combobox(newwindow, values=values)
    combobox2.pack()

    combobox2.set("목록 선택")

#전화번호 적을 리스트
    listbox = tkinter.ttk.Listbox(newwindow, selectmode='extended')
    listbox.insert(0,"0")
    listbox.insert(0,"1")
    listbox.insert(0,"2")
    listbox.insert(0,"3")
    listbox.insert(tkinter.ttk.End,"4")
    listbox.pack()


#로그인창
def createLoginWindow():
    newwindow=tkinter.Toplevel(window)
    tkinter.Label(newwindow, text = "Username : ").grid(row=0, column = 0, padx=10,pady=10)
    tkinter.Label(newwindow, text = "Password : ").grid(row=1, column = 0, padx=10,pady=10)
    tkinter.Entry(newwindow, textvariable = user_id).grid(row=0, column=1, padx=10, pady=10)
    tkinter.Entry(newwindow, textvariable = password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
    tkinter.Button(newwindow, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

def check_data():
    if user_id.get() == "Passing" and password.get() == "Story":
        print("Logged In Successfully")
    else:
        print("Check your Username/Password")

#원클릭 넣을 이미지라벨
image = tkinter.PhotoImage(file = "oneclick.png")
imageLabel=tkinter.Label(window, image=image, relief="flat", bg="cornsilk")
imageLabel.place(x=123,y=35)

#휴게소 라벨(이미지 넣어야하고 게임시작 버튼 넣어야함)
label2=tkinter.Label(window, text="휴게소", width=44,height=15, fg="blue",relief="solid")
label2.place(x=113,y=215)

#폰트 설정
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")

#주소모음 버튼
b1=tkinter.Button(window, text="충북대학교\n홈페이지",bg="pink1", font=font,command=createLoginWindow)
b2=tkinter.Button(window, text="충북대학교\necampus",bg="pink1", font=font,command=createLoginWindow)
b3=tkinter.Button(window, text="충북대학교\n학생생활관",bg="pink1", font=font,command=createLoginWindow)
b4=tkinter.Button(window, text="충북대학교\n개신누리",bg="pink1", font=font,command=createLoginWindow)
b5=tkinter.Button(window, text="충북대학교\n씨앗",bg="pink1", font=font,command=createLoginWindow)
b6=tkinter.Button(window, text="충북대학교\n취업지원본부",bg="pink1", font=font,command=createLoginWindow)

b7=tkinter.Button(window, text="백준",bg="white", font=font)
b8=tkinter.Button(window, text="코드업",bg="white", font=font)
b9=tkinter.Button(window, text="replit",bg="white", font=font)
b10=tkinter.Button(window, text="sw사업단\n공지사항",bg="white", font=font)
b11=tkinter.Button(window, text="컴퓨터공학과\n공지사항",bg="white", font=font)
b12=tkinter.Button(window, text="충북대학교\n전화번호",bg="white", font=font,command=createNumberWindow)

#주소버튼 절대위치
b1.place(x=20,y=30,width=80,height=50)
b2.place(x=20,y=100,width=80,height=50)
b3.place(x=20,y=170,width=80,height=50)
b4.place(x=20,y=240,width=80,height=50)
b5.place(x=20,y=310,width=80,height=50)
b6.place(x=20,y=380,width=80,height=50)

b7.place(x=440,y=30,width=80,height=50)
b8.place(x=440,y=100,width=80,height=50)
b9.place(x=440,y=170,width=80,height=50)
b10.place(x=440,y=240,width=80,height=50)
b11.place(x=440,y=310,width=80,height=50)
b12.place(x=440,y=380,width=80,height=50)


window.mainloop()