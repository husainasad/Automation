import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser =webdriver.Chrome()
browser.get('https://www.google.com/')
time.sleep(2)
search = browser.find_element_by_name('q')
search.send_keys('Python 3')
search.send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_name('q').clear()
time.sleep(2)
browser.close()
