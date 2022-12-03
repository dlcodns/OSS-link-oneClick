from tkinter import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

root = Tk()
root.title("임시")
root.geometry("300x400")

chromedriver_autoinstaller.install(True)                    # 크롬 드라이버 자동 설치
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)      # 창 꺼지지 않는 옵션
chrome_options.add_argument('incognito')                    # 시크릿 모드로 실행
chrome_options.add_argument('start-maximized')              # 창 최대화
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'disable-popup-blocking'])           # 로그 제거 및 팝업 차단
chrome_service = Service('chromedriver')
chrome_service.creationflags = 0x08000000                   # 명령 프롬프트창 안뜨게 하는 옵션

myId = ''
myPw = ''

# ----------------------------------------------------------------------------------------
# 링크 부분

def ecampusWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://ecampus.chungbuk.ac.kr/')

def homepageWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://www.chungbuk.ac.kr/')
    
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

def geshinAutoWindow() :
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
   
# Menu Bar
menubar = Menu(root)
menubar.add_cascade(label="로그인", command=lambda:[loginMenu()])
menubar.add_cascade(label="로그아웃", command=lambda:[logoutFunc()])
root.config(menu=menubar)

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
        
    
# 그냥 링크 버튼
ecampusBtn = Button(root, text = "ecampus", font="나눔고딕 10", command = ecampusWindow)
ecampusBtn.config(width = 10, height = 3)
homepageBtn = Button(root, text = "홈피", font="나눔고딕 10", command = homepageWindow)
homepageBtn.config(width = 10, height = 3)
cieatBtn = Button(root, text = "씨앗", font="나눔고딕 10", command = cieatWindow)
cieatBtn.config(width = 10, height = 3)
dormBtn = Button(root, text = "학생생활관", font="나눔고딕 10", command = dormWindow)
dormBtn.config(width = 10, height = 3)
geshinBtn = Button(root, text = "개신누리", font="나눔고딕 10", command = geshinWindow)
geshinBtn.config(width = 10, height = 3)
jobBtn = Button(root, text = "취업지원본부", font="나눔고딕 10", command = jobWindow)
jobBtn.config(width = 10, height = 3)

# 자동로그인 버튼
ecampusAutoBtn = Button(root, text = "ecampus A", font="나눔고딕 10", command = ecampusAutoWindow)
ecampusAutoBtn.config(width = 10, height = 3)
homepageAutoBtn = Button(root, text = "홈피 A", font="나눔고딕 10", command = homepageAutoWindow)
homepageAutoBtn.config(width = 10, height = 3)
cieatAutoBtn = Button(root, text = "씨앗 A", font="나눔고딕 10", command = cieatAutoWindow)
cieatAutoBtn.config(width = 10, height = 3)
dormAutoBtn = Button(root, text = "학생생활관 A", font="나눔고딕 10", command = dormAutoWindow)
dormAutoBtn.config(width = 10, height = 3)
geshinAutoBtn = Button(root, text = "개신누리 A", font="나눔고딕 10", command = geshinAutoWindow)
geshinAutoBtn.config(width = 10, height = 3)
jobAutoBtn = Button(root, text = "취업지원본부 A", font="나눔고딕 10", command = jobAutoWindow)
jobAutoBtn.config(width = 10, height = 3)

ecampusBtn.grid(row=0, column=0, padx=5, pady=3)
homepageBtn.grid(row=1, column=0, padx=5, pady=3)
cieatBtn.grid(row=2, column=0, padx=5, pady=3)
dormBtn.grid(row=3, column=0, padx=5, pady=3)
geshinBtn.grid(row=4, column=0, padx=5, pady=3)
jobBtn.grid(row=5, column=0, padx=5, pady=3)

ecampusAutoBtn.grid(row=0, column=1, padx=5, pady=3)
homepageAutoBtn.grid(row=1, column=1, padx=5, pady=3)
cieatAutoBtn.grid(row=2, column=1, padx=5, pady=3)
dormAutoBtn.grid(row=3, column=1, padx=5, pady=3)
geshinAutoBtn.grid(row=4, column=1, padx=5, pady=3)
jobAutoBtn.grid(row=5, column=1, padx=5, pady=3)

root.mainloop() #위에서 생성한 객체.mainloop
