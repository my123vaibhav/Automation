
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://www.google.com/')
driver.implicitly_wait(6)
driver.maximize_window()
search=driver.find_element(By.NAME,'q')
#print(search.is_displayed())
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.NAME, "q")))
search.send_keys('hi')
search.submit()
time.sleep(3)
driver.close()

#
wait.until(EC.presence_of_element_located(driver.find_element(By.NAME,'q')))
#(1,2) 0--->1  1--->2
#((1,2)) 0--->(1,2)

import sys
sys.exit(0)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.get('https://www.google.com/')

object_wait=WebDriverWait(driver,4)   #__init__(self,driver,time)
search_box=driver.find_element(By.NAME,'q')
object_wait.until(EC.presence_of_element_located(search_box))
#search_box=driver.find_element(By.NAME,'q')
search_box.send_keys('facebook')






import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(5)
male_locator=driver.find_element(By.XPATH,'//input[@id="gender-male"]')
female_locator=driver.find_element(By.XPATH,'//input[@id="gender-female"]')

#print(male_locator.is_enabled())
if male_locator.is_enabled():
    male_locator.click()
time.sleep(3)

import sys
sys.exit(0)
print(male_locator.is_displayed())
print(female_locator.is_displayed())
print(male_locator.is_selected())
print(female_locator.is_selected())
male_locator.click()
print('after the male opt selected')
print(male_locator.is_selected())   #T
print(female_locator.is_selected()) #F
time.sleep(2)
female_locator.click()
print('after the female opt selected')
print(male_locator.is_selected())   #F
print(female_locator.is_selected()) #T
time.sleep(2)
import sys
sys.exit(0)
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
#driver.get('https://demo.nopcommerce.com/')
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
#v=driver.find_elements(By.TAG_NAME,'a')
v=driver.find_elements(By.CLASS_NAME,'form-check-input')
print(len(v))

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
print('before click',driver.current_url)     #https://demo.nopcommerce.com/
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()
print('after click',driver.current_url)     #https://demo.nopcommerce.com/register?returnUrl=%2Fsearch%3Fq%3Dlevono
time.sleep(2)
driver.back()
print('after back',driver.current_url)   #https://demo.nopcommerce.com/
driver.forward()
print('after forword',driver.current_url)   ##https://demo.nopcommerce.com/register?returnUrl=%2Fsearch%3Fq%3Dlevono
time.sleep(2)
driver.refresh()
print('after refresh',driver.current_url)   ##https://demo.nopcommerce.com/register?returnUrl=%2Fsearch%3Fq%3Dlevono
time.sleep(2)
time.sleep(2)


import sys
sys.exit(0)
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

drive=webdriver.Chrome()

drive.get('https://demo.nopcommerce.com/')
str1=drive.page_source
print(str1)

import sys
sys.exit(0)
#print(drive.page_source)
n='nopCommerce demo store'
if drive.title==n:
    print('pass')