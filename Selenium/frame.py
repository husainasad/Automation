from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.wayver.media/")

driver.switch_to.frame('frame2')