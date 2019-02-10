from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')

try:
    assert 'Wikipedia' in driver.title
    print('Assertion test passed')

except Exception as e:
    print('Assertion test failed', format(e))  

driver.close()  