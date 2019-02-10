from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get('https://www.google.com/')

ids = driver.find_elements_by_xpath('//*[@href]')

for ii in ids:
    print(ii.get_attribute('href'))

time.sleep(3)
driver.close()