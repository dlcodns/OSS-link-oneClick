import tkinter
import tkinter.font
import tkinter.ttk

window = tkinter.Tk()
window.title("업다운 게임")
window.geometry("500x400")
window.resizable(False,False)
window['bg']='olivedrab'

font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")
  
b1=tkinter.Button(window, text="게임 시작",bg="olivedrab",relief="raised",borderwidth=1,font=font,command=updown)
b1.place(x=200,y=300,width=100,height=50)

window.mainloop()
