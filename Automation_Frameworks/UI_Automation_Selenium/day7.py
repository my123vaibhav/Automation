import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def check_alerts(*args):
    try:
        '''
        args[0] -type_alert
        args[1] - accept
        args[2] -dismiss
        args[3] -data
        args[4]- value
        '''
        driver=webdriver.Firefox()
        driver.get('https://stepupandlearn.in/wp-content/UI/javascript_alerts.html')
        driver.maximize_window()
        driver.implicitly_wait(5)
        if args[0][0]=='confirmation':
            pop1=driver.find_element(By.XPATH,f"//button[normalize-space()='{args[0][4]}']")
            if pop1.is_displayed():
                pop1.click()
                var1 = driver.switch_to.alert
                if args[0][1]:
                    var1.accept()
                    element = driver.find_element(By.XPATH, "//*[@id='result']")
                    if 'Ok' in element.text:
                        driver.save_screenshot('confimation.png')
                        return True
                    else:
                        return False
        if args[0][0]=='info':
            pop1 = driver.find_element(By.XPATH, f"//button[normalize-space()='{args[0][4]}']")
            pop1.click()
            var1=driver.switch_to.alert
            var1.accept()
            element = driver.find_element(By.XPATH, "//*[@id='result']")
            if args[0][3] in element.text:
                driver.save_screenshot('info.png')
                return True
            else:
                return False
        if args[0][0]=='input':
            pop1 = driver.find_element(By.XPATH, f"//button[normalize-space()='{args[0][4]}']")
            pop1.click()
            var1 = driver.switch_to.alert
            var1.send_keys(f'{args[0][3]}')
            var1.accept()
            element = driver.find_element(By.XPATH, "//*[@id='result']")
            if args[0][3] in element.text:
                driver.save_screenshot('input.png')
                return True
            else:
                return False
    except Exception as e:
        print(e)
    finally:
        driver.close()
