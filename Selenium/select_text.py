from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element_by_css_selector('body')
time.sleep(5)
element.send_keys(Keys.CONTROL + 'a')
