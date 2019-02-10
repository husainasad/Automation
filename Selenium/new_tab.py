from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# element = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# time.sleep(2)

driver.execute_script("window.open('https://en.wikipedia.org/wiki/Main_Page', 'new window')")
time.sleep(2)

driver.close()
