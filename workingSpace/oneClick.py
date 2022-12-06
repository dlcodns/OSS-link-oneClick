from tkinter import *
import tkinter.font
from tkinter.ttk import Combobox
from tkinter import messagebox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_autoinstaller                           # 웹드라이버 자동
from selenium.webdriver.common.alert import Alert           # 팝업창 해결위해서
import os
import sys
import csv
import win32file            # https://gentlesark.tistory.com/112 conda 설치

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
root.geometry("620x450+100+100")
root.resizable(False,False)
root['bg']='#d4e157'

# 계정 초기화
myId = ''
myPw = ''

# 사용자 계정 정보
accountLabel=Label(root, text=" 비 로그인 이용 중 입니다. ", fg="blue", relief="solid")
accountLabel.place(x=230,y=170)

def setAccount(myId, myPw) :
    accountHeader = [['학번','비밀번호']]
    accountHeader.append([myId, myPw])
    writeCsv('userAccount.csv',accountHeader)

def writeAccount(myId, myPw):
    accountHeader = [['학번','비밀번호']]
    accountHeader.append([myId, myPw])
    win32file.SetFileAttributes('userAccount.csv', 0)
    writeCsv('userAccount.csv',accountHeader)

def readAccount():
    global myId, myPw
    tmp = []
    win32file.SetFileAttributes('userAccount.csv', 0)
    with open('userAccount.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp.append(row)
        if len(tmp) > 1 :
            for i in range(1, len(tmp)) :
                myId = tmp[i][0]
                myPw = tmp[i][1]
                if myId != '' and myPw != '' :
                    accountLabel.configure(text=" {} 님이 로그인 중 입니다. ".format(myId), fg="blue", relief="solid")
                    accountLabel.place(x=205, y=170)
                    win32file.SetFileAttributes('userAccount.csv', 2)
                
def writeCsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        accountHeader = csv.writer(f, delimiter = ',')
        accountHeader.writerows(the_list)
        win32file.SetFileAttributes(filename, 2)
try:
    with open('userAccount.csv') as f:
        readAccount()
except IOError:
    setAccount(myId, myPw)


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
    
def baekjuneWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://www.acmicpc.net/')
    
def codeupWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://www.codeup.kr/')

def replitWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://replit.com/')
    
def sojungWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://sw7up.cbnu.ac.kr/community/notice')
    
def majorWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://computer.cbnu.ac.kr/bbs/bbs.php?db=notice')

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
        messagebox.showerror("로그아웃", "로그인 되어있지 않습니다.")
    else :
        messagebox.showinfo("로그아웃", "로그아웃 되었습니다.")
        accountLabel.configure(text=" 비 로그인 이용 중 입니다. ", fg="blue", relief="solid")
        accountLabel.place(x=230,y=170)
        myId = ''
        myPw = ''

def duplicateLogin() :
    if myId != '' and myPw != '' :
            response = messagebox.askquestion(title="로그인 경고" , message = "이미 로그인이 되어있습니다.\n로그아웃하고 새로 로그인 하시겠습니까?" )
            if response == "yes" :
                logoutFunc()
                loginMenu()
    else :
        loginMenu()
                
                
# 로그인 창
def loginMenu() :
    if not windowOpen :
        loginWindow = Tk()
        loginWindow.title("로그인")
        loginWindow.geometry("280x130+600+190")
        loginWindow.resizable(width = False, height = False)
        loginWindow['bg']='cornsilk'
        whenOpen()
        loginWindow.bind('<Destroy>', whenClose)
     
        # 로그인 창에 들어갈 내용
        idLabel = Label(loginWindow, text="학번", bg='cornsilk')
        idEntry = Entry(loginWindow)
        pwLabel = Label(loginWindow, text="비밀번호", bg='cornsilk')
        pwEntry = Entry(loginWindow, show="*")
        loginBtn = Button(loginWindow, text="일회용 로그인", bg='lightblue',command=lambda:[loginFunc(idEntry.get(), pwEntry.get())])
        saveAccountBtn = Button(loginWindow, text="로그인 및 계정 저장", bg='lightblue',command=lambda:[saveLoginFunc(idEntry.get(), pwEntry.get())])

        def loginFunc(id, pw) :
            global myId, myPw
            if id == '' or pw == '' :
                messagebox.showerror("로그인 오류", "아이디와 비밀번호를 입력해주세요.")
                loginWindow.lift()
            else :
                myId = id
                myPw = pw
                messagebox.showinfo("일회용 로그인", "로그인 되었습니다.")
                loginWindow.destroy()
                accountLabel.configure(text=" {} 님이 로그인 중 입니다. ".format(myId), fg="blue", relief="solid")
                accountLabel.place(x=205, y=170)

        def saveLoginFunc(id, pw) :
            global myId, myPw
            if id == '' or pw == '' :
                messagebox.showerror("로그인 오류", "아이디와 비밀번호를 입력해주세요.")
                loginWindow.lift()
            else :
                myId = id
                myPw = pw
                messagebox.showinfo("일회용 로그인", "로그인 되었습니다.")
                writeAccount(myId, myPw)
                loginWindow.destroy()
                accountLabel.configure(text=" {} 님이 로그인 중 입니다. ".format(myId), fg="blue", relief="solid")
                accountLabel.place(x=205, y=170)
            
        idLabel.grid(row=0, column=0, padx=10, pady=10)
        idEntry.grid(row=0, column=1, padx=10, pady=10)
        pwLabel.grid(row=1, column=0, padx=10, pady=10)
        pwEntry.grid(row=1, column=1, padx=10, pady=10)
        loginBtn.grid(row=2, column=0, padx=10, pady=10)
        saveAccountBtn.grid(row=2, column=1, padx=10, pady=10)
        
        

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
menubar.add_cascade(label="로그인", command=lambda:[duplicateLogin()])
menubar.add_cascade(label="로그아웃", command=lambda:[logoutFunc()])
root.config(menu=menubar)

#폰트 설정
font=tkinter.font.Font(family="맑은고딕", size=10, weight="bold")

# exe 제작을 위한 이미지 경로 설정 함수
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#주소모음 버튼 이미지
#주소모음 버튼이미지
homepageImgPath=resource_path("src/homepage.png")
homepageImg=PhotoImage(file = homepageImgPath)
ecampusImgPath=resource_path("src/ecampus.png")
ecampusImg=PhotoImage(file = ecampusImgPath)
dormImgPath=resource_path("src/dorm.png")
dormImg=PhotoImage(file = dormImgPath)
gaesinImgPath=resource_path("src/gaesin.png")
gaesinImg=PhotoImage(file = gaesinImgPath)
cieatImgPath=resource_path("src/cieat.png")
cieatImg=PhotoImage(file = cieatImgPath)
jobImgPath=resource_path("src/job.png")
jobImg=PhotoImage(file = jobImgPath)

baekjunImgPath=resource_path("src/baekjun.png")
baekjunImg=PhotoImage(file = baekjunImgPath)
codeupImgPath=resource_path("src/codeup.png")
codeupImg=PhotoImage(file = codeupImgPath)
replitImgPath=resource_path("src/replit.png")
replitImg=PhotoImage(file = replitImgPath)
sojungImgPath=resource_path("src/sojung.png")
sojungImg=PhotoImage(file = sojungImgPath)
majorImgPath=resource_path("src/major.png")
majorImg=PhotoImage(file = majorImgPath)
phonebookImgPath=resource_path("src/phonebook.png")
phonebookImg=PhotoImage(file = phonebookImgPath)


#주소모음 절대위치
homepageBtn=Button(root, image = homepageImg,relief = "flat", bg="#d4e157",command=homepageAutoWindow)
homepageBtn.place(x=15,y=20,width=125,height=60)
ecampusBtn=Button(root, image = ecampusImg, relief = "flat", bg="#d4e157", command=ecampusAutoWindow)
ecampusBtn.place(x=15,y=90,width=125,height=60)
dormBtn=Button(root, image = dormImg, relief = "flat", bg="#d4e157", command=dormAutoWindow)
dormBtn.place(x=15,y=160,width=125,height=60)
gaesinBtn=Button(root, image = gaesinImg, relief = "flat", bg="#d4e157", command=geshinAutoWindow)
gaesinBtn.place(x=15,y=230,width=125,height=60)
cieatBtn=Button(root, image = cieatImg, relief = "flat", bg="#d4e157", command=cieatAutoWindow)
cieatBtn.place(x=15,y=300,width=125,height=60)
jobBtn=Button(root, image = jobImg, relief = "flat", bg="#d4e157", command=jobAutoWindow)
jobBtn.place(x=15,y=370,width=125,height=60)

baekjunBtn=Button(root, image = baekjunImg,relief = "flat", bg="#d4e157", command=baekjuneWindow)
baekjunBtn.place(x=475,y=20,width=125,height=60)
codeupBtn=Button(root, image = codeupImg, relief = "flat", bg="#d4e157", command=codeupWindow)
codeupBtn.place(x=475,y=90,width=125,height=60)
replitBtn=Button(root, image = replitImg, relief = "flat", bg="#d4e157", command=replitWindow)
replitBtn.place(x=475,y=160,width=125,height=60)
sojungBtn=Button(root, image = sojungImg, relief = "flat", bg="#d4e157", command=sojungWindow)
sojungBtn.place(x=475,y=230,width=125,height=60)
majorBtn=Button(root, image = majorImg, relief = "flat", bg="#d4e157", command=majorWindow)
majorBtn.place(x=475,y=300,width=125,height=60)
phonebookBtn=Button(root, image = phonebookImg, relief = "flat", bg="#d4e157", command=createNumberWindow)
phonebookBtn.place(x=475,y=370,width=125,height=60)

#주소모음 버튼
#homepageBtn=Button(root, text="충북대학교\n홈페이지", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=homepageAutoWindow)
#ecampusBtn=Button(root, text="충북대학교\necampus", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=ecampusAutoWindow)
#dormBtn=Button(root, text="충북대학교\n학생생활관", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=dormAutoWindow)
#geshinBtn=Button(root, text="충북대학교\n개신누리", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=geshinAutoWindow)
#cieatBtn=Button(root, text="충북대학교\n씨앗", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=cieatAutoWindow)
#jobBtn=Button(root, text="충북대학교\n취업지원본부", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=jobAutoWindow)

#baekjuneBtn=Button(root, text="백준", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=baekjuneWindow)
#codeupBtn=Button(root, text="코드업", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=codeupWindow)
#replitBtn=Button(root, text="replit", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=replitWindow)
#sojungBtn=Button(root, text="SW사업단\n공지사항", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=sojungWindow)
#majorBtn=Button(root, text="컴공\n공지사항", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=majorWindow)
#phonebookBtn=Button(root, text="충북대학교\n전화번호", bg="cornsilk", relief="solid", borderwidth=1, font=font, command=createNumberWindow)


#주소버튼 절대위치
#homepageBtn.place(x=55,y=30,width=80,height=50)
#ecampusBtn.place(x=55,y=100,width=80,height=50)
#dormBtn.place(x=55,y=170,width=80,height=50)
#geshinBtn.place(x=55,y=240,width=80,height=50)
#cieatBtn.place(x=55,y=310,width=80,height=50)
#jobBtn.place(x=55,y=380,width=80,height=50)

#baekjuneBtn.place(x=505,y=30,width=80,height=50)
#codeupBtn.place(x=505,y=100,width=80,height=50)
#replitBtn.place(x=505,y=170,width=80,height=50)
#sojungBtn.place(x=505,y=240,width=80,height=50)
#majorBtn.place(x=505,y=310,width=80,height=50)
#phonebookBtn.place(x=505,y=380,width=80,height=50)

#원클릭 로고
oneclickimagePath=resource_path("src/oneclick_logo.png")
oneclickimage = PhotoImage(file = oneclickimagePath)
imageLabel=Label(root, image=oneclickimage, relief="flat", bg="#d4e157")
imageLabel.place(x=160,y=40)

#휴게소 라벨
playimagePath=resource_path("src/playroom.png")
playimage = PhotoImage(file = playimagePath)
playimagelabel=Label(root, image=playimage, relief="solid", bg="cornsilk")
playimagelabel.place(x=148,y=215)

#휴게소 버튼
omokbttn=Button(root, text="오목\n게임하기",relief="solid",borderwidth=1, bg="cornsilk",font=font)
updownbttn=Button(root, text="업다운\n게임하기", relief="solid",borderwidth=1, bg="cornsilk",font=font)
omokbttn.place(x=195,y=390,width=70,height=36)
updownbttn.place(x=345,y=390,width=70,height=36)

#휴게소 꽃 라벨
flowerImgPath=resource_path("src/flower.png")
flowerImg = PhotoImage(file = flowerImgPath)

omoklabel=Label(root, image=flowerImg, relief="flat", bg="cornsilk")
omoklabel.place(x=175,y=401,width=30)

updownlabel=Label(root, image=flowerImg, relief="flat", bg="cornsilk")
updownlabel.place(x=325,y=401,width=30)




#클로버 이미지
#coloverImgPath=resource_path("src/clov.png")
#cloverImg = PhotoImage(file = coloverImgPath)

#homepagelabel=Label(root, image = cloverImg, relief="flat",bg="cornsilk")
#homepagelabel.place(x=23, y=48, width=40 )

#ecampuslabel=Label(root, image = cloverImg, relief="flat",bg="cornsilk")
#ecampuslabel.place(x=23, y=118, width=40 )

#dormlabel=Label(root, image = cloverImg, relief="flat",bg="cornsilk")
#dormlabel.place(x=23, y=188, width=40 )

#gaesinlabel=Label(root, image = cloverImg, relief="flat",bg="cornsilk")
#gaesinlabel.place(x=23, y=258, width=40 )

#siatlabel=Label(root, image = cloverImg, relief="flat",bg="cornsilk")
#siatlabel.place(x=23, y=328, width=40 )

#joblabel=Label(root, image = cloverImg, relief="flat",bg="cornsilk")
#joblabel.place(x=18, y=398, width=40 )

#잎 라벨이미지
#leafImgPath=resource_path("src/leaf.png")
#leafImg = PhotoImage(file = leafImgPath)

#baekjunlabel=Label(root, image=leafImg,relief="flat", bg="cornsilk")
#baekjunlabel.place(x=475, y=40, width=40)

#codeuplabel=Label(root, image=leafImg,relief="flat", bg="cornsilk")
#codeuplabel.place(x=475, y=110, width=40)

#replitlabel=Label(root, image=leafImg,relief="flat", bg="cornsilk")
#replitlabel.place(x=475, y=180, width=40)

#swlabel=Label(root, image=leafImg,relief="flat", bg="cornsilk")
#swlabel.place(x=475, y=250, width=40)

#noticelabel=Label(root, image=leafImg,relief="flat", bg="cornsilk")
#noticelabel.place(x=475, y=320, width=40)

#numberlabel=Label(root, image=leafImg,relief="flat", bg="cornsilk")
#numberlabel.place(x=475, y=390, width=40)

root.mainloop()
