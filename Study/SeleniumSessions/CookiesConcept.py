from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
print(driver.get_cookies())

driver.add_cookie({"name":"naveenpython","domain":"reddit.com","value":"python"})

#print(driver.get_cookies())


cookies = driver.get_cookies()

for cook in cookies:
    print(cook)
print("test case completed")

