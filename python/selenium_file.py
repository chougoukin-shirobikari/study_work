from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

url = "file:///C:/python/study_work/html/file.html"
driver = webdriver.Chrome()
driver.get(url)
upfile = r"C:/python/study_work/html/text.txt"

driver.find_element_by_name("filename").send_keys(upfile)
time.sleep(3)
driver.quit()