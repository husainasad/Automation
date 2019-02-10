from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

element = driver.find_element_by_css_selector('body')
time.sleep(2)

element.send_keys('\uE035')