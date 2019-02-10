from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

element = driver.find_element_by_link_text('About')
time.sleep(2)
element.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()