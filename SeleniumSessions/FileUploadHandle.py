from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

# type="file"
driver.find_element(By.NAME, "//input[@name='upfile']").send_keys('.//SeleniumSessions/DataFile.xls')

driver.find_element(By.XPATH, "//input[@type='submit']").click()

print("Test case completed")