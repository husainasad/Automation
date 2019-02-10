from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()