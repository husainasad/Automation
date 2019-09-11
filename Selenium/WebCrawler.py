import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re,os,codecs
query=input("Enter your search query:\n")
# number=input("Enter number of paragraphs:\n")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
driver=webdriver.Chrome(options=options)

tabUrl="https://en.wikipedia.org/wiki/"
driver.get(tabUrl+query)

paragraphs = driver.find_elements_by_tag_name('p')
file=[]

for p in paragraphs:
	file.append(p.text)

exp=r'\[[0-9]+\]'

file2=[]

for words in file:
	file2.append(re.sub(exp," ",words))

f = codecs.open("websearch.txt", "w", encoding="utf8")
for w in file2:
	f.write(w)
	
f.close()
os.system("notepad.exe websearch.txt")