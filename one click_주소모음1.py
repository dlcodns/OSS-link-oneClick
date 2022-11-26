import tkinter
import tkinter.font

window=tkinter.Tk()
window.title("One Click")
window.geometry("540x450+100+100")
window.resizable(False,False)
window['bg']='cornsilk'

image=tkinter.PhotoImage(file="oneclick.png")

label=tkinter.Label(window,text="ccc",width=200, height=105,relief="solid",image=image)
label.pack()

label=tkinter.Label(window, text="휴게소", width=44,height=15, fg="blue",relief="solid")
label.place(x=113,y=215)

font=tkinter.font.Font(family="맑은 고딕", size=10, weight="bold")

b1=tkinter.Button(window, text="충북대학교\n홈페이지",bg="white", font=font)
b2=tkinter.Button(window, text="충북대학교\n씨앗",bg="white", font=font)
b3=tkinter.Button(window, text="충북대학교\n학생생활관",bg="white", font=font)
b4=tkinter.Button(window, text="충북대학교\necampus",bg="white", font=font)
b5=tkinter.Button(window, text="충북대학교\n개신누리",bg="white", font=font)
b6=tkinter.Button(window, text="충북대학교\n취업지원본부",bg="white", font=font)

b7=tkinter.Button(window, text="백준",bg="white", font=font)
b8=tkinter.Button(window, text="코드업",bg="white", font=font)
b9=tkinter.Button(window, text="replit",bg="white", font=font)
b10=tkinter.Button(window, text="충북대학교\n전화번호",bg="white", font=font)


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

window.mainloop()