from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.zkoss.org/zkdemo/input/checkbox')

for i in browser.find_elements_by_xpath("//*[@type='checkbox']"):
    i.click()
    

time.sleep(2)
browser.quit()