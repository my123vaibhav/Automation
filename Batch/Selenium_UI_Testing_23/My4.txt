import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
str1='https://www.'
str2='.com/'
str3='name'
url=str1+str3+str2
#ram189@gmail.com
driver.get('https://www.facebook.com/')
driver.maximize_window()
n=driver.current_url
l=n.split('.')
print(l[1])


import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(2)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)



import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
before=time.time()
#print(before)
driver.get('https://itera-qa.azurewebsites.net/home/automation')
after=time.time()
#print(after)

driver.maximize_window()
time.sleep(2)
#select monday
#mon=driver.find_element(By.XPATH,"//input[@id='monday']") --->1
#mon.click()

#all checkbox select--->
#type='checkbox'  and contains(@id,'day')   ----> 7

list_day=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(list_day))
#select first 5 elements
#for i in range(len(list_day),len(list_day)-2):  #range(7)--->0 to 6
    #list_day[i].click()
    #time.sleep(2)
for i in range(0,len(list_day),3):  #range(7)--->0 to 6
    list_day[i].click()
    time.sleep(2)
list_day[0].click()
list_day[5].click()

'''
Monday  day
Tuesday day
Wednesday day
Thursday day
Friday   day
Saturday day
Sunday day
'''

time.sleep(3)


#//input[@id='monday']  ---->//input[@id='monday']