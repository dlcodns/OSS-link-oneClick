from tkinter import *
import tkinter.font
from tkinter.ttk import Combobox
from tkinter import messagebox
from selenium.webdriver.common.keys import Keys
#웹드라이버 자동
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.alert import Alert # 팝업창 해결위해서

chromedriver_autoinstaller.install(True)                         # 크롬 드라이버 자동 설치
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)      # 창 꺼지지 않는 옵션
chrome_options.add_argument('incognito')                    # 시크릿 모드로 실행
chrome_options.add_argument('start-maximized')              # 최대화
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', "disable-popup-blocking"]) #로그 안뜨게 + 팝업차단

chrome_service = Service('chromedriver')
chrome_service.creationflags = 0x08000000

#기본적인 윈도우창 설정
root=Tk()
root.title("One Click")
root.geometry("600x450+100+100")
root.resizable(False,False)
root['bg']='cornsilk'

# 계정 초기화
myId = ''
myPw = ''

# ----------------------------------------------------------------------------------------
# 일반 링크 부분

def ecampusWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://ecampus.chungbuk.ac.kr/')

def homepageWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://chungbuk.ac.kr/')
    
def cieatWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://cieat.cbnu.ac.kr/')

def dormWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://dorm.chungbuk.ac.kr/')
    
def geshinWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://eis.cbnu.ac.kr/')
    
def jobWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('http://hrd.chungbuk.ac.kr/')


# -------------------------------------------------------------------------------------    
# 자동로그인 부분

def ecampusAutoWindow() :
    if myId == '' or myPw == '' :
        ecampusWindow()
    else :
        args = ["hide_console", ]
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get('https://ecampus.chungbuk.ac.kr/')

        id = browser.find_element(By.XPATH,'//*[@id="uid"]')
        id.click()
        id.send_keys(myId)

        pw = browser.find_element(By.XPATH,'//*[@id="pswd"]')
        pw.click()
        pw.send_keys(myPw)

        browser.find_element(By.XPATH,'//*[@id="entry-login"]').click()
    
def homepageAutoWindow() :
    if myId == '' or myPw == '' :
        homepageWindow()
    else :
        args = ["hide_console", ]
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get('https://www.chungbuk.ac.kr/')
        
        browser.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/ul/li[2]/a').click()

        id = browser.find_element(By.XPATH,'//*[@id="userid"]')
        id.click()
        id.send_keys(myId)

        pw = browser.find_element(By.XPATH,'//*[@id="userpw"]')
        pw.click()
        pw.send_keys(myPw)

        browser.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/div/div/span/input').click()
    
def cieatAutoWindow() :
    if myId == '' or myPw == '' :
        cieatWindow()
    else :
        args = ["hide_console", ]
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get('https://cieat.cbnu.ac.kr/')

        browser.find_element(By.XPATH,'/html/body/div[3]/header/div[2]/div/a').click()
        
        id = browser.find_element(By.XPATH,'//*[@id="userId"]')
        id.click()
        id.send_keys(myId)

        pw = browser.find_element(By.XPATH,'//*[@id="userPw"]')
        pw.click()
        pw.send_keys(myPw)

        browser.find_element(By.XPATH,'//*[@id="loginBtnStd"]').click()
    
def dormAutoWindow() :
    if myId == '' or myPw == '' :
        dormWindow()
    else :
        args = ["hide_console", ]
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get('https://dorm.chungbuk.ac.kr/')

        browser.find_element(By.XPATH,'//*[@id="gnb"]/ul/li[1]').click()

        id = browser.find_element(By.XPATH,'//*[@id="info1"]')
        id.click()
        id.send_keys(myId)

        pw = browser.find_element(By.XPATH,'//*[@id="info2"]')
        pw.click()
        pw.send_keys(myPw)

        browser.find_element(By.XPATH,'//*[@id="memberLoginForm"]/fieldset/button').click()
        
        # IP확인 팝업 뜨면 닫기
        alert = Alert(browser)
        alert.accept()

def geshinAutoWindow() :
    if myId == '' or myPw == '' :
        geshinWindow()
    else :
        args = ["hide_console", ]
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get('https://eis.cbnu.ac.kr/')

        id = browser.find_element(By.XPATH,'//*[@id="uid"]')
        id.click()
        id.send_keys(myId)

        pw = browser.find_element(By.XPATH,'//*[@id="pswd"]')
        pw.click()
        pw.send_keys(myPw)

        browser.find_element(By.XPATH,'//*[@id="commonLoginBtn"]').click()
    
def jobAutoWindow() :
    if myId == '' or myPw == '' :
        jobWindow()
    else :
        args = ["hide_console", ]
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get('http://hrd.chungbuk.ac.kr/')

        id = browser.find_element(By.XPATH,'//*[@id="id"]')
        id.click()
        id.send_keys(myId)

        pw = browser.find_element(By.XPATH,'//*[@id="pw"]')
        pw.click()
        pw.send_keys(myPw)

        browser.find_element(By.XPATH,'//*[@id="login"]/form/div[2]/div[2]/table/tbody/tr[1]/td[2]/input').click()

        # 셀레니움 봇 사용으로 인한 안전하지 않음 표시 무시하기
        browser.find_element(By.XPATH,'//*[@id="proceed-button"]').click()
        
# 로그인 메뉴 설정
windowOpen = False

def whenClose(event) :
    global windowOpen
    windowOpen = False

def whenOpen() :
    global windowOpen
    windowOpen = True

def logoutFunc() :
    global myId, myPw
    if myId == '' or myPw == '' :
        messagebox.showinfo("로그아웃", "로그인 되어있지 않습니다.")
    else :
        messagebox.showinfo("로그아웃", "로그아웃 되었습니다.")
        myId = ''
        myPw = ''

def loginMenu() :
    if not windowOpen :       
        loginWindow = Tk()
        loginWindow.title("로그인")
        loginWindow.geometry("280x150+600+190")
        loginWindow.resizable(width = False, height = False)
        whenOpen()
        loginWindow.bind('<Destroy>', whenClose)
     
        # 로그인 창에 들어갈 내용
        idLabel = Label(loginWindow, text="학번")
        idEntry = Entry(loginWindow)
        pwLabel = Label(loginWindow, text="비밀번호")
        pwEntry = Entry(loginWindow, show="*")
        loginButton = Button(loginWindow, text="로그인", command=lambda:[loginFunc(idEntry.get(), pwEntry.get())])

        def loginFunc(id, pw) :
            global myId, myPw
            if id == '' or pw == '' :
                messagebox.showerror("로그인 오류", "아이디와 비밀번호를 입력해주세요.")
                loginWindow.lift()
            else :
                myId = id
                myPw = pw
                messagebox.showinfo("로그인", "로그인 되었습니다.")
                loginWindow.destroy()
            
        idLabel.grid(row=0, column=0, padx=10, pady=10)
        idEntry.grid(row=0, column=1, padx=10, pady=10)
        pwLabel.grid(row=1, column=0, padx=10, pady=10)
        pwEntry.grid(row=1, column=1, padx=10, pady=10)
        loginButton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#전화번호부 새창
def createNumberWindow():
    newwindow=Toplevel(root)
    newwindow.geometry("400x400")

#교수님 이메일 찾기
    label1=Label(newwindow, text="교수님 이메일 찾기")
    label1.pack()

    value=['교양', '컴퓨터공학과']
    combobox1=Combobox(newwindow, values=value)

    combobox1.pack()

    combobox1.set("목록 선택")

#전화번호 찾기
    label2=Label(newwindow, text="전화번호 찾기")
    label2.pack()

    values=['교양교육본부', '행정지원실', '교양교육원', 'RC교육센터','의사소통센터','교양교수님', '컴공교수님']
    combobox2=Combobox(newwindow, values=values)
    combobox2.pack()

    combobox2.set("목록 선택")

#전화번호 적을 리스트
    listbox = Listbox(newwindow, selectmode='extended')
    listbox.insert(0,"0")
    listbox.insert(0,"1")
    listbox.insert(0,"2")
    listbox.insert(0,"3")
    listbox.pack()


# GUI Section------------------------------------------------------------

# Menu Bar
menubar=Menu(root)
menubar.add_cascade(label="로그인", command=lambda:[loginMenu()])
menubar.add_cascade(label="로그아웃", command=lambda:[logoutFunc()])
root.config(menu=menubar)

#폰트 설정
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")


#주소모음 버튼
homepageBtn=Button(root, text="충북대학교\n홈페이지", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=homepageAutoWindow)
ecampusBtn=Button(root, text="충북대학교\necampus", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=ecampusAutoWindow)
dormBtn=Button(root, text="충북대학교\n학생생활관", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=dormAutoWindow)
geshinBtn=Button(root, text="충북대학교\n개신누리", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=geshinAutoWindow)
cieatBtn=Button(root, text="충북대학교\n씨앗", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=cieatAutoWindow)
jobBtn=Button(root, text="충북대학교\n취업지원본부", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=jobAutoWindow)

baekjuneBtn=Button(root, text="백준", bg="cornsilk", relief="solid", borderwidth=1, font=font)
codeupBtn=Button(root, text="코드업", bg="cornsilk", relief="solid", borderwidth=1, font=font)
replitBtn=Button(root, text="replit", bg="cornsilk", relief="solid", borderwidth=1, font=font)
sojungBtn=Button(root, text="SW사업단\n공지사항", bg="cornsilk", relief="solid", borderwidth=1, font=font)
majorBtn=Button(root, text="컴공\n공지사항", bg="cornsilk", relief="solid", borderwidth=1, font=font)
phonebookBtn=Button(root, text="충북대학교\n전화번호", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=createNumberWindow)


#주소버튼 절대위치
homepageBtn.place(x=55,y=30,width=80,height=50)
ecampusBtn.place(x=55,y=100,width=80,height=50)
dormBtn.place(x=55,y=170,width=80,height=50)
geshinBtn.place(x=55,y=240,width=80,height=50)
cieatBtn.place(x=55,y=310,width=80,height=50)
jobBtn.place(x=55,y=380,width=80,height=50)

baekjuneBtn.place(x=505,y=30,width=80,height=50)
codeupBtn.place(x=505,y=100,width=80,height=50)
replitBtn.place(x=505,y=170,width=80,height=50)
sojungBtn.place(x=505,y=240,width=80,height=50)
majorBtn.place(x=505,y=310,width=80,height=50)
phonebookBtn.place(x=505,y=380,width=80,height=50)

#원클릭 넣을 이미지라벨
oneclickimage = PhotoImage(file = "src/oneclick_logo.png")
imageLabel=Label(root, image=oneclickimage, relief="flat", bg="cornsilk")
imageLabel.place(x=158,y=40)

#휴게소 라벨
playimage = PhotoImage(file = "src/playroom.png")
playimagelabel=Label(root, image=playimage, relief="solid", bg="cornsilk")
playimagelabel.place(x=148,y=215)

#휴게소 버튼
omokbttn=Button(root, text="오목\n게임하기",relief="solid",borderwidth=1, bg="cornsilk",font=font)
updownbttn=Button(root, text="업다운\n게임하기", relief="solid",borderwidth=1, bg="cornsilk",font=font)
omokbttn.place(x=195,y=390,width=70,height=36)
updownbttn.place(x=345,y=390,width=70,height=36)

#휴게소 꽃 라벨
omokimage=PhotoImage(file = "src/flower.png")
omoklabel=Label(root, image=omokimage, relief="flat", bg="cornsilk")
omoklabel.place(x=175,y=401,width=30)

updownimage=PhotoImage(file = "src/flower.png")
updownlabel=Label(root, image=updownimage, relief="flat", bg="cornsilk")
updownlabel.place(x=325,y=401,width=30)

#클로버 이미지
homepageimage=PhotoImage(file = "src/clover.png")
homepagelabel=Label(root, image = homepageimage, relief="flat",bg="cornsilk")
homepagelabel.place(x=23, y=48, width=40 )

ecampusimage=PhotoImage(file = "src/clover.png")
ecampuslabel=Label(root, image = ecampusimage, relief="flat",bg="cornsilk")
ecampuslabel.place(x=23, y=118, width=40 )

dormimage=PhotoImage(file = "src/clover.png")
dormlabel=Label(root, image = dormimage, relief="flat",bg="cornsilk")
dormlabel.place(x=23, y=188, width=40 )

gaesinimage=PhotoImage(file = "src/clover.png")
gaesinlabel=Label(root, image = gaesinimage, relief="flat",bg="cornsilk")
gaesinlabel.place(x=23, y=258, width=40 )

siatimage=PhotoImage(file = "src/clover.png")
siatlabel=Label(root, image = siatimage, relief="flat",bg="cornsilk")
siatlabel.place(x=23, y=328, width=40 )

jobimage=PhotoImage(file = "src/clover.png")
joblabel=Label(root, image = jobimage, relief="flat",bg="cornsilk")
joblabel.place(x=18, y=398, width=40 )

#잎 라벨이미지
baekjunimage=PhotoImage(file="src/leaf.png")
baekjunlabel=Label(root, image=baekjunimage,relief="flat", bg="cornsilk")
baekjunlabel.place(x=475, y=40, width=40)

codeupimage=PhotoImage(file="src/leaf.png")
codeuplabel=Label(root, image=codeupimage,relief="flat", bg="cornsilk")
codeuplabel.place(x=475, y=110, width=40)

replitimage=PhotoImage(file="src/leaf.png")
replitlabel=Label(root, image=replitimage,relief="flat", bg="cornsilk")
replitlabel.place(x=475, y=180, width=40)

swimage=PhotoImage(file="src/leaf.png")
swlabel=Label(root, image=swimage,relief="flat", bg="cornsilk")
swlabel.place(x=475, y=250, width=40)

noticeimage=PhotoImage(file="src/leaf.png")
noticelabel=Label(root, image=noticeimage,relief="flat", bg="cornsilk")
noticelabel.place(x=475, y=320, width=40)

numberimage=PhotoImage(file="src/leaf.png")
numberlabel=Label(root, image=numberimage,relief="flat", bg="cornsilk")
numberlabel.place(x=475, y=390, width=40)

root.mainloop()