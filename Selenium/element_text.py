from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element_by_id('mp-dyk')
print(element.text)