import time
from selenium import webdriver

driver = webdriver.Chrome("F:/WebDev/Selenium/chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Main_Page")
print(driver.title)
time.sleep(8)
driver.quit()