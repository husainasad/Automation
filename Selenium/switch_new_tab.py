import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.google.com/')
window = driver.window_handles[0]

# tab = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
# driver.get('https://www.wikipedia.org/')
# time.sleep(2)

# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
# time.sleep(2) 

# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
# time.sleep(2) 

driver.execute_script("window.open('', 'new window')")
driver.switch_to.window('new window')
driver.get('https://www.wikipedia.org/')
window2 = driver.window_handles[1]

driver.switch_to.window(window)
time.sleep(2)
driver.switch_to.window(window2)
time.sleep(2)
driver.close()