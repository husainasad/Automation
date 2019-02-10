from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('https://www.google.com/')
browser.maximize_window()
print(browser.get_window_size())
time.sleep(2)
browser.set_window_size(1024,768)
print(browser.get_window_size())
time.sleep(2)
browser.quit()