import tkinter
import tkinter.font
import tkinter.ttk

#기본적인 윈도우창 설정
window=tkinter.Tk()
window.title("One Click")
window.geometry("600x450+100+100")
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
oneclickimage = tkinter.PhotoImage(file = "color label.png")
imageLabel=tkinter.Label(window, image=oneclickimage, relief="flat", bg="cornsilk")
imageLabel.place(x=158,y=40)

#휴게소 라벨(이미지 넣어야하고 게임시작 버튼 넣어야함)
playimage = tkinter.PhotoImage(file = "123.png")
playimagelabel=tkinter.Label(window, image=playimage, relief="solid", bg="cornsilk")
playimagelabel.place(x=148,y=215)

#폰트 설정
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")




#주소모음 버튼
b1=tkinter.Button(window, text="충북대학교\n홈페이지",bg="cornsilk",relief="solid",borderwidth=1,font=font,command=createLoginWindow)
b2=tkinter.Button(window, text="충북대학교\necampus",bg="cornsilk",relief="solid",borderwidth=1, font=font,command=createLoginWindow)
b3=tkinter.Button(window, text="충북대학교\n학생생활관",bg="cornsilk",relief="solid",borderwidth=1, font=font,command=createLoginWindow)
b4=tkinter.Button(window, text="충북대학교\n개신누리",bg="cornsilk",relief="solid",borderwidth=1, font=font,command=createLoginWindow)
b5=tkinter.Button(window, text="충북대학교\n씨앗",bg="cornsilk",relief="solid",borderwidth=1, font=font,command=createLoginWindow)
b6=tkinter.Button(window, text="충북대학교\n취업지원본부",bg="cornsilk",relief="solid",borderwidth=1, font=font,command=createLoginWindow)

b7=tkinter.Button(window, text="백준",bg="cornsilk",relief="solid",borderwidth=1, font=font)
b8=tkinter.Button(window, text="코드업",bg="cornsilk", relief="solid",borderwidth=1,font=font)
b9=tkinter.Button(window, text="replit",bg="cornsilk", relief="solid",borderwidth=1,font=font)
b10=tkinter.Button(window, text="sw사업단\n공지사항",bg="cornsilk", relief="solid",borderwidth=1,font=font)
b11=tkinter.Button(window, text="컴공\n공지사항",bg="cornsilk", relief="solid",borderwidth=1,font=font)
b12=tkinter.Button(window, text="충북대학교\n전화번호",bg="cornsilk", relief="solid",borderwidth=1,font=font,command=createNumberWindow)

#주소버튼 절대위치
b1.place(x=55,y=30,width=80,height=50)
b2.place(x=55,y=100,width=80,height=50)
b3.place(x=55,y=170,width=80,height=50)
b4.place(x=55,y=240,width=80,height=50)
b5.place(x=55,y=310,width=80,height=50)
b6.place(x=55,y=380,width=80,height=50)

b7.place(x=505,y=30,width=80,height=50)
b8.place(x=505,y=100,width=80,height=50)
b9.place(x=505,y=170,width=80,height=50)
b10.place(x=505,y=240,width=80,height=50)
b11.place(x=505,y=310,width=80,height=50)
b12.place(x=505,y=380,width=80,height=50)

#클로버 이미지
homepageimage=tkinter.PhotoImage(file = "clover.png")
homepagelabel=tkinter.Label(window, image = homepageimage, relief="flat",bg="cornsilk")
homepagelabel.place(x=23, y=48, width=40 )

ecampusimage=tkinter.PhotoImage(file = "clover.png")
ecampuslabel=tkinter.Label(window, image = ecampusimage, relief="flat",bg="cornsilk")
ecampuslabel.place(x=23, y=118, width=40 )

dormimage=tkinter.PhotoImage(file = "clover.png")
dormlabel=tkinter.Label(window, image = dormimage, relief="flat",bg="cornsilk")
dormlabel.place(x=23, y=188, width=40 )

gaesinimage=tkinter.PhotoImage(file = "clover.png")
gaesinlabel=tkinter.Label(window, image = gaesinimage, relief="flat",bg="cornsilk")
gaesinlabel.place(x=23, y=258, width=40 )

siatimage=tkinter.PhotoImage(file = "clover.png")
siatlabel=tkinter.Label(window, image = siatimage, relief="flat",bg="cornsilk")
siatlabel.place(x=23, y=328, width=40 )

jobimage=tkinter.PhotoImage(file = "clover.png")
joblabel=tkinter.Label(window, image = jobimage, relief="flat",bg="cornsilk")
joblabel.place(x=18, y=398, width=40 )

#잎 라벨이미지
baekjunimage=tkinter.PhotoImage(file="leaf.png")
baekjunlabel=tkinter.Label(window, image=baekjunimage,relief="flat", bg="cornsilk")
baekjunlabel.place(x=475, y=40, width=40)

codeupimage=tkinter.PhotoImage(file="leaf.png")
codeuplabel=tkinter.Label(window, image=codeupimage,relief="flat", bg="cornsilk")
codeuplabel.place(x=475, y=110, width=40)

replitimage=tkinter.PhotoImage(file="leaf.png")
replitlabel=tkinter.Label(window, image=replitimage,relief="flat", bg="cornsilk")
replitlabel.place(x=475, y=180, width=40)

swimage=tkinter.PhotoImage(file="leaf.png")
swlabel=tkinter.Label(window, image=swimage,relief="flat", bg="cornsilk")
swlabel.place(x=475, y=250, width=40)

noticeimage=tkinter.PhotoImage(file="leaf.png")
noticelabel=tkinter.Label(window, image=noticeimage,relief="flat", bg="cornsilk")
noticelabel.place(x=475, y=320, width=40)

numberimage=tkinter.PhotoImage(file="leaf.png")
numberlabel=tkinter.Label(window, image=numberimage,relief="flat", bg="cornsilk")
numberlabel.place(x=475, y=390, width=40)

#휴게소 버튼
omokbttn=tkinter.Button(window, text="오목\n게임하기",relief="solid",borderwidth=1, bg="cornsilk",font=font)
updownbttn=tkinter.Button(window, text="업다운\n게임하기", relief="solid",borderwidth=1, bg="cornsilk",font=font)
omokbttn.place(x=195,y=390,width=70,height=36)
updownbttn.place(x=345,y=390,width=70,height=36)

#휴게소 꽃 라벨
omokimage=tkinter.PhotoImage(file = "flower.png")
omoklabel=tkinter.Label(window, image=omokimage, relief="flat", bg="cornsilk")
omoklabel.place(x=175,y=401,width=30)

updownimage=tkinter.PhotoImage(file = "flower.png")
updownlabel=tkinter.Label(window, image=updownimage, relief="flat", bg="cornsilk")
updownlabel.place(x=325,y=401,width=30)

window.mainloop()