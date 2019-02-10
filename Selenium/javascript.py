from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

driver.execute_script("window.alert('This is an alert');")