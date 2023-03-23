from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdrivermanager import ChromeDriverManager
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
driver.get("https://www.westpac.co.nz/kiwisaver/calculators/kiwisaver-calculator/")

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'div#calculator-embed iframe'))

ele = driver.find_element(By.XPATH, "//div[@class='control text-control']//input[@class='ng-pristine ng-valid']")
ActionChains(driver).move_to_element(ele).send_keys("23").perform()
driver.find_element(By.XPATH, "(//div[@class='well-value ng-binding'])[1]").click()
empStatusList = driver.find_elements(By.CSS_SELECTOR, "ul.option-list li div.label span")
for ele in empStatusList:
    print(ele.text)
    if ele.text == "Self-employed":
        ele.click()
        break

print("Testcase Completed")
