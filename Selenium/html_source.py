from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')

html_source = driver.page_source

print(html_source)