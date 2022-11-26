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
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])           # 로그 제거
chrome_service = Service('chromedriver')
chrome_service.creationflags = 0x08000000                   # 명령 프롬프트창 안뜨게 하는 옵션

myId = '학번'
myPw = '비밀번호'

# ----------------------------------------------------------------------------------------
# 링크 부분

def ecampusWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://ecampus.chungbuk.ac.kr/')

def homepageWindow() :
    args = ["hide_console", ]
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://cbnu.ac.kr/')
    
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
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://ecampus.chungbuk.ac.kr/')

    id = browser.find_element(By.XPATH,'//*[@id="uid"]')
    id.click()
    id.send_keys(myId)

    pw = browser.find_element(By.XPATH,'//*[@id="pswd"]')
    pw.click()
    pw.send_keys(myPw)

    browser.find_element(By.XPATH,'//*[@id="entry-login"]').click()


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

ecampusBtn.grid(row=0, column=0, padx=5, pady=3)
homepageBtn.grid(row=1, column=0, padx=5, pady=3)
cieatBtn.grid(row=2, column=0, padx=5, pady=3)
dormBtn.grid(row=3, column=0, padx=5, pady=3)
geshinBtn.grid(row=4, column=0, padx=5, pady=3)
jobBtn.grid(row=5, column=0, padx=5, pady=3)

root.mainloop() #위에서 생성한 객체.mainloop
