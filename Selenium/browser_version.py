from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

print(driver.capabilities['version'])

driver.close()