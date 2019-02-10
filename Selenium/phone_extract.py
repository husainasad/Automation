from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('http://www.airindia.in/customer-support.htm')

doc = driver.page_source

phones =re.findall(r'[\d]{3}-[\d]{8}', doc)

for phone in phones:
    print(phone)