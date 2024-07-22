import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

serviceToBeUsed=Service("C:\\Users\\MSUSERSL123\\PythonAutomation\\chromedriver.exe")
driver=webdriver.Chrome(service=serviceToBeUsed)
driver.get("https://www.youtube.com/@rahuketukiduniya/shorts")
time.sleep(5)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(10)
try:
    element = driver.find_element(By.XPATH,"//*[@id=\"yDmH0d\"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]")
    element.click()
    time.sleep(20)
except:
    print("not working")
goToShorts = driver.find_element(By.XPATH,"//*[@id=\"thumbnail\"]/yt-image/img")
goToShorts.click()
time.sleep(10)
try:
    i=0
    j=1
    while(True):
        while(j<33):
            elementNext=driver.find_element(By.XPATH,"//*[@id=\"navigation-button-down\"]/ytd-button-renderer/yt-button-shape/button")
            elementNext.click()
            j=j+1
            time.sleep(20)
        while(j!=1):
            elementP = driver.find_element(By.XPATH,"//*[@id=\"navigation-button-up\"]/ytd-button-renderer/yt-button-shape/button")
            elementP.click()
            j=j-1
            time.sleep(20)
except:
    print("working")
