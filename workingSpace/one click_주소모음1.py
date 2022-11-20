import tkinter

window=tkinter.Tk()
window.title("One Click")
window.geometry("540x450+100+100")
window.resizable(False,False)

label=tkinter.Label(window, text="휴게소", width=40,height=10, fg="blue",relief="solid")
label.place(x=65,y=300)
label.pack()

b1=tkinter.Button(window, text="충북대학교\n홈페이지")
b2=tkinter.Button(window, text="충북대학교\n씨앗")
b3=tkinter.Button(window, text="충북대학교\n학생생활관")
b4=tkinter.Button(window, text="충북대학교\necampus")
b5=tkinter.Button(window, text="충북대학교\n개신누리")
b6=tkinter.Button(window, text="충북대학교\n취업지원본부")

b7=tkinter.Button(window, text="백준")
b8=tkinter.Button(window, text="코드업")
b9=tkinter.Button(window, text="replit")
b10=tkinter.Button(window, text="충북대학교\n전화번호")


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