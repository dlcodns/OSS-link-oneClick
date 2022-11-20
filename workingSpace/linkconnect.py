from tkinter import *
from selenium.webdriver.common.keys import Keys
#웹드라이버 자동
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver


root = Tk()
root.title("임시")
root.geometry("300x300")


def ecampusLink() :
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    browser.get('https://ecampus.chungbuk.ac.kr/')


ecampusBtn = Button(root, text = "ecampus", font="나눔고딕 10", command = ecampusLink)
ecampusBtn.config(width = 20, height = 5)
tmpBtn = Button(root, text = "임시버튼", font="나눔고딕 10")
tmpBtn.config(width = 20, height = 5)
ecampusBtn.pack()
tmpBtn.pack()

root.mainloop() #위에서 생성한 객체.mainloop
