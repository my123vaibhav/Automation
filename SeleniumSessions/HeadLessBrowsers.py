from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
#options.headless = True
options.headless = False
options.add_argument('--incognito')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
#driver = webdriver.Chrome("D:\\pythonProject\\API-Backend-Automation\\ALL-EXE\\chromedriver.exe",options=options)


# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

driver.implicitly_wait(10)

driver.get('http://amazon.in')
print(driver.title)