from selenium import webdriver
import time

url = "file:///C:/python/study_work/html/tea.html"
driver = webdriver.Chrome()
driver.get(url)

if driver.find_elements_by_css_selector("input[name='included'][svalue='cream']"):
    element = driver.find_element_by_css_selector("input[name='included'][value='cream']")
else:
    element = driver.find_element_by_css_selector("input[name='included'][value='lemon']")

element.click()
time.sleep(3)
driver.quit()