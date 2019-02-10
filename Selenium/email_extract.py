from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('http://www.airindia.in/customer-support.htm')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for email in emails:
    print(email)