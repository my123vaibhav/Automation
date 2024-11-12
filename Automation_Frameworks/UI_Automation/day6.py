import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#//select[@id='dropdown']
def select_element_by_text(text=None):
    driver=webdriver.Firefox()
    driver.get('https://stepupandlearn.in/wp-content/UI/dropdown.html')
    driver.implicitly_wait(3)
    driver.maximize_window()
    drp=driver.find_element(By.XPATH,"//select[@id='dropdown']")
    opt=Select(drp)
    opt.select_by_visible_text(text)
    driver.save_screenshot('sample_'+text+'.png')
    time.sleep(2)
    driver.close()

def select_element_by_value(value=None):
    driver=webdriver.Firefox()
    driver.get('https://stepupandlearn.in/wp-content/UI/dropdown.html')
    driver.implicitly_wait(3)
    driver.maximize_window()
    drp=driver.find_element(By.XPATH,"//select[@id='dropdown']")
    opt=Select(drp)
    opt.select_by_value(value)
    driver.save_screenshot('sample_'+value+'.png')
    time.sleep(2)
    driver.close()

def select_element_by_index(index=None):
    driver=webdriver.Firefox()
    driver.get('https://stepupandlearn.in/wp-content/UI/dropdown.html')
    driver.implicitly_wait(3)
    driver.maximize_window()
    drp=driver.find_element(By.XPATH,"//select[@id='dropdown']")
    opt=Select(drp)
    opt.select_by_index(index)
    driver.save_screenshot('sample_'+str(index)+'.png')
    time.sleep(2)
    driver.close()


select_element_by_text('Java')
select_element_by_value('4')
select_element_by_index(2)










import sys

sys.exit(0)
driver=webdriver.Firefox()

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html')

driver.maximize_window()

driver.implicitly_wait(5)

drp=driver.find_element(By.XPATH,"//select[@id='RESULT_RadioButton-9']")
element=Select(drp)

#element.select_by_visible_text('Evening')

#element.select_by_index(3)

element.select_by_value('Radio-1')

time.sleep(3)



driver.close()