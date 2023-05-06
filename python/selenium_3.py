from selenium import webdriver
import time

url = "file:///C:\python\study_work\html\menu.html"
driver = webdriver.Chrome()
driver.get(url)

title = driver.title
print(title)

html = driver.page_source
print(html)

current = driver.current_url
print(current)

time.sleep(3)
driver.quit()
