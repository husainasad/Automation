from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element_by_link_text("Technology")

actionChains = ActionChains(driver)
actionChains.context_click(element)
actionChains.send_keys(Keys.ARROW_DOWN)
actionChains.send_keys(Keys.ARROW_DOWN)
actionChains.send_keys(Keys.RETURN)
actionChains.perform()