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

driver.get('https://app.hubspot.com/login')

username_ele = driver.find_element(By.ID, 'username')
password_ele = driver.find_element(By.ID, 'password')
login_button_ele = driver.find_element(By.ID, 'loginBtn')

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username_ele, 'batchautomation@gmail.com')
act_chains.send_keys_to_element(password_ele, 'Test@12345')
act_chains.click(login_button_ele).perform()

print("test case completed")