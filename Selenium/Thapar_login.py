import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

rno = input("Enter Roll Number")
pw = getpass.getpass("Enter Password")

webbrowser = webdriver.Chrome()
webbrowser.get('https://172.31.1.6:8090/')

# element_1 = webbrowser.find_element_by_partial_link_text('information')
# webbrowser.implicitly_wait(2)
# element_1.send_keys(Keys.ENTER)
# element_2 = webbrowser.find_element_by_partial_link_text('webpage')
# webbrowser.implicitly_wait(2)
# element_2.send_keys(Keys.ENTER)

username = webbrowser.find_element_by_id('username')
username.send_keys(rno)
webbrowser.implicitly_wait(2)
password = webbrowser.find_element_by_id('password')
password.send_keys(pw)
time.sleep(2)
login = webbrowser.find_element_by_id('loginbutton')
login.click()

