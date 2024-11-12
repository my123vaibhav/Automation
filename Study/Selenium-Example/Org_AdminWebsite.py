import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,
                    "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(5)
DashText = driver.find_element(By.XPATH,
                               "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
print(DashText)
assert DashText=="Dashboard"
