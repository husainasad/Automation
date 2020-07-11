import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
import getpass
from parsel import Selector
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
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open('SD 2.0 Tracker').worksheet('SME Pool - Reachout')


emailid = input("Enter emailid")
pw = getpass.getpass("Enter Password")

driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe')
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


username = driver.find_element_by_id('username').send_keys(emailid)
password = driver.find_element_by_id('password').send_keys(pw)

login = driver.find_element_by_class_name('login__form_action_container')
login.click()

driver.get(sheet.cell(185,2).value)

sel = Selector(text=driver.page_source)
name = sel.xpath('//*[@class="inline t-24 t-black t-normal break-words"]/text()').extract_first().strip()
job_title = sel.xpath('//*[@class="mt1 t-18 t-black t-normal break-words"]/text()').extract_first().strip()

qualification = sel.xpath('//*[@class="pv-entity__degree-info"]/text()').extract_first().strip()
experience = sel.xpath('//*[contains(@class, "pv-entity__dates t-14 t-black--light t-normal")]/text()').extract_first().strip()


#def autofill(rowno, link):
#    driver.get(link)
#    name = driver.find_element_by_class_name('inline.t-24.t-black.t-normal.break-words')
#
#start = input("Enter start of row")
#
#cell = sheet.cell(start,2).value
#
#while (cell!=""):
#    cell = sheet.cell(start,2).value
#    autofill(start,cell)
#    start+=1