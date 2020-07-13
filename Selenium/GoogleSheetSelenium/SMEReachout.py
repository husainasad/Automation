import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
import getpass
from bs4 import BeautifulSoup
# 
##options = FirefoxOptions()
##options.add_argument("--headless")
##driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe',options=options)

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

#driver.get(sheet.cell(183,2).value)
driver.get('https://www.linkedin.com/in/sandeep-thilakan-30b7a513b/')

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

name_div = soup.find('div', {'class':'flex-1 mr5'})
name_loc =  name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()

name = name.split(" ")[0]

#exp_section = soup.find('section', {'id':'experience-section'})
#exp_section = exp_section.find('ul')
#li_tags = exp_section.find('div')
#a_tags = li_tags.find('a')
#job_title = a_tags.find('h3').get_text().strip()
#company = a_tags.find_all('p')[1].get_text().strip()

edu_section = soup.find('section', {'id':'education-section'})
university_name = edu_section.find('h3').get_text().strip()
degree_name = edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
degree_year = edu_section.find('p',{'class':'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[1].find_all('time')[1].get_text().strip()

driver.find_element_by_class_name('pv-s-profile-actions').click()
driver.find_element_by_xpath('//button[@class="mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view"]').click()

custom_msg = 'Hello ' + name + '\nWe, at upGrad, are looking for SMEs for our upcoming online software development programs. We believe that it’s an ideal opportunity for us to make rigorous higher education accessible to a wider audience. This will be a part-time engagement, and we will be working remotely.Thanks!'
msg_space = driver.find_element_by_id('custom-message')
msg_space.send_keys(custom_msg)
driver.find_element_by_class_name('ml1').click()


#start = input("Enter start of row")
#
#cell = sheet.cell(start,2).value
#
#while (cell!=""):
#    cell = sheet.cell(start,2).value
#    autofill(start,cell)
#    start+=1