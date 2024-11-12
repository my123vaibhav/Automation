from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
Link_List = driver.find_elements(By.TAG_NAME, "a")
for link_Name in Link_List:
    print(link_Name.get_attribute("href"))
