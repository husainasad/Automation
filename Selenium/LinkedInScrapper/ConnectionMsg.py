import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
import getpass
import time

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open('SD 2.0 Tracker').worksheet('SME Pool - Reachout')

def connectMsg(Name):
    try:
        try:
            driver.find_element_by_class_name('pv-s-profile-actions--connect').click()
        except:
            driver.find_element_by_class_name('pv-s-profile-actions__overflow-toggle').click()
            driver.find_element_by_class_name('pv-s-profile-actions--connect').click()
        driver.find_element_by_xpath('//button[@class="mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view"]').click()

        custom_msg = 'Hello ' + Name + '\nWe, at upGrad, are looking for SMEs for our upcoming online software development programs. We believe that it’s an ideal opportunity for us to make rigorous higher education accessible to a wider audience. This will be a part-time engagement, and we will be working remotely.Thanks!'
        msg_space = driver.find_element_by_id('custom-message')
        msg_space.send_keys(custom_msg)
        driver.find_element_by_class_name('ml1').click()
    except:
        print("error in sending connection message")

srow = int(input("Enter Starting Row "))
erow = int(input("Enter Ending Row ")) + 1


driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe')
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

emailid = input("Enter emailid")
pw = getpass.getpass("Enter Password")
   
username = driver.find_element_by_id('username').send_keys(emailid)
password = driver.find_element_by_id('password').send_keys(pw)


login = driver.find_element_by_class_name('login__form_action_container')
login.click()

for i in range(srow, erow):
    name = sheet.cell(i,1).value
    name = name.split(" ")[0]
    link = sheet.cell(i, 2).value
    driver.get(link)
    time.sleep(2)
    connectMsg(name)
    sheet.update_cell(i, 3, 'Y')
    
#driver.quit()