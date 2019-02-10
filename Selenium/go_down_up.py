from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')

element = driver.find_element_by_tag_name('html')
element.send_keys(Keys.END)
time.sleep(2)
element.send_keys(Keys.HOME)
time.sleep(2)
driver.quit()