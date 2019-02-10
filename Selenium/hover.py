from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element_by_link_text("Technology")

hover = ActionChains(driver).move_to_element(element)

hover.perform()
