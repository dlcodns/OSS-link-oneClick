import tkinter
import tkinter.font
import tkinter.ttk

window = tkinter.Tk()
window.title("업다운 게임")
window.geometry("500x400")
window.resizable(False,False)
window['bg']='olivedrab'

font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")

def updown():
  b2=tkinter.Button(window, text="게임 종료",bg="olivedrab",relief="raised",borderwidth=1,font=font,command=exit_game)
  b2.place(x=200,y=300,width=100,height=50)
  
  tkinter.Label(window, text="숫자 하나를 적으세요.",bg="darkslategray",fg="white",borderwidth=2,relief="raised").place(x=190,y=130,width=124,height=30)
    
  number = tkinter.StringVar()
  number_entered = tkinter.ttk.Entry(window, width=20, textvariable=number)
  number_entered.place(x=180,y=180)
  
  action = tkinter.Button(window, text="확인")
  action.place(x=330,y=178)
  
def exit_game():
    window.destroy()
  
b1=tkinter.Button(window, text="게임 시작",bg="olivedrab",relief="raised",borderwidth=1,font=font,command=updown)
b1.place(x=200,y=300,width=100,height=50)

window.mainloop()
