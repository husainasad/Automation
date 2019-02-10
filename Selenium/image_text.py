from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

for element in driver.find_elements_by_tag_name('img'):
    print(element.text) 
    print(element.tag_name)
    print(element.location)
    print(element.size)   
driver.close()