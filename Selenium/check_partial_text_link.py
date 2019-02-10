from selenium import webdriver

driver =webdriver.Chrome()
driver.get('https://www.wikipedia.org/')

try:
    driver.find_element_by_partial_link_text('for')
    print('Test Pass: Element found by partial link text')

except Exception as e:
    print('Exception found', format(e)) 

driver.close()  