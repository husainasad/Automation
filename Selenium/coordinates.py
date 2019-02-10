from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')

location = element.location
size = element.size
print(location)
print(size)
driver.close()