from selenium import webdriver
import time

url = "file:///C:\python\study_work\html\menu.html"
driver = webdriver.Chrome()
driver.get(url)

element = driver.find_element_by_link_text("Coffee")
element.click()
time.sleep(1)

driver.refresh()
time.sleep(1)

driver.back()
time.sleep(1)

driver.forward()
print(driver.current_url)
time.sleep(3)
driver.quit()