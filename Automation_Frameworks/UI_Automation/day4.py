import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By




list1=[]
driver=webdriver.Firefox()
driver.get("https://stepupandlearn.in/wp-content/UI/radiobutton.html")
list_of_radio=driver.find_elements(By.XPATH,"//input[@name='language']")
for i in list_of_radio:
    i.click()
    list1.append(i.get_attribute('value'))
    time.sleep(2)
    driver.save_screenshot('sample'+str(time.time())+'.png')
print(list1)
driver.close()











def click_on_radio_button(var1):
    try:
        driver = webdriver.Firefox()
        driver.get("https://stepupandlearn.in/wp-content/UI/radiobutton.html")
        locator_value = driver.find_element(By.XPATH, f"//input[@value='{var1}']")
        if not locator_value.is_selected():
            driver.maximize_window()
            locator_value.click()
            driver.save_screenshot(f'{var1}'+str(time.time())[:4]+'.png')
            return locator_value.is_selected()
        else:
            driver.maximize_window()
            driver.save_screenshot(f'{var1}' + str(time.time())[:4] + '.png')
            return True
    except Exception as e:
        print(e)
    finally:
        driver.close()








def check_box(male=None,female=None):
    try:
        driver=webdriver.Firefox()
        driver.get("https://demo.nopcommerce.com/register")
        male_locator=driver.find_element(By.XPATH,"//input[@value='M']")
        female_locator=driver.find_element(By.XPATH,"//input[@value='F']")
        time.sleep(2)
        if male:
            if not male_locator.is_selected():
                male_locator.click()
                driver.save_screenshot('maleselection.png')
                return male_locator.is_selected()
            else:
                return True
        if female:
            if not female_locator.is_selected():
                female_locator.click()
                driver.save_screenshot('femaleselection.png')
                return female_locator.is_selected()
            else:
                return True
    except Exception as e:
        print(e)
    finally:
        driver.close()