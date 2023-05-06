from selenium import webdriver
import time

url = "file:///C:\python\study_work\html\menu.html"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.quit()