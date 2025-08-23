import time
from selenium import webdriver


d=webdriver.Firefox()
d.get('https://stepupandlearn.in/admission-enquiry/')
print(d.current_url)
time.sleep(2)
d.get('https://www.google.com/')
print(d.current_url)
d.close()















import sys
sys.exit(0)
def get_title(url):
    try:
        driver=webdriver.Firefox()
        driver.get(url)  #open the url
        time.sleep(2)
        if 'STEP UP' in driver.title:
            return True
        else:
            return False
    except Exception as E:
        print(E)
    finally:
        driver.close()

def get_current_url(url):
    try:
        driver=webdriver.Firefox()
        driver.get(url)  #open the url
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        if 'admission-enquiry' in driver.current_url:
            return True
        else:
            return False
    except Exception as E:
        print(E)
    finally:
        driver.close()

