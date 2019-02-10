from selenium import webdriver

driver =webdriver.Chrome()
driver.get('https://www.google.com/')

ids = driver.find_elements_by_xpath('//*[@class]')

for ii in ids:
    print(ii.get_attribute('class'))

driver.close() 
 