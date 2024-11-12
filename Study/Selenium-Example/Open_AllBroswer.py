import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()

# get the text from dropdown without select class
li = driver.find_elements(By.XPATH, "//li[@class='nav-item has-treeview']//a[@href='#']//p[contains(text(),'')]")
for i in li:
    print(i.text)
    if i.text == 'Catalog':
        i.click()
        print("I have click on :", i.text)

driver.find_element(By.XPATH,"//li[@class='nav-item has-treeview']//a[@href='#']//p[contains(text(),'Catalog')]//following::ul//li/a[@href='/Admin/Product/List']/p[contains(text(),'Products')]").click()
driver.find_element(By.XPATH, "//a[@class='nav-link'][contains(text(),'Logout')]").click()
driver.quit()
