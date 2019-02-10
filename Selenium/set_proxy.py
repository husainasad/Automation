from selenium import webdriver
import time

PROXY = "124.108.18.10:8080"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://whatismyipaddress.com")
time.sleep(2)

chrome.close()

