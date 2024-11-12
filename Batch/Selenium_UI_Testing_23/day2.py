import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
print('before click',driver.current_url)
time.sleep(2)
#driver.find_element(By.LINK_TEXT,'Register').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()
time.sleep(3)
driver.find_element(By.XPATH,'//h1[normalize-space()="Register"]')
print('after click',driver.current_url)

import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

obj=webdriver.Chrome()
obj.get('https://demo.nopcommerce.com/')
obj.maximize_window()

time.sleep(4)
search_obj=obj.find_element(By.ID,'small-searchterms')
search_obj.send_keys('Lenovo')
obj.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
time.sleep(2)