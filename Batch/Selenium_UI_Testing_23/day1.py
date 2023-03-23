import sys
import time
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

driver.get('https://www.selenium.dev/about/')
time.sleep(5)

if driver.title=='About Selenium | Selenium':
    print('pass')
else:
    print('failed')

driver.close()

sys.exit(0)
driver=webdriver.Chrome('E:\\sel_driver\\chromedriver.exe')
driver.get('https://www.selenium.dev/about/')