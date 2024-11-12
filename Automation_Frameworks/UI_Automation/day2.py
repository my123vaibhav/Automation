import random
print(random.randint(1,20))


for i in range(10):
    print(i)





import sys
sys.exit(0)
import time

from selenium import webdriver
import logging
from constant import *

driver=webdriver.Firefox()

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

time.sleep(2)
driver.close()











import sys
sys.exit(0)
def nevigation_of_pages(url1,url2):
    try:
        driver=webdriver.Firefox()
        driver.get(url1)
        driver.maximize_window()
        driver.save_screenshot('sample'+str(time.time())+'.png')
        if 'amazon' in driver.current_url:
            driver.get(url2)
            if 'flipkart' in driver.current_url:
                driver.back()
                driver.save_screenshot('sample'+str(time.time())+'.png')
                print('16',driver.current_url,driver.title)
                if 'amazon' in driver.current_url:
                    print('18',driver.current_url,driver.title)
                    driver.forward()
                    driver.save_screenshot('sample'+str(time.time())+'.png')
                    print('20',driver.current_url,driver.title)
            else:
                driver.save_screenshot('sample' + str(time.time()) + '.png')
                return False
        else:
            driver.save_screenshot('sample' + str(time.time()) + '.png')
            return False
    except Exception as e:
        print(e)
    finally:
        driver.close()

nevigation_of_pages(amazon_url,flipkart_url)