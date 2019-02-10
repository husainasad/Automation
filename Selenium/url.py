from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

element = driver.find_element_by_link_text('About')
element.click()

print(driver.current_url)

driver.close()