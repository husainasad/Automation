from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

try:
    driver.find_element_by_id('gstyle')
    print('Test Pass : ID found')

except Exception as e:
    print("Exception found", format(e))

driver.close()        