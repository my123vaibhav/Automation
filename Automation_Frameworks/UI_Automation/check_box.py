import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

list_of_checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(list_of_checkbox)

for i in range(len(list_of_checkbox)):
    if i%2==0:
        list_of_checkbox[i].click()

# for i in range(len(list_of_checkbox)):
#     list_of_checkbox[i].click()
#     time.sleep(2)

driver.close()





import sys
sys.exit(0)
sun=driver.find_element(By.ID,'sunday')
sun.click()
mon=driver.find_element(By.ID,'monday')
mon.click()
tue=driver.find_element(By.ID,'tuesday')
tue.click()
wen=driver.find_element(By.ID,'wednesday')
wen.click()
thu=driver.find_element(By.ID,'thursday')
thu.click()
fri=driver.find_element(By.ID,'friday')
fri.click()
sat=driver.find_element(By.ID,'saturday')
sat.click()
time.sleep(3)
driver.close()
