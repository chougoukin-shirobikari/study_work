from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "file:///C:\python\study_work\html\menu.html"
options = Options()
options.add_argument('--incognito')
options.add_argument('--window-size=500,300')

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)
driver.quit()