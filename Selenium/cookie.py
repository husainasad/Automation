from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')

# cookie = {'fruit' : 'pineapple', 'shake' : 'mango'}
# driver.add_cookie(cookie)

print(driver.get_cookies())