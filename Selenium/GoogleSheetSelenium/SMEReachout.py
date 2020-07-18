import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
import getpass
from bs4 import BeautifulSoup
import datetime
import time
from selenium.common.exceptions import NoSuchElementException
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


#def next_available_row(Sheet):
#    str_list = list(filter(None, Sheet.col_values(1)))
#    return str(len(str_list)+1)

def next_available_row(sheet):
    cols_to_sample = 2
    cols = sheet.range(1, 1, sheet.row_count, cols_to_sample)
    return max([cell.row for cell in cols if cell.value]) + 1

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
    #    driver.find_element_by_class_name('ml1').click()
    except:
        print("error in connecting")
    


def fillSheet(new_row,query,page_no):
    time.sleep(2)
    link = driver.current_url
    sheet.update_cell(new_row, 2, link)
    
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    try:
        name_div = soup.find('div', {'class':'flex-1 mr5'})
        name_loc =  name_div.find_all('ul')
        name = name_loc[0].find('li').get_text().strip()
        sheet.update_cell(new_row, 1, name)
    except:
        print("error in name section")
    

    try:
        exp_section = soup.find('section', {'id':'experience-section'})
        exp_section = exp_section.find('ul')
        li_tags = exp_section.find('div')
        a_tags = li_tags.find('a')
        job_title = a_tags.find('h3').get_text().strip()
        sheet.update_cell(new_row, 20, job_title) 
        
        company = a_tags.find_all('p')[1].get_text().strip()
        sheet.update_cell(new_row, 19, company) 
    except:
        profile_title = name_div.find('h2').get_text().strip()
        try:
            job_title, company = profile_title.split(" at ")
            sheet.update_cell(new_row, 19, company)
            sheet.update_cell(new_row, 20, job_title)
        except:
            sheet.update_cell(new_row, 20, profile_title)
        
            
    try:
        edu_section = soup.find('section', {'id':'education-section'})
        university_name = edu_section.find('h3').get_text().strip()
        degree_name = edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
        qualification = degree_name + "," + university_name
        sheet.update_cell(new_row, 21, qualification) 
    except:
        print("error in education section")
    
    try:
        degree_year = edu_section.find('p',{'class':'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[1].find_all('time')[1].get_text().strip()
        now = datetime.datetime.now()
        experience = now.year - int(degree_year)
        sheet.update_cell(new_row, 22, experience)
    except:
        print("error in degree year")
    
    sheet.update_cell(new_row, 5, 'LinkedIn')
    
    rdate = datetime.date.today()
    rdate = rdate.strftime("%d/%b/%Y")
    sheet.update_cell(new_row, 6, rdate)
    
    sheet.update_cell(new_row, 7, 'Selenium')
    
    sheet.update_cell(new_row, 23, query)
    
    for  x in range(8,19):
        sheet.update_cell(new_row, x, 'NA')
    
    sheet.update_cell(new_row, 26, 'Not-Replied')
    sheet.update_cell(new_row, 32, page_no)
    
    name = name.split(" ")[0]
    connectMsg(name)
    
def getProfiles(profile_list ):
    profiles = []
    soup = BeautifulSoup(driver.page_source)
    profile_results = soup.find('ul', {'class': 'search-results__list list-style-none'})
    results = profile_results.find_all('li', {'class': 'search-result search-result__occluded-item ember-view'})
    for result in results:
        userID = result.find('a', {'class': 'search-result__result-link ember-view'}).get('href')
        profiles.append(userID)
    
#    driver.execute_script("window.scrollTo(0, 750)") 
#    time.sleep(5)    
    results_next = profile_results.find_all('li', {'class': 'search-result search-result__occluded-item search-result__occlusion-hint ember-view'})
    for result in results_next:
        userID = result.find('a', {'class': 'search-result__result-link ember-view'}).get('href')
        profiles.append(userID)
    
    return profiles

query = input("Enter the area of expertise: ")
page_no = input("Enter the page number to be searched: ")
driver = webdriver.Firefox(executable_path='F:\Projects\Automation\Selenium\geckodriver.exe')
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

emailid = input("Enter emailid")
pw = getpass.getpass("Enter Password")
   
username = driver.find_element_by_id('username').send_keys(emailid)
password = driver.find_element_by_id('password').send_keys(pw)


login = driver.find_element_by_class_name('login__form_action_container')
login.click()

base_url = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221009%22%2C%221028%22%2C%221035%22%2C%222382910%22%2C%221068%22%2C%2211174522%22%2C%221441%22%2C%221482%22%2C%221586%22%2C%22162479%22%2C%22165158%22%2C%221666%22%2C%221753%22%2C%222340144%22%2C%222646%22%2C%222751%22%2C%222988%22%2C%2231513022%22%2C%223545%22%2C%229390173%22%5D&facetGeoRegion=%5B%22in%3A0%22%5D&facetNetwork=%5B%22S%22%2C%22O%22%5D&keywords='
driver.get(base_url + 'fullstack developer' + '&page=3' )
driver.get(base_url + query + '&page=' + str(page_no))
driver.implicitly_wait(5)


profile_list = []

profile_list = getProfiles(profile_list)

while profile_list:
    profile = profile_list.pop()
    profile_link = 'https://www.linkedin.com/' + profile
    driver.get(profile_link)
    try:
        connect_btn = driver.find_element_by_class_name('pv-s-profile-actions--connect')
        if connect_btn.is_enabled():
            fillSheet(next_available_row(sheet), query, page_no)
    except:
        driver.find_element_by_class_name('pv-s-profile-actions__overflow-toggle').click()
        connect_btn = driver.find_element_by_class_name('pv-s-profile-actions--connect')
        if connect_btn.is_enabled():
            fillSheet(next_available_row(sheet), query, page_no)

#driver.quit()