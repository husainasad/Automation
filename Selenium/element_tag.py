from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

try:
    driver.find_element_by_tag_name('form')
    print('Test Pass : Tag found')

except Exception as e:
    print("Exception found", format(e))

driver.close()  