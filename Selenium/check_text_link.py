from selenium import webdriver

driver =webdriver.Chrome()
driver.get('https://www.google.com/')

try:
    driver.find_element_by_link_text('about')
    print('Test Pass: Element found by link text')

except Exception as e:
    print('Exception found', format(e)) 

driver.close()  