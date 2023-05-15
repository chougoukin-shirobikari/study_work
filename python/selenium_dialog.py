from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

url = "file:///C:/python/study_work/html/dialog.html"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id("alert").click()
time.sleep(1)
Alert(driver).dismiss()

driver.find_element_by_id("confirm").click()
time.sleep(1)
Alert(driver).dismiss()

driver.find_element_by_id("prompt").click()
time.sleep(1)
Alert(driver).send_keys("てすと")
Alert(driver).accept()
time.sleep(1)
Alert(driver).accept()
time.sleep(3)
driver.quit()