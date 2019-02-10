from selenium import webdriver

driver =webdriver.Chrome()
driver.get('https://www.google.com/')

try:
    driver.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[2]/a')
    print('Test Pass: Link text class by xpath found')

except Exception as e:
    print('Exception found', format(e)) 

driver.close()  