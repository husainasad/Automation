from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

driver.execute_script("window.alert('This is an alert');")
time.sleep(5)
alert = driver.switch_to_alert()
alert.accept()
# alert.dismiss()