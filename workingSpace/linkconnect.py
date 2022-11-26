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
root.geometry("300x300")

chromedriver_autoinstaller.install(True)                    # 크롬 드라이버 자동 설치
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)      # 창 꺼지지 않는 옵션
chrome_service = Service('chromedriver')
chrome_service.creationflags = 0x08000000                   # 명령 프롬프트창 안뜨게 하는 옵션

myId = '학번'
myPw = '비밀번호'

def ecampusLink() :
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('https://ecampus.chungbuk.ac.kr/')

    id = browser.find_element(By.XPATH,'//*[@id="uid"]')
    id.click()
    id.send_keys(myId)

    pw = browser.find_element(By.XPATH,'//*[@id="pswd"]')
    pw.click()
    pw.send_keys(myPw)

    browser.find_element(By.XPATH,'//*[@id="entry-login"]').click()


ecampusBtn = Button(root, text = "ecampus", font="나눔고딕 10", command = ecampusLink)
ecampusBtn.config(width = 20, height = 5)
tmpBtn = Button(root, text = "임시버튼", font="나눔고딕 10")
tmpBtn.config(width = 20, height = 5)
ecampusBtn.pack()
tmpBtn.pack()

root.mainloop() #위에서 생성한 객체.mainloop
