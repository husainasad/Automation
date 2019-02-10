from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://google.com')

element = driver.find_element_by_link_text('About')

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .perform()

time.sleep(2) 
driver.close()

