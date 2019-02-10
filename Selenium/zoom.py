from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

driver.execute_script("document.body.style_zoom = '50%'")