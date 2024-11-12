from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)


alert = driver.switch_to.alert
print(alert.text)
alert.accept() # accept it, click on Ok

#alert.dismiss()#cancel the pop up
#alert.send_keys('hi')

driver.switch_to.default_content()

time.sleep(3)
driver.quit()