import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# driver=webdriver.Firefox()
# driver.get('https://www.google.com/')
# driver.maximize_window()
# w=WebDriverWait(driver,5)
# search=driver.find_element(By.NAME,'q')
# w.until(EC.presence_of_element_located((By.NAME,'q')))
# search.send_keys('hi')
# search.submit()
#
# driver.close()




def search_data_in_google(data=None):
    try:
        driver=webdriver.Firefox()
        driver.get('https://www.google.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//textarea[@aria-label='Search']").send_keys(data)
        driver.find_element(By.XPATH,"//textarea[@aria-label='Search']").submit()
        if data in driver.current_url:
            driver.save_screenshot('searchdata.png')
            return True
        else:
            driver.save_screenshot('searchdata.png')
            return False
    except Exception as e:
        print(e)
    finally:
        driver.close()

print(search_data_in_google('987654456'))