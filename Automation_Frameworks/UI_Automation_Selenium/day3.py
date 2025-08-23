
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

#driver.find_element(By.LINK_TEXT,'Register').click()

driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()

print(driver.current_url)
driver.close()






import sys
sys.exit(0)
def search_data(input_data=None):
    try:
        driver=webdriver.Firefox()
        driver.get('https://demo.nopcommerce.com/')
        driver.maximize_window()
        element=driver.find_element(By.NAME,"q")
        if element.is_displayed():
            element.send_keys(input_data)
            time.sleep(3)
            driver.find_element(By.XPATH,'//button[@type="submit"]').click()
            time.sleep(3)
            if 'hi+good' in driver.current_url:
                driver.save_screenshot('sample22.png')
                return True
            else:
                return False
    except Exception as e:
        print(f'this is the {e}')
    finally:
        driver.quit()

