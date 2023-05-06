from selenium import webdriver
import time

url = "file:///C:\python\study_work\html\menu.html"
driver = webdriver.Chrome()
driver.get(url)

tags_h1 = driver.find_elements_by_tag_name('h1')
for h1 in tags_h1:
    print(h1.text)

tags_a = driver.find_elements_by_tag_name('a')
for a in tags_a:
    print(a.text + "" + a.get_attribute("href"))

print(len(driver.find_elements_by_tag_name("ul")))
print(len(driver.find_elements_by_tag_name("li")))
print(driver.find_elements_by_tag_name("ul")[0].text)
print(driver.find_elements_by_tag_name("a")[1].text)

time.sleep(1)
driver.find_elements_by_tag_name("a")[1].click()
time.sleep(3)
driver.quit()