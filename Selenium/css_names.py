from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

ids = driver.find_elements_by_xpath('//*[@name]')
for ii in ids:
    print(ii.get_attribute('name'))
    
driver.close()