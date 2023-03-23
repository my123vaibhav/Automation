'''
Alerts/PopUp

text ----> text of al
accept()---> ok click
dismiss()----> cancel click

driver.switch_to.alert ----> enable the context

1st al----->xpath-->//button[normalize-space()='Click for JS Alert']

Authentication alert---->
web appli---> admin/password

url

authe alr--->

https://username:password@urls

coding--->UI
abstraction end user--->

context----> will on same page

driver.save_as_screenshot('sample.png')--->

scrolldown(X,Y)--->
driver.send_keys('filepath.pdf')----> upload the file

** How to handle mutiple windows in automation**
** Open pyxl     -----> data drven framework

** Mouse actions--->

**requests ----> postman(akshay)
** Open py xl---->

**unittest
**pytest
** database

** PRoject

'''''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.save_screenshot('ram.png')
driver.maximize_window()
time.sleep(3)
driver.switch_to.new_window('window')
driver.get('https://www.facebook.com/')
time.sleep(3)
driver.save_screenshot('sample.png')

import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
time.sleep(3)
driver.switch_to.new_window('tab') #context/ to open new tab on same browser
driver.get('https://www.facebook.com/')
time.sleep(3)



import sys
sys.exit(0)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.maximize_window()
time.sleep(30)







import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

#pop1=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
#pop1=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
pop1=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
pop1.click()
time.sleep(3)
var1=driver.switch_to.alert
var1.send_keys('Hi good morning')
var1.accept()

#var1.accept()
#var1.dismiss()
time.sleep(3)





import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()
drp_list=driver.find_element(By.XPATH,"//select[@id='input-country']")
drp=Select(drp_list)    #dropdown ko active
# 3 method to select the dropdown
#select_by_visible_text('' )---> visible text on UI

#drp.select_by_visible_text('China')

#select_by_index() ---> 0 to len-1

#drp.select_by_index(8)
drp.select_by_value('100')

time.sleep(2)
driver.close()




import sys
sys.exit(0)
s=drp.options
#print(len(s))
for i in s:
    print(i)