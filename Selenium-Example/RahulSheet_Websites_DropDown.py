import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

Veg_List = driver.find_elements(By.XPATH,"//div[@class='products']//div//div//following::h4[contains(text(),'')]")

for name in Veg_List:
    print(name.text)
