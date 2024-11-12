from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def testMethod1():
    print("This is test method1")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID,"Password").send_keys("admin")
    driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()
    driver.close()


