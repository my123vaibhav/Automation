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

driver.get('http://amazon.in')

driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
time.sleep(2)

driver.back()
time.sleep(2)


driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)

driver.refresh()

driver.quit()
print("Testcase Completed")