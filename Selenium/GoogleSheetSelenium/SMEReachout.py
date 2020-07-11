import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
# 
##options = FirefoxOptions()
##options.add_argument("--headless")
##driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe',options=options)
##driver.get("https://pythonbasics.org")

#driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe')
#driver.get("https://pythonbasics.org")
#

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"
         ]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open('SD 2.0 Tracker').worksheet('SME Pool - Reachout')

#data = sheet.get_all_records()
#cell = sheet.cell(167,2).value

driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe')
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

username = driver.find_element_by_id('username').send_keys('thilakan.sandeep@gmail.com')
password = driver.find_element_by_id('password').send_keys('CoViD2019')
login = driver.find_element_by_class_name('login__form_action_container')
login.click()

