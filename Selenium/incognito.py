from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.wikipedia.org/')
time.sleep(2)

driver.close()