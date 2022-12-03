import tkinter
import tkinter.font
import tkinter.ttk
import random

window = tkinter.Tk()
window.title("업다운 게임")
window.geometry("500x400")
window.resizable(False,False)
window["bg"]="olivedrab"

font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")

ran = random.randint(1,100)
count = 0

def updown():
  global ran, count

  b2=tkinter.Button(window, text="게임 종료",bg="olivedrab",relief="raised",borderwidth=1,font=font,command=exit_game)
  b2.place(x=200,y=300,width=100,height=50)
  
  while(True):
        tkinter.Label(window, text="숫자 하나를 적으세요.",bg="darkslategray",fg="white",borderwidth=2,relief="raised").place(x=190,y=130,width=124,height=30)
    
        number = tkinter.StringVar()
        number_entered = tkinter.ttk.Entry(window, width=20, textvariable=number)
        number_entered.place(x=180,y=180)
    
        action = tkinter.Button(window, text="확인", command=lambda:[calc(number_entered)])
        action.place(x=330,y=178)
        
        if count == 6:
            print('\n정답은 %d였습니다~ 메롱 ㅋㅋㄹㅃㅃ', %(ran))
            break
            
def calc(enteredNum):
    global ran, count
    
    num = int(enteredNum.get())
        
    if ran > num:
        if count != 5:
                print('up!\n')
    elif ran < num:
        if count != 5:
            print('down!\n')
    elif ran == num:
        win = random.randint(1,3)
        if win == 1:
            print('딩동댕~ 정답!')
        if win == 2:
            print('운이 좋으시네요! :)')
        if win == 3:
            print('올ㅋ')
    count += 1
  
def exit_game():
    window.destroy()
  
b1=tkinter.Button(window, text="게임 시작",bg="olivedrab",relief="raised",borderwidth=1,font=font,command=updown)
b1.place(x=200,y=300,width=100,height=50)

window.mainloop()
